from typing import List, Dict, Optional, Literal
from swarmhub.core.spec import (
    UniversalAgentSpec, 
    WorkflowNode, 
    WorkflowTopology, 
    RuntimeConfig, 
    MemoryConfig, 
    InterfaceConfig, 
    TransitionRule
)

class SwarmWorkflow:
    """
    The main developer-facing Programmatic SDK for SwarmHub.
    Allows developers to build, route, and compile multi-agent swarms 
    using a clean, framework-agnostic Fluent API with integrated memory and MCP tools.
    """
    def __init__(self, name: str):
        self.name = name
        self.provider = "openai"
        self.model = "gpt-4o"
        self.temperature = 0.2
        self.system_prompt = "You are a professional autonomous agent instance engineered via SwarmHub SDK."
        
        # Core Feature Configurations Arrays
        self.memory_config = MemoryConfig(storage_backend="in_memory")
        self.interfaces: List[InterfaceConfig] = []
        
        self.nodes: List[WorkflowNode] = []
        self.initial_node: Optional[str] = None
        self.state_schema: Dict[str, str] = {} 

    def configure_runtime(self, provider: str, model: str, temperature: float = 0.2) -> 'SwarmWorkflow':
        """Sets the cognitive engine targets for the workforce configuration."""
        self.provider = provider
        self.model = model
        self.temperature = temperature
        return self

    def configure_memory(self, backend: str = "sqlite", thread_id: Optional[str] = None, connection_string: Optional[str] = None) -> 'SwarmWorkflow':
        """Configures the state checkpointing parameters and thread session targets for the running swarm."""
        if backend == "sqlite" and not connection_string:
            connection_string = "swarmhub_memory.db"
            
        self.memory_config = MemoryConfig(
            storage_backend=backend,
            thread_id=thread_id,
            connection_string=connection_string
        )
        return self

    def register_mcp_server(
        self, 
        name: str, 
        transport: Literal["stdio", "sse", "http"] = "stdio", 
        endpoint: str = "", 
        args: Optional[List[str]] = None
    ) -> 'SwarmWorkflow':
        """
        Fluent API Extension: Registers an external Model Context Protocol capability server 
        into the global infrastructure layer of the agent swarm.
        
        :param name: Unique identifying handle for this interface server (e.g., 'filesystem-service')
        :param transport: The transmission channel protocol style ('stdio' for subprocesses, 'sse'/'http' for remote APIs)
        :param endpoint: The execution shell command string (for stdio) or the remote target base URL (for sse/http)
        :param args: Optional array list of command-line initialization parameters passed to stdio transport processes
        """
        new_interface = InterfaceConfig(
            name=name,
            protocol="mcp",
            transport=transport,
            endpoint=endpoint,
            args=args or []
        )
        self.interfaces.append(new_interface)
        return self

    def set_global_prompt(self, prompt: str) -> 'SwarmWorkflow':
        """Sets the overarching system guardrails instruction text."""
        self.system_prompt = prompt
        return self

    def set_state_schema(self, schema: Dict[str, str]) -> 'SwarmWorkflow':
        """Defines the strict type-safe contract data schema fields for the global context."""
        self.state_schema = schema
        return self

    def add_step(
        self, 
        node_id: str, 
        executor_reference: str, 
        is_entry_point: bool = False, 
        tools: Optional[List[str]] = None,
        interfaces: Optional[List[str]] = None
    ) -> 'SwarmWorkflow':
        """
        Registers a new independent execution step optionally linked to a set of local tools 
        and global MCP capabilities interfaces.
        """
        new_node = WorkflowNode(
            id=node_id,
            executor_type="opaque_blob",
            executor_reference=executor_reference,
            transitions=[],
            tools=tools or [] if tools else [],
            interfaces=interfaces or [] if interfaces else []
        )
        self.nodes.append(new_node)
        
        if is_entry_point or self.initial_node is None:
            self.initial_node = node_id
            
        return self

    def bind_tool(self, node_id: str, tool_name: str) -> 'SwarmWorkflow':
        """Binds an LLM functional tool dependency directly to a specific workflow execution step."""
        node_map = {n.id: n for n in self.nodes}
        if node_id not in node_map:
            raise ValueError(f"❌ Cannot bind tool to '{node_id}': Node does not exist in workspace layout.")
        
        if tool_name not in node_map[node_id].tools:
            node_map[node_id].tools.append(tool_name)
        return self

    def add_route(self, from_node: str, to_node: str, condition_trigger: str = "PROCEED") -> 'SwarmWorkflow':
        """Drives a directional execution link path channel between two functional steps."""
        node_map = {n.id: n for n in self.nodes}
        if from_node not in node_map:
            raise ValueError(f"❌ Cannot route away from '{from_node}': Node does not exist in workspace layout.")
            
        rule = TransitionRule(on_condition=f"GOTO_{condition_trigger.upper()}", target_node=to_node)
        node_map[from_node].transitions.append(rule)
        return self

    def build_spec(self) -> UniversalAgentSpec:
        """Assembles the current code layout structures into our validated universal contract spec."""
        if not self.nodes:
            raise ValueError("❌ Cannot compile empty swarm layout workspace.")
            
        return UniversalAgentSpec(
            name=self.name,
            runtime=RuntimeConfig(
                provider=self.provider,
                model=self.model,
                temperature=self.temperature
            ),
            memory=self.memory_config,
            interfaces=self.interfaces, # Inject the registered capability servers
            system_prompt=self.system_prompt,
            state_schema=self.state_schema, 
            topology=WorkflowTopology(
                type="StateMachine",
                initial_node=self.initial_node or self.nodes[0].id,
                nodes=self.nodes
            )
        )