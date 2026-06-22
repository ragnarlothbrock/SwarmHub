import os
import json
from swarmhub.core.spec import UniversalAgentSpec

class LangGraphEmitter:
    """
    Compiles a UniversalAgentSpec declarative object down into 
    a pristine, native, executable LangGraph Python script.
    
    Generates and injects strict runtime Pydantic contract validation hooks,
    inline compilation capabilities, database thread checkpointers, and MCP tool interfaces.
    """
    def __init__(self, spec: UniversalAgentSpec, inline_blobs: bool = False):
        self.spec = spec
        self.inline_blobs = inline_blobs

    def emit(self) -> str:
        unique_tools = sorted(list(set(tool for node in self.spec.topology.nodes for tool in node.tools)))
        
        # Pull configuration snapshot parameters
        backend = self.spec.memory.storage_backend
        thread_id = self.spec.memory.thread_id or "swarmhub-default-thread"
        conn_str = self.spec.memory.connection_string or "swarmhub_memory.db"

        code_lines = [
            '# ==========================================================================',
            f'# GENERATED AUTOMATICALLY BY SWARMHUB FOR AGENT: {self.spec.name}',
            f'# TARGET RUNTIME: LangGraph (Memory Layer: {backend} | Thread: {thread_id})',
            '# ==========================================================================\n',
            'import importlib',
            'import os',
            'import sys',
            'import sqlite3',
            'import json',
            'import subprocess',
            'from typing import Annotated, Dict, Any, List',
            'from typing_extensions import TypedDict',
            'from pydantic import BaseModel, Field',
            'from langgraph.graph import StateGraph, START, END',
        ]

        # Inject corresponding native memory checkpointer library imports
        if backend == "sqlite":
            code_lines.append('from langgraph.checkpoint.sqlite import SqliteSaver')
        else:
            code_lines.append('from langgraph.checkpoint.memory import MemorySaver')

        code_lines.extend([
            '\n# 1. Patch Runtime Environment Paths to discover localized Code Blobs',
            'sys.path.insert(0, os.getcwd())',
            '\n# 2. Define functional stubs for cross-compiled tools'
        ])

        if unique_tools:
            for tool in unique_tools:
                code_lines.append(f'def {tool}(*args, **kwargs):')
                code_lines.append(f'    print("    🧰 [Tool Called] Executing workspace capability tool: {tool}")')
                code_lines.append('    return "Tool execution fallback payload successfully completed."\n')
        else:
            code_lines.append('# No external tool dependencies declared in universal spec topology.\n')

        # 2.5 Generate Global MCP / Interface Environment Capabilities Manifest
        code_lines.append('# 2.5 Initialize Registered Global MCP Capability Interface Targets')
        if self.spec.interfaces:
            code_lines.append('GLOBAL_INTERFACES_REGISTRY = {')
            for iface in self.spec.interfaces:
                code_lines.append(f'    "{iface.name}": {{')
                code_lines.append(f'        "protocol": "{iface.protocol}",')
                code_lines.append(f'        "transport": "{iface.transport}",')
                code_lines.append(f'        "endpoint": "{iface.endpoint}",')
                code_lines.append(f'        "args": {iface.args}')
                code_lines.append('    },')
            code_lines.append('}\n')
            
            # Emit standard MCP shell execution connection wrapper
            code_lines.extend([
                'def call_mcp_interface(interface_name: str, method: str, params: dict) -> Any:',
                '    if interface_name not in GLOBAL_INTERFACES_REGISTRY:',
                '        raise ValueError(f"Target interface \'{interface_name}\' not found in global spec context.")',
                '    cfg = GLOBAL_INTERFACES_REGISTRY[interface_name]',
                '    print(f"    🔌 [MCP Client] Dispatching RPC transaction over {cfg[\'transport\']} to server: {interface_name}")',
                '    if cfg["transport"] == "stdio":',
                '        # Simulating standard text execution boundary over stdin/stdout channels',
                '        return f"MCP stdio sub-process [{cfg[\'endpoint\']}] simulated response completed successfully."',
                '    return f"MCP network connection [{cfg[\'endpoint\']}] request resolved successfully."\n'
            ])
        else:
            code_lines.append('GLOBAL_INTERFACES_REGISTRY = {}\n')

        # 3. Dynamic Compilation of the Pydantic Context Guardrail Contract
        code_lines.append('# 3. Define strict Data Contract Verification Model schemas')
        code_lines.append('class SharedContextContract(BaseModel):')
        if self.spec.state_schema:
            for field, ftype in self.spec.state_schema.items():
                default_val = '""' if ftype == 'str' else '0' if ftype in ('int', 'float') else 'None'
                code_lines.append(f'    {field}: {ftype} = {default_val}')
        else:
            code_lines.append('    pass  # Loose empty context contract layout placeholder')
        code_lines.append('')

        code_lines.extend([
            '# 4. Define the global State layout contract',
            'class AgentState(TypedDict):',
            '    messages: list',
            '    context: Dict[str, Any]',
            '    next_action: str',
            '\n# 5. Re-hydrate Execution Anchors and Bind Run Methods'
        ])

        # Inject contract validation checks into the node wrappers
        for node in self.spec.topology.nodes:
            import_path = node.executor_reference.replace('.py', '').replace('/', '.')
            
            if self.inline_blobs:
                code_lines.append(f'# --- INLINED COGNITIVE LOGIC FOR ACTOR: {node.id} ---')
                if os.path.exists(node.executor_reference):
                    with open(node.executor_reference, 'r') as f:
                        blob_code = f.read()
                    blob_code = blob_code.replace("def run(state):", f"def _inline_{node.id}(state):", 1)
                    code_lines.append(blob_code)
                else:
                    code_lines.append(f'def _inline_{node.id}(state):\n    print("⚠️ Source file missing during compilation.")\n    return state')
                code_lines.append('')

            code_lines.append(f'def {node.id}(state: AgentState) -> AgentState:')
            code_lines.append(f'    print(f"\\n--- 🟢 Entering Runtime Node: {node.id} ---")')
            code_lines.append(f'    print(f"    🔒 [Permissions] Authorized MCP Interfaces: {node.interfaces}")')
            
            # Entry Guardrail Check
            code_lines.append('    try:')
            code_lines.append('        SharedContextContract(**state["context"])')
            code_lines.append('    except Exception as contract_err:')
            code_lines.append(f'        print(f"    ⚠️ [Contract Breakage] Incoming schema anomaly caught at entry of {node.id}: {{contract_err}}")')
            
            # Core Routing Branch Divergence
            code_lines.append('    try:')
            if self.inline_blobs:
                code_lines.append(f'        state = _inline_{node.id}(state)')
            else:
                code_lines.append(f'        module = importlib.import_module("{import_path}")')
                code_lines.append(f'        state = module.run(state)')
            
            # Exit Guardrail Check
            code_lines.append('        SharedContextContract(**state["context"])')
            code_lines.append('    except Exception as e:')
            code_lines.append(f'        print(f"    ❌ Execution/Contract Fault inside {node.id}: {{e}}")')
            
            if not node.transitions:
                code_lines.append('        state["next_action"] = "END"')
                
            code_lines.append('    return state\n')

        # 6. Construct the graph structural topology map
        code_lines.append('# 6. Build the workflow graph structural topology')
        code_lines.append('workflow = StateGraph(AgentState)\n')

        for node in self.spec.topology.nodes:
            code_lines.append(f'workflow.add_node("{node.id}", {node.id})')
        
        code_lines.append(f'\nworkflow.add_edge(START, "{self.spec.topology.initial_node}")')

        # 🚀 Inject the native routing normalizer function to reconcile blob string semantics
        code_lines.extend([
            '\n# Symmetrical routing normalizer to resolve action tokens dynamically',
            'def route_normalizer(state: AgentState) -> str:',
            '    action = state.get("next_action", "END").upper()',
            '    if not action.startswith("GOTO_") and action != "END":',
            '        return f"GOTO_{action}"',
            '    return action'
        ])

        code_lines.append('\n# Define routing conditions rules')
        for node in self.spec.topology.nodes:
            if node.transitions:
                path_map_entries = []
                for transition in node.transitions:
                    cond = transition.on_condition.upper()
                    cond_fixed = cond if cond.startswith("GOTO_") else f"GOTO_{cond}"
                    path_map_entries.append(f'        "{cond_fixed}": "{transition.target_node}"')
                path_map_entries.append('        "GOTO_END": END')
                path_map_entries.append('        "END": END')
                path_map_str = ",\n".join(path_map_entries)
                
                code_lines.append(
                    f'workflow.add_conditional_edges(\n'
                    f'    "{node.id}",\n'
                    f'    route_normalizer,\n'
                    f'    {{\n{path_map_str}\n    }}\n'
                    f')'
                )
            else:
                code_lines.append(f'workflow.add_edge("{node.id}", END)')

        # Instantiate Memory Checkpointer Instance
        code_lines.append('\n# 6.5 Mount Checkpointer System Instance')
        if backend == "sqlite":
            code_lines.append(f'db_conn = sqlite3.connect("{conn_str}", check_same_thread=False)')
            code_lines.append('memory_saver = SqliteSaver(db_conn)')
        else:
            code_lines.append('memory_saver = MemorySaver()')

        code_lines.append('\n# 7. Compile the graph execution app binary with active checkpointer')
        code_lines.append('app = workflow.compile(checkpointer=memory_saver)')
        
        # Driver block with memory initialization mapping
        code_lines.append('\nif __name__ == "__main__":')
        code_lines.append('    print("🚀 Running compiled SwarmHub execution pipeline validation...")')
        
        # 📥 Dynamic terminal prompt compiler injection pass
        if self.spec.state_schema and "user_query" in self.spec.state_schema:
            code_lines.append('    user_prompt = input("\\n❓ Enter your workflow query: ")')
        
        initial_ctx_entries = []
        if self.spec.state_schema:
            for k in self.spec.state_schema.keys():
                if k == "user_query":
                    initial_ctx_entries.append('"user_query": user_prompt')
                elif self.spec.state_schema[k] == "int":
                    initial_ctx_entries.append(f'"{k}": 0')
                else:
                    initial_ctx_entries.append(f'"{k}": ""')
        initial_ctx_str = ", ".join(initial_ctx_entries)
        
        code_lines.append(f'    initial_state = {{"messages": [], "context": {{{initial_ctx_str}}}, "next_action": ""}}')
        code_lines.append(f'    execution_config = {{"configurable": {{"thread_id": "{thread_id}"}}}}')
        code_lines.append('    final_output = app.invoke(initial_state, config=execution_config)')
        code_lines.append('    print("\\n🏁 Workflow Execution Successfully Finished!")')
        code_lines.append('    print("Final State Context Payload:", final_output["context"])')
        
        return '\n'.join(code_lines)

    def write_to_disk(self, output_path: str):
        generated_code = self.emit()
        if os.path.dirname(output_path):
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, 'w') as f:
            f.write(generated_code)
        print(f"💾 Production LangGraph output compiled to: {output_path}")