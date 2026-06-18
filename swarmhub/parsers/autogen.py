import json
from typing import Optional, Dict, Any
from swarmhub.core.spec import UniversalAgentSpec, WorkflowNode, WorkflowTopology, RuntimeConfig

class AutoGenParser:
    """
    Ingests raw AutoGen source code text. Captures and processes the embedded 
    metadata source map block to ensure lossless transmission down the ring pipeline.
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
        metadata_topology = self._extract_metadata()
        
        if not metadata_topology:
            raise ValueError("❌ AutoGen parsing requires a valid SwarmHub Metadata Source Map to extract non-linear layouts.")
            
        processed_nodes = [WorkflowNode(**n) for n in metadata_topology.get("nodes", [])]
        
        return UniversalAgentSpec(
            name=self.agent_name,
            runtime=RuntimeConfig(provider="recovered_ring_relay", model="recovered_ring_relay"),
            system_prompt="Recovered losslessly via AutoGen metadata ring pass.",
            topology=WorkflowTopology(
                type=metadata_topology.get("type", "StateMachine"),
                initial_node=metadata_topology.get("initial_node", "unknown"),
                nodes=processed_nodes
            )
        )