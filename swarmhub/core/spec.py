from typing import List, Dict, Literal, Optional, Union
from pydantic import BaseModel, Field, field_validator

class RuntimeConfig(BaseModel):
    provider: str = Field(..., description="e.g., anthropic, openai, ollama, custom_gemm")
    model: str = Field(..., description="Specific model identifier string")
    temperature: float = Field(0.2, ge=0.0, le=2.0)
    max_tokens: Optional[int] = None

class MemoryConfig(BaseModel):
    storage_backend: Literal["in_memory", "sqlite", "postgres", "json_file"] = Field(
        "in_memory", description="Persistence infrastructure type for check-pointing states across runs"
    )
    thread_id: Optional[str] = Field(
        None, description="Unique session boundary token identifier used to partition thread context logs"
    )
    connection_string: Optional[str] = Field(
        None, description="Target location URI configuration path or local file path handle (e.g., 'swarmhub_memory.db')"
    )

class InterfaceConfig(BaseModel):
    """
    Defines connection configurations for external capability layers.
    Supports local stdio sub-processes and remote SSE/HTTP server transports.
    """
    name: str = Field(..., description="Unique identifying handle for this interface server (e.g., 'local-filesystem')")
    protocol: Literal["mcp", "openapi", "custom"]
    transport: Literal["stdio", "sse", "http"] = "stdio"
    endpoint: str = Field(..., description="Command/executable name for stdio, or connection URL for sse/http")
    args: List[str] = Field(default_factory=list, description="Optional command-line arguments passed to stdio transport processes")
    metadata: Dict[str, str] = Field(default_factory=dict)

class TransitionRule(BaseModel):
    on_condition: str = Field(..., description="The output state, regex, or value that triggers this transition")
    target_node: str = Field(..., description="The ID of the next destination node")

class WorkflowNode(BaseModel):
    id: str = Field(..., description="Unique alphanumeric identifier for the execution node")
    executor_type: Literal["opaque_blob", "mcp_tool", "native_stub"]
    executor_reference: str = Field(..., description="Path to the python code blob or the tool name string")
    transitions: List[TransitionRule] = Field(default_factory=list)
    tools: List[str] = Field(default_factory=list, description="List of local functional tool strings assigned to this agent node")
    interfaces: List[str] = Field(
        default_factory=list, 
        description="List of global InterfaceConfig names this specific node is authorized to pull tools from"
    )

class WorkflowTopology(BaseModel):
    type: Literal["StateMachine", "DAG", "Sequential"] = "StateMachine"
    initial_node: str = Field(..., description="The node ID where the swarm starts execution")
    nodes: List[WorkflowNode]

class UniversalAgentSpec(BaseModel):
    version: str = "agentic.io/v1alpha1"
    kind: str = "UniversalAgent"
    name: str = Field(..., description="Unique slug name for this independent agent unit")
    runtime: RuntimeConfig
    memory: MemoryConfig = Field(
        default_factory=MemoryConfig, 
        description="The persistence execution settings managing transaction snapshots and message thread checkpoint chains"
    )
    system_prompt: str = Field(..., description="The foundational persona or anchoring context instructions")
    interfaces: List[InterfaceConfig] = Field(default_factory=list)
    state_schema: Dict[str, str] = Field(default_factory=dict, description="Explicit context state layout fields and primitive type signatures")
    topology: WorkflowTopology

    @field_validator("topology")
    @classmethod
    def validate_initial_node_exists(cls, v: WorkflowTopology) -> WorkflowTopology:
        node_ids = {node.id for node in v.nodes}
        if v.initial_node not in node_ids:
            raise ValueError(f"initial_node '{v.initial_node}' must exist within the defined workflow nodes.")
        return v