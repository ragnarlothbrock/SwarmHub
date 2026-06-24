import ast
import os
import json
from typing import Optional, Dict, Any, List
from swarmhub.core.spec import UniversalAgentSpec, WorkflowNode, WorkflowTopology, RuntimeConfig, MemoryConfig, InterfaceConfig

class PydanticAIASTVisitor(ast.NodeVisitor):
    """
    Deterministically crawls a Python Abstract Syntax Tree (AST) to extract
    PydanticAI primitives, including Agent instances, wrapped tool functions,
    and system prompt registration structures.
    """
    def __init__(self, source_lines: List[str]):
        self.source_lines = source_lines
        self.discovered_agents: List[Dict[str, Any]] = []
        self.function_bodies: Dict[str, str] = {}
        self.globally_bound_tools: List[str] = []
        self.extracted_system_prompts: List[str] = []

    def visit_FunctionDef(self, node: ast.FunctionDef):
        """Locates and slices custom run steps or tool logic bound via decorators."""
        start_line = node.lineno - 1
        end_line = node.end_lineno
        function_code_lines = self.source_lines[start_line:end_line]
        
        if function_code_lines:
            leading_spaces = len(function_code_lines[0]) - len(function_code_lines[0].lstrip())
            function_code_lines[0] = " " * leading_spaces + "def run(state):"
            
        self.function_bodies[node.name] = "\n".join(function_code_lines)

        # Inspect PydanticAI function decorators (@agent.tool, @agent.system_prompt)
        for decorator in node.decorator_list:
            if isinstance(decorator, ast.Attribute):
                attr_name = decorator.attr
                if attr_name in ("tool", "tool_plain"):
                    self.globally_bound_tools.append(node.name)
                elif attr_name == "system_prompt":
                    self.extracted_system_prompts.append(node.name)
                    
        self.generic_visit(node)

    def visit_Assign(self, node: ast.Assign):
        """Captures PydanticAI Agent instantiation expressions and model declarations."""
        if isinstance(node.value, ast.Call):
            call_name = ""
            if isinstance(node.value.func, ast.Name):
                call_name = node.value.func.id
            elif isinstance(node.value.func, ast.Attribute):
                call_name = node.value.func.attr

            if call_name == "Agent" and node.targets and isinstance(node.targets[0], ast.Name):
                agent_id = node.targets[0].id
                model_str = "pydanticai_default_model"
                
                # Extract targeted model identifier from structural positional or keyword arguments
                if node.value.args and isinstance(node.value.args[0], ast.Constant):
                    model_str = str(node.value.args[0].value)
                for kw in node.value.keywords:
                    if kw.arg == "model" and isinstance(kw.value, ast.Constant):
                        model_str = str(kw.value.value)

                self.discovered_agents.append({
                    "id": agent_id,
                    "model": model_str
                })
                
        self.generic_visit(node)


class PydanticAIParser:
    """
    Ingests raw PydanticAI source code text. Captures and processes the embedded 
    metadata source map block or slices raw functional agent execution nodes via AST.
    """
    def __init__(self, source_code: str, agent_name: str = "migrated-pydanticai-swarm"):
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
                runtime=RuntimeConfig(**spec_metadata.get("runtime", {"provider": "pydanticai_metadata", "model": "recovered"})),
                memory=MemoryConfig(**memory_data),
                interfaces=interfaces,
                system_prompt=spec_metadata.get("system_prompt", "Recovered losslessly via PydanticAI metadata loop pass."),
                topology=WorkflowTopology(
                    type=topology_data.get("type", "StateMachine"),
                    initial_node=topology_data.get("initial_node", "unknown"),
                    nodes=processed_nodes
                )
            )

        # Fallback AST Source-Slicing Logic Plane
        source_lines = self.source_code.split("\n")
        tree = ast.parse(self.source_code)
        visitor = PydanticAIASTVisitor(source_lines)
        visitor.visit(tree)

        if not visitor.discovered_agents:
            visitor.discovered_agents.append({
                "id": "default_pydanticai_node",
                "model": "gpt-4o-mini"
            })

        processed_nodes = []
        os.makedirs("blobs", exist_ok=True)
        
        extracted_model = visitor.discovered_agents[0]["model"]
        provider_name = "openai"
        if ":" in extracted_model:
            provider_name, extracted_model = extracted_model.split(":", 1)

        for i, agent_data in enumerate(visitor.discovered_agents):
            agent_id = agent_data["id"]
            transitions = []
            
            # Form a sequential translation map sequence if multiple agent blocks exist
            if i < len(visitor.discovered_agents) - 1:
                next_agent = visitor.discovered_agents[i + 1]["id"]
                transitions.append({
                    "on_condition": f"GOTO_{next_agent.upper()}",
                    "target_node": next_agent
                })

            if agent_id in visitor.function_bodies:
                blob_code = visitor.function_bodies[agent_id]
            else:
                blob_code = (
                    "def run(state):\n"
                    f"    print('    ⚡ PydanticAI extracted orchestration node running: {agent_id}')\n"
                    "    return state\n"
                )

            with open(f"blobs/{agent_id}.py", "w", encoding="utf-8") as f:
                f.write(blob_code)

            processed_nodes.append(WorkflowNode(
                id=agent_id,
                executor_type="opaque_blob",
                executor_reference=f"blobs/{agent_id}.py",
                transitions=transitions,
                tools=list(set(visitor.globally_bound_tools)),
                interfaces=[]
            ))

        return UniversalAgentSpec(
            name=self.agent_name,
            runtime=RuntimeConfig(provider=provider_name, model=extracted_model, temperature=0.1),
            memory=MemoryConfig(storage_backend="in_memory"),
            interfaces=[],
            system_prompt="Extracted from legacy PydanticAI codebase via AST structural slicing.",
            topology=WorkflowTopology(
                type="Sequential" if len(processed_nodes) > 1 else "StateMachine",
                initial_node=visitor.discovered_agents[0]["id"],
                nodes=processed_nodes
            )
        )