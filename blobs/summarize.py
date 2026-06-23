def run(state):
    """
    Node for article summarization
    
    Args:
        state (Dict[str, Any]): Current workflow state
        
    Returns:
        Dict[str, Any]: Updated state with summaries
    """
    summarizer = Summarizer()
    state['summaries'] = []
    
    for article in state['articles']: # Uses articles from previous node
        summary = summarizer.summarize(article)
        state['summaries'].append({
            'title': article.title,
            'summary': summary,
            'url': article.url
        })
    return state