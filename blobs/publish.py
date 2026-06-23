def run(state):
    """
    Node for report generation
    
    Args:
        state (Dict[str, Any]): Current workflow state
        
    Returns:
        Dict[str, Any]: Updated state with final report
    """
    publisher = Publisher()
    report_content = publisher.create_report(state['summaries'])
    state['report'] = report_content
    return state