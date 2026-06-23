def run(state):
    """Generates search queries based on learning checkpoints from current state."""
    structured_llm = llm.with_structured_output(SearchQuery) 
    checkpoints_message = HumanMessage(content=format_checkpoints_as_message(state['checkpoints']))  
    messages = [checkpoint_based_query_generator, checkpoints_message]
    search_queries = structured_llm.invoke(messages)
    return {"search_queries": search_queries}