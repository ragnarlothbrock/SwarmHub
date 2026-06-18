import ast
import json
from typing import Dict, Any, List, Optional
from swarmhub.core.spec import UniversalAgentSpec, WorkflowNode, WorkflowTopology, RuntimeConfig

class CrewAIEASTVisitor(ast.NodeVisitor):
    """
    Deterministically crawls a Python Abstract Syntax Tree (AST) to extract
    CrewAI task configurations if metadata is missing.
    """
    def __init__(self):
        self.tasks: List[Dict[str, Any]] = []

    def visit_Assign(self, node: ast.Assign):
        if isinstance(node.value, ast.Call) and isinstance(node.value.func, ast.Name):
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
                    
                    # Option A: Extract elements from the native tools list parameter
                    elif keyword.arg == "tools" and isinstance(keyword.value, ast.List):
                        for elt in keyword.value.elts:
                            if isinstance(elt, ast.Name):
                                task_tools.append(elt.id)
                            elif isinstance(elt, ast.Constant):
                                task_tools.append(str(elt.value))

                self.tasks.append({
                    "id": task_id.replace("_task", ""),
                    "executor_type": "opaque_blob",
                    "executor_reference": executor_ref if executor_ref != "unknown_reference" else f"blobs/{task_id}.py",
                    "transitions": [],
                    "tools": task_tools  # Maps tools to the task configuration dictionary
                })
        self.generic_visit(node)


class CrewAIParser:
    """
    Ingests raw CrewAI source code text and normalizes it into a 
    UniversalAgentSpec layout. Checks for a hidden metadata source map 
    to guarantee lossless topology restoration.
    """
    def __init__(self, source_code: str, agent_name: str = "migrated-crew-swarm"):
        self.source_code = source_code
        self.agent_name = agent_name

    def _extract_metadata(self) -> Optional[Dict[str, Any]]:
        """Scans the file lines for our hidden JSON source map comment block."""
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
            
            if inside_metadata:
                if cleaned.startswith('#'):
                    json_lines.append(cleaned[1:].strip())
                    
        if json_lines:
            try:
                return json.loads("".join(json_lines))
            except Exception:
                return None
        return None

    def parse(self) -> UniversalAgentSpec:
        # Step 1: Attempt to recover the exact topology from our source map metadata
        metadata_topology = self._extract_metadata()
        
        if metadata_topology:
            # Rehydrate the nodes directly from the recovered lossless blueprint
            processed_nodes = [WorkflowNode(**n) for n in metadata_topology.get("nodes", [])]
            return UniversalAgentSpec(
                name=self.agent_name,
                runtime=RuntimeConfig(provider="recovered_metadata", model="recovered_metadata"),
                system_prompt="Recovered losslessly via SwarmHub source map metadata.",
                topology=WorkflowTopology(
                    type=metadata_topology.get("type", "StateMachine"),
                    initial_node=metadata_topology.get("initial_node", "unknown"),
                    nodes=processed_nodes
                )
            )

        # Fallback: Parse sequentially if no metadata exists
        tree = ast.parse(self.source_code)
        visitor = CrewAIEASTVisitor()
        visitor.visit(tree)

        processed_nodes = []
        for i, task_data in enumerate(visitor.tasks):
            if i < len(visitor.tasks) - 1:
                next_task_id = visitor.tasks[i + 1]["id"]
                task_data["transitions"] = [{"on_condition": f"GOTO_{next_task_id.upper()}", "target_node": next_task_id}]
            processed_nodes.append(WorkflowNode(**task_data))

        return UniversalAgentSpec(
            name=self.agent_name,
            runtime=RuntimeConfig(provider="unknown_crew_imported", model="unknown_crew_imported"),
            system_prompt="Extracted sequentially from legacy CrewAI manifest.",
            topology=WorkflowTopology(
                type="Sequential",
                initial_node=processed_nodes[0].id if processed_nodes else "unknown_start",
                nodes=processed_nodes
            )
        )