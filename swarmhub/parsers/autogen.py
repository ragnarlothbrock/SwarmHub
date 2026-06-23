import ast
import os
import json
from typing import Optional, Dict, Any, List
from swarmhub.core.spec import UniversalAgentSpec, WorkflowNode, WorkflowTopology, RuntimeConfig, MemoryConfig, InterfaceConfig

class AutoGenASTVisitor(ast.NodeVisitor):
    """
    Crawls raw AutoGen source blocks to slice out message-routing functions,
    tools configurations, or custom agent registrations. Supports v0.2 and v0.4+ monorepos.
    """
    def __init__(self, source_lines: List[str]):
        self.source_lines = source_lines
        self.function_bodies: Dict[str, str] = {}
        self.discovered_agents: List[str] = []

    def visit_FunctionDef(self, node: ast.FunctionDef):
        """Extracts any conversational response logic or capability registration rules."""
        start_line = node.lineno - 1
        end_line = node.end_lineno
        function_code_lines = self.source_lines[start_line:end_line]
        
        if function_code_lines:
            leading_spaces = len(function_code_lines[0]) - len(function_code_lines[0].lstrip())
            function_code_lines[0] = " " * leading_spaces + "def run(state):"
            
        self.function_bodies[node.name] = "\n".join(function_code_lines)
        self.generic_visit(node)

    def visit_ClassDef(self, node: ast.ClassDef):
        """Identifies custom object factories inheriting from core framework agent base classes."""
        is_agent_subclass = False
        for base in node.bases:
            if isinstance(base, ast.Name) and "Agent" in base.id:
                is_agent_subclass = True
            elif isinstance(base, ast.Attribute) and "Agent" in base.attr:
                is_agent_subclass = True
                
        if is_agent_subclass:
            self.discovered_agents.append(node.name)
        self.generic_visit(node)

    def visit_Call(self, node: ast.Call):
        """Audits calls and captures target names for legacy or next-gen core agent instantiations."""
        if isinstance(node.func, (ast.Name, ast.Attribute)):
            call_name = node.func.id if isinstance(node.func, ast.Name) else node.func.attr
            
            # Catches ConversableAgent, AssistantAgent, RoutedAgent, and next-gen BaseAgent definitions
            if "Agent" in call_name and call_name != "Agent":
                for keyword in node.keywords:
                    if keyword.arg == "name" and isinstance(keyword.value, ast.Constant):
                        self.discovered_agents.append(str(keyword.value.value))
                        
        self.generic_visit(node)


class AutoGenParser:
    """
    Ingests raw AutoGen source code text. Captures and processes the embedded 
    metadata source map block or slices raw conversational function steps and capabilities.
    """
    def __init__(self, source_code: str, agent_name: str = "migrated-autogen-swarm"):
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
                runtime=RuntimeConfig(**spec_metadata.get("runtime", {"provider": "recovered_ring_relay", "model": "recovered_ring_relay"})),
                memory=MemoryConfig(**memory_data),
                interfaces=interfaces,
                system_prompt=spec_metadata.get("system_prompt", "Recovered losslessly via AutoGen metadata ring pass."),
                topology=WorkflowTopology(
                    type=topology_data.get("type", "StateMachine"),
                    initial_node=topology_data.get("initial_node", "unknown"),
                    nodes=processed_nodes
                )
            )
            
        # Fallback Source-Slicing Logic Pass
        source_lines = self.source_code.split("\n")
        tree = ast.parse(self.source_code)
        visitor = AutoGenASTVisitor(source_lines)
        visitor.visit(tree)
        
        # Resilient fall-through: Auto-inject a baseline tracking node if 0 explicit initializations are logged
        if not visitor.discovered_agents:
            visitor.discovered_agents.append("default_autogen_agent")
            
        processed_nodes = []
        os.makedirs("blobs", exist_ok=True)
        
        for i, agent_id in enumerate(visitor.discovered_agents):
            transitions = []
            if i < len(visitor.discovered_agents) - 1:
                next_agent = visitor.discovered_agents[i + 1]
                transitions.append({"on_condition": f"GOTO_{next_agent.upper()}", "target_node": next_agent})
                
            if agent_id in visitor.function_bodies:
                blob_code = visitor.function_bodies[agent_id]
            else:
                blob_code = (
                    "def run(state):\n"
                    f"    print('    💬 Conversable agent runtime node executing: {agent_id}')\n"
                    "    return state\n"
                    )
                
            with open(f"blobs/{agent_id}.py", "w", encoding="utf-8") as f:
                f.write(blob_code)
                
            processed_nodes.append(WorkflowNode(
                id=agent_id,
                executor_type="opaque_blob",
                executor_reference=f"blobs/{agent_id}.py",
                transitions=transitions,
                tools=[],
                interfaces=[]
            ))
            
        return UniversalAgentSpec(
            name=self.agent_name,
            runtime=RuntimeConfig(provider="autogen_sliced_fallback", model="fallback_model"),
            memory=MemoryConfig(storage_backend="in_memory"),
            interfaces=[],
            system_prompt="Extracted from legacy conversational script via AST source-slicing.",
            topology=WorkflowTopology(
                type="StateMachine",
                initial_node=visitor.discovered_agents[0],
                nodes=processed_nodes
            )
        )