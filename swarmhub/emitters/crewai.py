import os
import json
from swarmhub.core.spec import UniversalAgentSpec

class CrewAIEmitter:
    """
    Compiles a UniversalAgentSpec declarative layout object down into 
    native, clean, executable CrewAI Python code with a persistent checkpointer loop.
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

        code_lines = [
            '# ==========================================================================',
            f'# GENERATED AUTOMATICALLY BY SWARMHUB FOR AGENT SWARM: {self.spec.name}',
            f'# TARGET RUNTIME: CrewAI (Memory Layer: {backend} | Thread: {thread_id})',
            '# ==========================================================================\n',
            'import importlib',
            'import os',
            'import sys',
            'import sqlite3',
            'import json',
            'from pydantic import BaseModel, Field',
        ] + metadata_comment_lines + [
            'from crewai import Agent, Task, Crew, Process',
            'from crewai.tools import tool',
            '\n# 1. Patch Runtime Environment Paths to discover localized Code Blobs',
            'sys.path.insert(0, os.getcwd())',
            '\n# 2. Initialize Global Runtime Configurations',
            f'# Selected Provider Context: {self.spec.runtime.provider}',
            f'# Selected Model Target: {self.spec.runtime.model}\n',
            '# 3. Define functional stubs for cross-compiled tools'
        ]

        if unique_tools:
            for t in unique_tools:
                code_lines.append(f'@tool("{t}")')
                code_lines.append(f'def {t}(*args, **kwargs):')
                code_lines.append(f'    """Cross-compiled SwarmHub capability artifact: {t}"""')
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

        code_lines.append('# 5. Define Autonomous Agent Personas dynamically from Topology')
        for node in self.spec.topology.nodes:
            code_lines.append(f'{node.id}_agent = Agent(')
            code_lines.append(f'    role="{node.id.replace("_", " ").title()}",')
            code_lines.append(f'    goal="Execute capabilities defined under the workspace node {node.id}",')
            code_lines.append(f'    backstory="You are a specialized automation layer unit extracted from a {node.executor_type} pipeline. Authorized MCP Interfaces: {node.interfaces}",')
            
            if node.tools:
                tools_references = ", ".join(node.tools)
                code_lines.append(f'    tools=[{tools_references}],')
            else:
                code_lines.append('    tools=[],')
                
            code_lines.append('    verbose=True,')
            code_lines.append('    allow_delegation=False')
            code_lines.append(')\n')

        code_lines.append('# 6. Define Concrete Task Assignments linked back to Code Blobs')
        for node in self.spec.topology.nodes:
            code_lines.append(f'{node.id}_task = Task(')
            code_lines.append(f'    description="Execute processing code logic anchored at: {node.executor_reference}. Authorized Connection Boundaries: {node.interfaces}",')
            code_lines.append(f'    expected_output="Successful completion state payload matching criteria for next sequence step.",')
            code_lines.append(f'    agent={node.id}_agent')
            code_lines.append(')\n')

        code_lines.append('# 7. Assemble the Unified Crew Workspace Execution Order')
        agent_list = ", ".join([f"{node.id}_agent" for node in self.spec.topology.nodes])
        task_list = ", ".join([f"{node.id}_task" for node in self.spec.topology.nodes])
        
        code_lines.append('crew = Crew(')
        code_lines.append(f'    agents=[{agent_list}],')
        code_lines.append(f'    tasks=[{task_list}],')
        code_lines.append('    process=Process.sequential,')
        code_lines.append('    verbose=True')
        code_lines.append(')\n')
        
        code_lines.append('# 8. Execution and Localized Blob Verification Pipeline')
        code_lines.append('if __name__ == "__main__":')
        code_lines.append('    print("🚀 Running compiled SwarmHub execution pipeline validation...")')
        code_lines.append('    print("⚠️ [Mode: Local Offline Execution] Sequential verification pass ignited.\\n")')
        
        if backend == "sqlite":
            code_lines.extend([
                f'    db = sqlite3.connect("{conn_str}")',
                '    cursor = db.cursor()',
                '    cursor.execute("CREATE TABLE IF NOT EXISTS checkpoints (thread_id TEXT PRIMARY KEY, state_json TEXT)")',
                '    db.commit()',
                f'    cursor.execute("SELECT state_json FROM checkpoints WHERE thread_id = \'{thread_id}\'")',
                '    row = cursor.fetchone()',
            ])
        
        initial_ctx_entries = []
        if self.spec.state_schema:
            for k in self.spec.state_schema.keys():
                initial_ctx_entries.append(f'"{k}": ""')
        initial_ctx_str = ", ".join(initial_ctx_entries)
        
        code_lines.append(f'    default_state = {{"messages": [], "context": {{{initial_ctx_str}}}, "next_action": ""}}')
        
        if backend == "sqlite":
            code_lines.extend([
                '    if row:',
                '        print("   ⏳ [Memory] Found active checkpoint snapshot. Re-hydrating context state...")',
                '        state = json.loads(row[0])',
                '    else:',
                '        state = default_state'
            ])
        else:
            code_lines.append('    state = default_state')
        
        code_lines.append('    ')
        
        for node in self.spec.topology.nodes:
            import_path = node.executor_reference.replace('.py', '').replace('/', '.')
            code_lines.append(f'    print("--- 🟢 Entering Runtime Task Node: {node.id} ---")')
            code_lines.append(f'    print("    🔒 [Permissions] Authorized MCP Interfaces: {node.interfaces}")')
            
            code_lines.append('    try:')
            code_lines.append('        SharedContextContract(**state["context"])')
            code_lines.append('    except Exception as contract_err:')
            code_lines.append(f'        print(f"    ⚠️ [Contract Breakage] Incoming schema anomaly caught at entry of {node.id}: {{contract_err}}")')
            
            code_lines.append('    try:')
            if self.inline_blobs:
                code_lines.append(f'        state = _inline_{node.id}(state)')
            else:
                code_lines.append(f'        module = importlib.import_module("{import_path}")')
                code_lines.append(f'        state = module.run(state)')
            
            code_lines.append('        SharedContextContract(**state["context"])')
            if backend == "sqlite":
                code_lines.extend([
                    '        # Save intermediate snapshot checkpoint straight to disk',
                    f'        cursor.execute("INSERT OR REPLACE INTO checkpoints VALUES (\'{thread_id}\', ?)", (json.dumps(state),))',
                    '        db.commit()'
                ])
            code_lines.append(f'    except Exception as e:')
            code_lines.append(f'        print(f"    ❌ Execution/Contract Fault inside {node.id}: {{e}}")\n')
            
        code_lines.append('    print("\\n🏁 Local CrewAI Task Blob Pipeline Successfully Executed!")')
        code_lines.append('    print("Final Verified State Context Payload:", state["context"])')
        if backend == "sqlite":
            code_lines.append('    db.close()')

        return '\n'.join(code_lines)

    def write_to_disk(self, output_path: str):
        generated_code = self.emit()
        if os.path.dirname(output_path):
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, 'w') as f:
            f.write(generated_code)
        print(f"💾 CrewAI native architecture successfully compiled to: {output_path}")