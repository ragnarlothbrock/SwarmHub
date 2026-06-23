def run(state):
    # Check if the database graph is already present in the state
    if state.get('db_graph') is None:
        logger.info("Performing one-time database schema discovery...")
        
        # Use the DiscoveryAgent to generate the database graph
        discovery_agent = DiscoveryAgent()
        graph = discovery_agent.discover()
        
        logger.info("Database schema discovery complete - this will be reused for future queries")
        
        # Update the state with the discovered database graph
        return {**state, "db_graph": graph}
    
    # Return the existing state if the database graph already exists
    return state