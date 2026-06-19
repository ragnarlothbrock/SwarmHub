from copy import deepcopy
from typing import Dict, List, Any
from swarmhub.core.spec import UniversalAgentSpec, WorkflowNode, TransitionRule

class SwarmLinker:
    """
    Acts as the Link-Editor for AI Workforces. Combines, mutates, 
    and bridges disparate agentic topologies, memory setups, and MCP tool servers.
    """
    @staticmethod
    def combine(agent_a: UniversalAgentSpec, agent_b: UniversalAgentSpec, new_name: str) -> UniversalAgentSpec:
        """
        Stitches two independent agent specifications into a single workspace registry.
        Gracefully merges distinct MCP tool interfaces, resolves name collisions,
        and rewrites least-privilege node authorization tokens dynamically.
        """
        combined_spec = deepcopy(agent_a)
        combined_spec.name = new_name
        
        # 1. Merge and deduplicate global MCP tool interfaces
        existing_interface_names = {iface.name for iface in combined_spec.interfaces}
        interface_name_mapping = {}  # Tracks name shifts: {old_b_name: new_combined_name}
        
        for iface in agent_b.interfaces:
            if iface.name in existing_interface_names:
                new_iface_name = f"{agent_b.name}_{iface.name}".replace("-", "_")
                interface_name_mapping[iface.name] = new_iface_name
                
                cloned_iface = deepcopy(iface)
                cloned_iface.name = new_iface_name
                combined_spec.interfaces.append(cloned_iface)
            else:
                interface_name_mapping[iface.name] = iface.name
                combined_spec.interfaces.append(deepcopy(iface))
        
        # 2. Guard against node ID collisions across the imported boundaries
        agent_a_ids = {node.id for node in agent_a.topology.nodes}
        
        for node in agent_b.topology.nodes:
            if node.id in agent_a_ids:
                # Deduplicate conflicting IDs gracefully by suffixing source origin and normalizing string formats
                node.id = f"{agent_b.name}_{node.id}".replace("-", "_")
                for trans in node.transitions:
                    trans.target_node = f"{agent_b.name}_{trans.target_node}".replace("-", "_")
            
            # 3. Dynamic Permission Remapping Pass
            updated_node_interfaces = []
            for iface_ref in node.interfaces:
                if iface_ref in interface_name_mapping:
                    updated_node_interfaces.append(interface_name_mapping[iface_ref])
                else:
                    updated_node_interfaces.append(iface_ref)
            node.interfaces = updated_node_interfaces
            
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
            
        mutated_spec.topology.nodes.append(new_node)
        source_node = node_map[source_node_id]
        edge_intercepted = False
        
        for transition in source_node.transitions:
            if transition.target_node == target_node_id:
                transition.target_node = new_node.id
                edge_intercepted = True
                break
                
        if not edge_intercepted:
            source_node.transitions.append(
                TransitionRule(on_condition=f"GOTO_{new_node.id.upper()}", target_node=new_node.id)
            )
            
        new_node.transitions.append(
            TransitionRule(on_condition=adapter_condition, target_node=target_node_id)
        )
        
        return mutated_spec