import ast
from typing import Dict, Any, List
from swarmhub.core.spec import UniversalAgentSpec, WorkflowNode, WorkflowTopology, RuntimeConfig

class LangGraphASTVisitor(ast.NodeVisitor):
    """
    Deterministically crawls a Python Abstract Syntax Tree (AST) to extract
    LangGraph topology structure (nodes, edges, initial pointers, and bound tools).
    """
    def __init__(self):
        self.nodes: List[Dict[str, Any]] = []
        self.edges: List[tuple] = []
        self.initial_node: str = ""
        self.globally_bound_tools: List[str] = []

    def visit_Call(self, node: ast.Call):
        if isinstance(node.func, ast.Attribute):
            method_name = node.func.attr
            
            # 1. Parse workflow.add_node("node_name", function)
            if method_name == "add_node" and len(node.args) >= 1:
                first_arg = node.args[0]
                if isinstance(first_arg, ast.Constant):
                    node_id = first_arg.value
                    self.nodes.append({
                        "id": node_id,
                        "executor_type": "opaque_blob",
                        "executor_reference": f"extracted_blobs/{node_id}.py",
                        "transitions": [],
                        "tools": []  # Option A: Initialized empty tools array
                    })

            # 2. Parse workflow.add_edge(START, "node_name")
            elif method_name == "add_edge" and len(node.args) >= 2:
                arg1, arg2 = node.args[0], node.args[1]
                val1 = arg1.value if isinstance(arg1, ast.Constant) else getattr(arg1, 'id', str(arg1))
                val2 = arg2.value if isinstance(arg2, ast.Constant) else getattr(arg2, 'id', str(arg2))
                
                if val1 == "START":
                    self.initial_node = val2
                else:
                    self.edges.append((val1, val2))
            
            # 3. Static Tool Extraction: Detect model.bind_tools([tool_a, tool_b])
            elif method_name == "bind_tools" and len(node.args) >= 1:
                first_arg = node.args[0]
                if isinstance(first_arg, ast.List):
                    for elt in first_arg.elts:
                        if isinstance(elt, ast.Name):
                            self.globally_bound_tools.append(elt.id)
                        elif isinstance(elt, ast.Constant):
                            self.globally_bound_tools.append(str(elt.value))
                    
        self.generic_visit(node)


class LangGraphParser:
    """
    Ingests raw legacy LangGraph source code and outputs a structured
    UniversalAgentSpec file model ready for mutation or cross-compilation.
    """
    def __init__(self, source_code: str, agent_name: str = "imported-legacy-agent"):
        self.source_code = source_code
        self.agent_name = agent_name

    def parse(self) -> UniversalAgentSpec:
        tree = ast.parse(self.source_code)
        visitor = LangGraphASTVisitor()
        visitor.visit(tree)

        # Reconstruct standard edge transitions and bind discovered tools
        processed_nodes = []
        for node_data in visitor.nodes:
            node_id = node_data["id"]
            transitions = []
            
            for src, dest in visitor.edges:
                if src == node_id:
                    transitions.append({
                        "on_condition": f"GOTO_{dest.upper()}",
                        "target_node": dest
                    })
            
            node_data["transitions"] = transitions
            
            # Fallback: distribute globally discovered tools to nodes if metadata is absent
            if visitor.globally_bound_tools:
                node_data["tools"] = list(set(visitor.globally_bound_tools))
                
            processed_nodes.append(WorkflowNode(**node_data))

        return UniversalAgentSpec(
            name=self.agent_name,
            runtime=RuntimeConfig(
                provider="unknown_imported",
                model="unknown_imported",
                temperature=0.2
            ),
            system_prompt="Extracted automatically via SwarmHub static AST analysis.",
            topology=WorkflowTopology(
                type="StateMachine",
                initial_node=visitor.initial_node or "unknown_start",
                nodes=processed_nodes
            )
        )