def run(state):
    """
    Node for article search
    
    Args:
        state (Dict[str, Any]): Current workflow state
        
    Returns:
        Dict[str, Any]: Updated state with found articles
    """
    searcher = NewsSearcher()
    state['articles'] = searcher.search() 
    return state