def run(state):
    """
    Part of the Game Loop Graph.

    Manages the main conversation loop between Sherlock/player and characters.

    Args:
        state (GenerateGameState): The LangGraph State object containing:
            - selected_character_id: ID of the character to converse with
            - characters: List of all character objects
            - story_details: Complete story information

    Returns:
        dict: Contains either:
            - messages: List of conversation messages if character selected
            - END constant if no character selected (moving to guessing phase)

    Note:
        - Implements recursion limit to prevent infinite loops
        - Handles conversation flow and state management
        - Integrates with the conversation subgraph
    """
    selected_character_id = state['selected_character_id']
    if selected_character_id is not None:
        characters = state['characters']
        character = characters[selected_character_id]
        inputs = {
            "character": character,
            "story_details": state['story_details'],
        }
        response = conversation_graph.invoke(inputs,{"recursion_limit": 50})

        # Return the response as a message
        return {"messages": [response['messages']]}
    else:
        return END