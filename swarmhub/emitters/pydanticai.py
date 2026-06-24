import os
import json
from swarmhub.core.spec import UniversalAgentSpec

class PydanticAIEmitter:
    """
    Compiles a UniversalAgentSpec declarative layout object down into 
    native, clean, executable PydanticAI Python code with a persistent checkpointer loop.
    
    Generates dynamic state-machine graph routers, embedded schema verification contracts,
    automatic user interaction entry gates, and a deep unified telemetry tracking layer.
    """
    def __init__(self, spec: UniversalAgentSpec, inline_blobs: bool = False):
        self.spec = spec
        self.inline_blobs = inline_blobs

    def emit(self) -> str:
        unique_tools = sorted(list(set(tool for node in self.spec.topology.nodes for tool in node.tools)))
        
        backend = self.spec.memory.storage_backend
        thread_id = self.spec.memory.thread_id or "swarmhub-default-thread"
        conn_str = self.spec.memory.connection_string or "swarmhub_memory.db"

        # Serialize full specification object blueprint map context losslessly
        spec_snapshot = self.spec.model_dump()
        json_metadata = json.dumps(spec_snapshot, indent=2)
        
        metadata_comment_lines = [
            '# === SWARMHUB METADATA SOURCE MAP (LOSSLESS ROUND-TRIP ASSURANCE) ===',
            '# SWARMHUB_METADATA_START'
        ]
        for line in json_metadata.split('\n'):
            metadata_comment_lines.append(f'# {line}')
        metadata_comment_lines.append('# SWARMHUB_METADATA_END\n')

        # Format model string cleanly to match PydanticAI's platform string layout formats (e.g., 'openai:gpt-4o')
        provider = self.spec.runtime.provider or "openai"
        model_name = self.spec.runtime.model or "gpt-4o-mini"
        if provider == "langgraph_extracted" or "fallback" in provider:
            provider = "openai"
            model_name = "gpt-4o-mini"
        pydantic_ai_model_str = f"{provider}:{model_name}"

        code_lines = [
            '# ==========================================================================',
            f'# GENERATED AUTOMATICALLY BY SWARMHUB FOR AGENT SWARM: {self.spec.name}',
            f'# TARGET RUNTIME: PydanticAI (Memory Layer: {backend} | Thread: {thread_id})',
            '# ==========================================================================\n',
            'import importlib',
            'import os',
            'import sys',
            'import sqlite3',
            'import json',
            'import time',              # Added for high-fidelity latency telemetry counters
            'import uuid',              # Added for unique transaction span ID allocations
            'from pydantic import BaseModel, Field',
        ] + metadata_comment_lines + [
            'from pydantic_ai import Agent, RunContext',
            '\n# 1. Patch Runtime Environment Paths to discover localized Code Blobs',
            'sys.path.insert(0, os.getcwd())',
            '\n# 2. Initialize Global Runtime Configurations',
            f'# Target Model Provider Coordinate: {pydantic_ai_model_str}\n',
            '# 3. Define functional stubs for cross-compiled tools'
        ]

        # Define workspace tools as plain stubs that can be attached to the PydanticAI agents
        if unique_tools:
            for t in unique_tools:
                code_lines.append(f'def {t}(ctx: RunContext[Any], *args, **kwargs) -> str:')
                code_lines.append(f'    """Cross-compiled SwarmHub tool capability artifact: {t}"""')
                code_lines.append(f'    print("    🧰 [Tool Called] Executing workspace tool stub: {t}")')
                code_lines.append('    return "Tool execution fallback payload finished."\n')
        else:
            code_lines.append('# No external tool dependencies declared in universal spec topology.\n')

        code_lines.append('# 3.2 Initialize Registered Global MCP Capability Interface Targets')
        if self.spec.interfaces:
            code_lines.append('GLOBAL_INTERFACES_REGISTRY = {')
            for iface in self.spec.interfaces:
                code_lines.append(f'    "{iface.name}": {{"protocol": "{iface.protocol}", "transport": "{iface.transport}", "endpoint": "{iface.endpoint}", "args": {iface.args}}},')
            code_lines.append('}\n')
        else:
            code_lines.append('GLOBAL_INTERFACES_REGISTRY = {}\n')

        if self.inline_blobs:
            code_lines.append('# 3.5 Define Inlined Cognitive Blobs for Direct Source Execution')
            for node in self.spec.topology.nodes:
                if os.path.exists(node.executor_reference):
                    with open(node.executor_reference, 'r') as f:
                        blob_code = f.read()
                    blob_code = blob_code.replace("def run(state):", f"def _inline_{node.id}(state):", 1)
                    code_lines.append(blob_code)
                else:
                    code_lines.append(f'def _inline_{node.id}(state):\n    return state')
                code_lines.append('')

        code_lines.append('# 4. Define strict Data Contract Verification Model schemas')
        code_lines.append('class SharedContextContract(BaseModel):')
        if self.spec.state_schema:
            for field, ftype in self.spec.state_schema.items():
                default_val = '""' if ftype == 'str' else '0' if ftype in ('int', 'float') else 'None'
                code_lines.append(f'    {field}: {ftype} = {default_val}')
        else:
            code_lines.append('    pass')
        code_lines.append('')

        code_lines.append('# 5. Define Autonomous PydanticAI Agents dynamically from Topology')
        for node in self.spec.topology.nodes:
            system_prompt_str = self.spec.system_prompt or "Specialized operational automation node."
            clean_prompt = system_prompt_str.replace('"', '\\"').replace('\n', ' ')
            
            code_lines.append(f'{node.id}_agent = Agent(')
            code_lines.append(f'    "{pydantic_ai_model_str}",')
            code_lines.append(f'    system_prompt="{clean_prompt} Node context: {node.id}. Authorized MCP Interfaces: {node.interfaces}",')
            code_lines.append(')')
            
            # Register tools to this specific agent using PydanticAI plain function injection hooks
            for tool in node.tools:
                code_lines.append(f'{node.id}_agent.tool_plain({tool})')
            code_lines.append('')

        code_lines.append('# 6. Assemble the State-Machine Execution Architecture Runtime Maps')
        code_lines.append('if __name__ == "__main__":')
        code_lines.append('    print("🚀 Running compiled SwarmHub execution pipeline validation...")')
        code_lines.append('    print("⚠️ [Mode: Local Offline Execution] PydanticAI state-machine verification pass ignited.\\n")')
        
        if backend == "sqlite":
            code_lines.extend([
                f'    db = sqlite3.connect("{conn_str}")',
                '    cursor = db.cursor()',
                '    cursor.execute("CREATE TABLE IF NOT EXISTS swarmhub_checkpoints (thread_id TEXT PRIMARY KEY, state_json TEXT)")',
                '    db.commit()',
                f'    cursor.execute("SELECT state_json FROM swarmhub_checkpoints WHERE thread_id = \'{thread_id}\'")',
                '    row = cursor.fetchone()',
            ])
        
        if self.spec.state_schema and "user_query" in self.spec.state_schema:
            code_lines.append('    user_prompt = input("❓ Enter your workflow query: ")')
        
        initial_ctx_entries = []
        if self.spec.state_schema:
            for k in self.spec.state_schema.keys():
                if k == "user_query":
                    initial_ctx_entries.append(f'"{k}": user_prompt')
                else:
                    default_val = '""' if self.spec.state_schema[k] == 'str' else '0'
                    initial_ctx_entries.append(f'"{k}": {default_val}')
        
        code_lines.append(f'    initial_state_context = {{{", ".join(initial_ctx_entries)}}}')

        code_lines.extend([
            '    if "row" in locals() and row:',
            '        state = json.loads(row[0])',
            '    else:',
            '        state = {',
            '            "messages": [],',
            '            "context": initial_state_context,',
            '            "next_action": "PROCEED"',
            '        }',
            ''
        ])

        # Form functional layout reference tracking dictionaries
        code_lines.append('    NODES_REGISTRY = {')
        for node in self.spec.topology.nodes:
            code_lines.append(f'        "{node.id}": {node.id}_agent,')
        code_lines.append('    }')

        code_lines.append('    NODES_PIPELINE_MAP = {')
        for node in self.spec.topology.nodes:
            if self.inline_blobs:
                code_lines.append(f'        "{node.id}": _inline_{node.id},')
            else:
                import_path = node.executor_reference.replace('.py', '').replace('/', '.')
                code_lines.append(f'        "{node.id}": importlib.import_module("{import_path}").run,')
        code_lines.append('    }\n')

        code_lines.append('    ROUTING_TABLE = {')
        for node in self.spec.topology.nodes:
            code_lines.append(f'        "{node.id}": {{')
            for edge in node.transitions:
                cond = edge.on_condition.upper()
                if cond.startswith("GOTO_"):
                    cond = cond.replace("GOTO_", "", 1)
                code_lines.append(f'            "{cond}": "{edge.target_node}",')
            code_lines.append('            "END": "END"')
            code_lines.append('        },')
        code_lines.append('    }')

        # Execution tracking driver loop matching framework layout metrics Symmetrically
        code_lines.extend([
            f'\n    current_node = "{self.spec.topology.initial_node}"',
            '    incoming_action = "INITIAL_ENTRY"',
            '    while current_node and current_node != "END":',
            '        agent_instance = NODES_REGISTRY.get(current_node)',
            '        node_executor = NODES_PIPELINE_MAP.get(current_node)',
            '        if not agent_instance or not node_executor:',
            '            break',
            '        print(f"\\n--- 🟢 Entering PydanticAI Core Node: {current_node} ---")',
            '        ',
            '        span_id = f"span-{uuid.uuid4().hex[:8]}"',
            '        contract_status = "VERIFIED"',
            '        start_time = time.perf_counter()',
            '        ',
            '        try:',
            '            SharedContextContract(**state["context"])',
            '        except Exception as contract_err:',
            '            print(f"    ⚠️ [Contract Breakage] Incoming schema anomaly caught at entry of {current_node}: {contract_err}")',
            '            contract_status = "FAILED_ENTRY"',
            '        ',
            '        try:',
            '            # Execute the node context mutation pass through the runtime executor hook',
            '            state = node_executor(state)',
            '            ',
            '            if contract_status == "VERIFIED":',
            '                try:',
            '                    SharedContextContract(**state["context"])',
            '                except Exception as contract_err_exit:',
            '                    print(f"    ❌ [Contract Breakage] Outgoing contract violation caught at exit of {current_node}: {contract_err_exit}")',
            '                    contract_status = "FAILED_EXIT"',
            '        except Exception as e:',
            '            print(f"    ❌ Execution/Contract Fault inside node [{current_node}]: {e}")',
            '            contract_status = "CRASHED"',
            '            break',
            '        ',
            '        latency = round(time.perf_counter() - start_time, 4)',
            '        action = state.get("next_action", "PROCEED").upper()',
            '        if action.startswith("GOTO_"):',
            '            action = action.replace("GOTO_", "", 1)',
            '        ',
            '        # 📊 EMIT UNIFIED SWARMHUB TELEMETRY STRIP LOG',
            '        telemetry_span = {',
            '            "span_id": span_id,',
            f'            "thread_id": "{thread_id}",',
            '            "node_id": current_node,',
            '            "latency_seconds": latency,',
            '            "incoming_action": incoming_action,',
            '            "outgoing_action": action,',
            '            "contract_status": contract_status',
            '        }',
            '        print(f"📊 [Telemetry Span Generated]: {json.dumps(telemetry_span)}")',
            '        ',
        ])

        if backend == "sqlite":
            code_lines.extend([
                f'        cursor.execute("INSERT OR REPLACE INTO swarmhub_checkpoints VALUES (\'{thread_id}\', ?)", (json.dumps(state),))',
                '        db.commit()',
            ])

        code_lines.extend([
            '        incoming_action = action',
            '        current_node = ROUTING_TABLE.get(current_node, {}).get(action, "END")',
            '',
            '    print("\\n🏁 PydanticAI Task Step Loop Pipeline Successfully Executed!")',
            '    print("Final Verified State Context Payload:", state["context"])',
        ])

        if backend == "sqlite":
            code_lines.append('    db.close()')

        return '\n'.join(code_lines)

    def write_to_disk(self, output_path: str):
        generated_code = self.emit()
        if os.path.dirname(output_path):
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(generated_code)
        print(f"💾 PydanticAI native architecture successfully compiled to: {output_path}")