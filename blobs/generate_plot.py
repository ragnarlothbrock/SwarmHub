def run(state):
    """Generate a 5-step plot for the GIF animation."""
    query = state["query"]
    character_description = state["character_description"]
    response = llm.invoke([HumanMessage(content=f"Create a short, 5-step plot for a GIF based on this query: '{query}' and featuring this description: {character_description}. Each step should be a brief description of a single frame, maintaining consistency throughout. Keep it family-friendly and avoid any sensitive themes.")])
    state["plot"] = response.content
    return state