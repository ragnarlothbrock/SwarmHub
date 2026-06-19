import ast
import os
import json
from typing import Dict, Any, List, Optional
from swarmhub.core.spec import UniversalAgentSpec, WorkflowNode, WorkflowTopology, RuntimeConfig, MemoryConfig, InterfaceConfig

class CrewAIEASTVisitor(ast.NodeVisitor):
    """
    Deterministically crawls a Python Abstract Syntax Tree (AST) to extract
    CrewAI task configurations, tools, and baseline execution parameters.
    """
    def __init__(self, source_lines: List[str]):
        self.source_lines = source_lines
        self.tasks: List[Dict[str, Any]] = []
        self.function_bodies: Dict[str, str] = {}
        self.has_memory_flag: bool = False

    def visit_FunctionDef(self, node: ast.FunctionDef):
        """Slices out any custom tools or helper routines declared inside the file."""
        start_line = node.lineno - 1
        end_line = node.end_lineno
        function_code_lines = self.source_lines[start_line:end_line]
        
        if function_code_lines:
            leading_spaces = len(function_code_lines[0]) - len(function_code_lines[0].lstrip())
            function_code_lines[0] = " " * leading_spaces + "def run(state):"
            
        self.function_bodies[node.name] = "\n".join(function_code_lines)
        self.generic_visit(node)

    def visit_Assign(self, node: ast.Assign):
        if isinstance(node.value, ast.Call) and isinstance(node.value.func, ast.Name):
            if node.value.func.id in ("Agent", "Crew"):
                for kw in node.value.keywords:
                    if kw.arg == "memory" and isinstance(kw.value, ast.Constant) and kw.value.value is True:
                        self.has_memory_flag = True

            if node.value.func.id == "Task":
                task_id = "unknown_task"
                if node.targets and isinstance(node.targets[0], ast.Name):
                    task_id = node.targets[0].id

                description = "No description found"
                executor_ref = "unknown_reference"
                task_tools = []
                
                for keyword in node.value.keywords:
                    if keyword.arg == "description" and isinstance(keyword.value, ast.Constant):
                        description = keyword.value.value
                        if "anchored at:" in description:
                            executor_ref = description.split("anchored at:")[-1].strip()
                    
                    elif keyword.arg == "tools" and isinstance(keyword.value, ast.List):
                        for elt in keyword.value.elts:
                            if isinstance(elt, ast.Name):
                                task_tools.append(elt.id)
                            elif isinstance(elt, ast.Constant):
                                task_tools.append(str(elt.value))

                clean_id = task_id.replace("_task", "")
                self.tasks.append({
                    "id": clean_id,
                    "executor_type": "opaque_blob",
                    "executor_reference": executor_ref if executor_ref != "unknown_reference" else f"blobs/{clean_id}.py",
                    "transitions": [],
                    "tools": task_tools,
                    "interfaces": [],
                    "_description_context": description
                })
        self.generic_visit(node)


class CrewAIParser:
    """
    Ingests raw CrewAI source code text and normalizes it into a 
    UniversalAgentSpec layout, auto-extracting capabilities and metadata maps.
    """
    def __init__(self, source_code: str, agent_name: str = "migrated-crew-swarm"):
        self.source_code = source_code
        self.agent_name = agent_name

    def _extract_metadata(self) -> Optional[Dict[str, Any]]:
        lines = self.source_code.split('\n')
        inside_metadata = False
        json_lines = []
        
        for line in lines:
            cleaned = line.strip()
            if cleaned == "# SWARMHUB_METADATA_START":
                inside_metadata = True
                continue
            elif cleaned == "# SWARMHUB_METADATA_END":
                inside_metadata = False
                break
            
            if inside_metadata and cleaned.startswith('#'):
                json_lines.append(cleaned[1:].strip())
                    
        if json_lines:
            try:
                return json.loads("".join(json_lines))
            except Exception:
                return None
        return None

    def parse(self) -> UniversalAgentSpec:
        spec_metadata = self._extract_metadata()
        
        if spec_metadata:
            topology_data = spec_metadata.get("topology", {})
            processed_nodes = [WorkflowNode(**n) for n in topology_data.get("nodes", [])]
            memory_data = spec_metadata.get("memory", {"storage_backend": "in_memory"})
            interfaces_data = spec_metadata.get("interfaces", [])
            interfaces = [InterfaceConfig(**i) for i in interfaces_data]
            
            return UniversalAgentSpec(
                name=self.agent_name,
                runtime=RuntimeConfig(**spec_metadata.get("runtime", {"provider": "recovered_metadata", "model": "recovered_metadata"})),
                memory=MemoryConfig(**memory_data),
                interfaces=interfaces,
                system_prompt=spec_metadata.get("system_prompt", "Recovered losslessly via SwarmHub source map metadata."),
                topology=WorkflowTopology(
                    type=topology_data.get("type", "StateMachine"),
                    initial_node=topology_data.get("initial_node", "unknown"),
                    nodes=processed_nodes
                )
            )

        # Fallback Source-Slicing Mode
        source_lines = self.source_code.split("\n")
        tree = ast.parse(self.source_code)
        visitor = CrewAIEASTVisitor(source_lines)
        visitor.visit(tree)

        processed_nodes = []
        os.makedirs("blobs", exist_ok=True)

        for i, task_data in enumerate(visitor.tasks):
            node_id = task_data["id"]
            desc = task_data.pop("_description_context", "")
            
            if i < len(visitor.tasks) - 1:
                next_task_id = visitor.tasks[i + 1]["id"]
                task_data["transitions"] = [{"on_condition": f"GOTO_{next_task_id.upper()}", "target_node": next_task_id}]
            
            if node_id in visitor.function_bodies:
                blob_code = visitor.function_bodies[node_id]
            else:
                blob_code = (
                    "def run(state):\n"
                    f"    print('    🎯 Executing extracted legacy task workflow: {node_id}')\n"
                    f"    # Task Context: {desc.strip()}\n"
                    "    state['context']['last_completed_step'] = '" + node_id + "'\n"
                    "    return state\n"
                )
                
            with open(f"blobs/{node_id}.py", "w") as f:
                f.write(blob_code)
                
            processed_nodes.append(WorkflowNode(**task_data))

        return UniversalAgentSpec(
            name=self.agent_name,
            runtime=RuntimeConfig(provider="unknown_crew_imported", model="unknown_crew_imported"),
            memory=MemoryConfig(storage_backend="in_memory"),
            interfaces=[],
            system_prompt="Extracted sequentially from legacy CrewAI manifest.",
            topology=WorkflowTopology(
                type="Sequential",
                initial_node=processed_nodes[0].id if processed_nodes else "unknown_start",
                nodes=processed_nodes
            )
        )