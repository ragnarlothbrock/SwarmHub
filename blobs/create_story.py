def run(state):
    """
    Part of the Game Loop Graph.

    Generates the complete murder mystery scenario and storyline based on the provided environment and the generated characters.

    Args:
        state (GenerateGameState): The LangGraph State object containing:
            - environment: Description of the game's setting
            - characters: List of character objects generated in create_character step

    Returns:
        dict: Contains the complete story details. Adds to the State Object.
            - story_details: StoryDetails object including:
                - Crime scene information
                - Evidence and clues
                - Character relationships
                - Environmental factors

    Note:
        - Creates a solvable mystery without revealing the killer
        - Includes both true clues and red herrings
        - Ensures consistency between characters and environment
    """

    environment = state['environment']
    characters = state['characters']

    # Format character list for the prompt
    character_list = "\n".join([char.persona for char in characters])

    # Enforce structured output
    structured_llm = llm.with_structured_output(StoryDetails)

    # System message
    system_message = story_instructions.replace("{{environment}}", environment)
    system_message = system_message.replace("{{characters}}", character_list)

    # Generate story details
    result = structured_llm.invoke([
        SystemMessage(content=system_message),
        HumanMessage(content="Generate the murder mystery scenario")
    ])

    # Return the story details
    return {"story_details": result}