def run(state):
    """Generate a detailed description of the main character or scene."""
    query = state["query"]
    response = llm.invoke([HumanMessage(content=f"Based on the query '{query}', create a detailed description of the main character, object, or scene. Include specific details about appearance, characteristics, and any unique features. This description will be used to maintain consistency across multiple images.")])
    state["character_description"] = response.content
    return state