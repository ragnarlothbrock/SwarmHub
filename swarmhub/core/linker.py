from copy import deepcopy
from typing import Dict, List, Any
from swarmhub.core.spec import UniversalAgentSpec, WorkflowNode, TransitionRule

class SwarmLinker:
    """
    Acts as the Link-Editor for AI Workforces. Combines, mutates, 
    and bridges disparate agentic topologies under a unified schema.
    """
    @staticmethod
    def combine(agent_a: UniversalAgentSpec, agent_b: UniversalAgentSpec, new_name: str) -> UniversalAgentSpec:
        """
        Stitches two independent agent specifications into a single workspace.
        By default, the entrance pointer targets agent_a's original entry node.
        """
        combined_spec = deepcopy(agent_a)
        combined_spec.name = new_name
        
        # Guard against node ID collisions across the imported boundaries
        agent_a_ids = {node.id for node in agent_a.topology.nodes}
        
        for node in agent_b.topology.nodes:
            if node.id in agent_a_ids:
                # Deduplicate conflicting IDs gracefully by suffixing source origin
                node.id = f"{agent_b.name}_{node.id}"
                for trans in node.transitions:
                    trans.target_node = f"{agent_b.name}_{trans.target_node}"
            combined_spec.topology.nodes.append(node)
            
        return combined_spec

    @staticmethod
    def inject_node_between(
        spec: UniversalAgentSpec, 
        source_node_id: str, 
        target_node_id: str, 
        new_node: WorkflowNode,
        adapter_condition: str = "PROCEED"
    ) -> UniversalAgentSpec:
        """
        Mutates the topology graph by intercepting an existing connection edge
        and cleanly splicing a new processing step right between them.
        """
        mutated_spec = deepcopy(spec)
        node_map = {node.id: node for node in mutated_spec.topology.nodes}
        
        if source_node_id not in node_map or target_node_id not in node_map:
            raise ValueError("Both explicit source and target nodes must exist to intercept an edge layout.")
            
        # 1. Append the new node to the workspace array
        mutated_spec.topology.nodes.append(new_node)
        
        # 2. Intercept the legacy transition rule from the source node
        source_node = node_map[source_node_id]
        edge_intercepted = False
        
        for transition in source_node.transitions:
            if transition.target_node == target_node_id:
                # Re-route the arrow to target our injected node instead
                transition.target_node = new_node.id
                edge_intercepted = True
                break
                
        if not edge_intercepted:
            # If no direct transition existed, create an explicit step attachment rule
            source_node.transitions.append(
                TransitionRule(on_condition=f"GOTO_{new_node.id.upper()}", target_node=new_node.id)
            )
            
        # 3. Force our new injected node to point down into the original destination target
        new_node.transitions.append(
            TransitionRule(on_condition=adapter_condition, target_node=target_node_id)
        )
        
        return mutated_spec