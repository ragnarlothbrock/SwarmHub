import ast
import os
from typing import Dict, Any, List
from swarmhub.core.spec import UniversalAgentSpec, WorkflowNode, WorkflowTopology, RuntimeConfig, MemoryConfig, InterfaceConfig

class LangGraphASTVisitor(ast.NodeVisitor):
    """
    Deterministically crawls a Python Abstract Syntax Tree (AST) to extract
    LangGraph topology structure, code bodies, memory checkpointer properties, and tools.
    """
    def __init__(self, source_lines: List[str]):
        self.source_lines = source_lines
        self.nodes: List[Dict[str, Any]] = []
        self.edges: List[tuple] = []
        self.initial_node: str = ""
        self.globally_bound_tools: List[str] = []
        self.function_bodies: Dict[str, str] = {}
        
        # Memory Layer Extraction Pointers
        self.memory_backend: str = "in_memory"
        self.thread_id: str = "swarmhub-recovered-thread"
        self.connection_string: str = "swarmhub_memory.db"
        
        # Global Interfaces Layer Pool
        self.interfaces: List[InterfaceConfig] = []

    def _resolve_node_name(self, node: ast.AST) -> str:
        """Converts an abstract AST expression or reference safely into a human-readable identifier."""
        if isinstance(node, ast.Constant):
            return str(node.value)
        elif isinstance(node, ast.Name):
            return node.id
        else:
            try:
                # Safe unparse fallback to serialize complex dynamic lookups/ternaries without object pointer leaks
                return ast.unparse(node).strip().replace("'", "").replace('"', "")
            except Exception:
                return "unknown_node"

    def visit_FunctionDef(self, node: ast.FunctionDef):
        """Locates and slices the raw Python string body of legacy node functions."""
        start_line = node.lineno - 1
        end_line = node.end_lineno
        function_code_lines = self.source_lines[start_line:end_line]
        
        if function_code_lines:
            leading_spaces = len(function_code_lines[0]) - len(function_code_lines[0].lstrip())
            function_code_lines[0] = " " * leading_spaces + "def run(state):"
            
        self.function_bodies[node.name] = "\n".join(function_code_lines)
        self.generic_visit(node)

    def visit_Assign(self, node: ast.Assign):
        """Captures variable allocations defined out-of-line."""
        if isinstance(node.value, ast.Call):
            call_id = ""
            if isinstance(node.value.func, ast.Name):
                call_id = node.value.func.id
            elif isinstance(node.value.func, ast.Attribute):
                call_id = node.value.func.attr
                
            if call_id == "connect" and node.value.args:
                if isinstance(node.value.args[0], ast.Constant):
                    self.connection_string = str(node.value.args[0].value)
                    self.memory_backend = "sqlite"

        if isinstance(node.value, ast.Dict):
            for k, v in zip(node.value.keys, node.value.values):
                if isinstance(k, ast.Constant) and k.value == "configurable" and isinstance(v, ast.Dict):
                    for sub_k, sub_v in zip(v.keys, v.values):
                        if isinstance(sub_k, ast.Constant) and sub_k.value == "thread_id" and isinstance(sub_v, ast.Constant):
                            self.thread_id = str(sub_v.value)
                            
        self.generic_visit(node)

    def visit_Call(self, node: ast.Call):
        call_id = ""
        if isinstance(node.func, ast.Name):
            call_id = node.func.id
        elif isinstance(node.func, ast.Attribute):
            call_id = node.func.attr

        if call_id == "SqliteSaver":
            self.memory_backend = "sqlite"
        elif call_id == "MemorySaver":
            self.memory_backend = "in_memory"

        if isinstance(node.func, ast.Attribute):
            method_name = node.func.attr
            
            if method_name == "add_node" and len(node.args) >= 2:
                arg1, arg2 = node.args[0], node.args[1]
                node_id = self._resolve_node_name(arg1)
                func_pointer = self._resolve_node_name(arg2)
                
                self.nodes.append({
                    "id": node_id,
                    "executor_type": "opaque_blob",
                    "executor_reference": f"blobs/{node_id}.py",
                    "transitions": [],
                    "tools": [],
                    "interfaces": [],
                    "_associated_function": func_pointer
                })

            elif method_name == "add_edge" and len(node.args) >= 2:
                arg1, arg2 = node.args[0], node.args[1]
                val1 = self._resolve_node_name(arg1)
                val2 = self._resolve_node_name(arg2)
                
                if val1 == "START":
                    self.initial_node = val2
                else:
                    self.edges.append((val1, val2))
            
            elif method_name == "bind_tools" and len(node.args) >= 1:
                first_arg = node.args[0]
                if isinstance(first_arg, ast.List):
                    for elt in first_arg.elts:
                        self.globally_bound_tools.append(self._resolve_node_name(elt))
                        
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
        source_lines = self.source_code.split("\n")
        tree = ast.parse(self.source_code)
        
        visitor = LangGraphASTVisitor(source_lines)
        visitor.visit(tree)

        processed_nodes = []
        os.makedirs("blobs", exist_ok=True)

        for node_data in visitor.nodes:
            node_id = node_data["id"]
            func_name = node_data.pop("_associated_function", None)
            
            if func_name and func_name in visitor.function_bodies:
                blob_code = visitor.function_bodies[func_name]
                with open(f"blobs/{node_id}.py", "w", encoding="utf-8") as f:
                    f.write(blob_code)
            
            transitions = []
            for src, dest in visitor.edges:
                if src == node_id:
                    transitions.append({
                        "on_condition": f"GOTO_{dest.upper()}",
                        "target_node": dest
                    })
            
            node_data["transitions"] = transitions
            if visitor.globally_bound_tools:
                node_data["tools"] = list(set(visitor.globally_bound_tools))
                
            processed_nodes.append(WorkflowNode(**node_data))

        # Enforce relational consistency constraints across Pydantic initialization tracking thresholds
        initial_node = visitor.initial_node
        if processed_nodes:
            if not initial_node or not any(n.id == initial_node for n in processed_nodes):
                initial_node = processed_nodes[0].id
        else:
            # Inject structural safety placeholder node if the crawler scraped zero target functions
            processed_nodes.append(WorkflowNode(
                id="unknown_start",
                executor_type="opaque_blob",
                executor_reference="blobs/unknown_start.py",
                transitions=[],
                tools=[],
                interfaces=[]
            ))
            initial_node = "unknown_start"

        return UniversalAgentSpec(
            name=self.agent_name,
            runtime=RuntimeConfig(
                provider="langgraph_extracted",
                model="extracted_model",
                temperature=0.2
            ),
            memory=MemoryConfig(
                storage_backend=visitor.memory_backend,
                thread_id=visitor.thread_id,
                connection_string=visitor.connection_string
            ),
            interfaces=visitor.interfaces,
            system_prompt="Extracted automatically via SwarmHub static AST source-slicing.",
            topology=WorkflowTopology(
                type="StateMachine",
                initial_node=initial_node,
                nodes=processed_nodes
            )
        )