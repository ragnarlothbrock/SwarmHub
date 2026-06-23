def run(state):
    """
    Part of the Game Loop Graph.

    Creates a cast of characters for the murder mystery game based on the environment and the max_characters.

    Args:
        state (GenerateGameState): The LangGraph State object containing:
            - environment: Description of the game's setting
            - max_characters: Maximum number of characters to create

    Returns:
        dict : Contains the generated character list. Adds to the State object.
            - characters : List of NPC objects with defined roles, including:
                - One killer
                - One victim
                - Supporting characters

    Note:
        - Uses structured LLM output to ensure consistent character creation
        - Each character has a name, role, and detailed persona
        - Ensures character diversity and setting appropriateness
    """

    environment = state['environment']
    max_characters = state['max_characters']

    # Enforce structured output
    structured_llm = llm.with_structured_output(NPC)

    # System message
    system_message = character_instructions.replace("{{environment}}", environment)
    system_message = system_message.replace("{{max_characters}}", str(max_characters))

    # Generate characters
    result = structured_llm.invoke([
        SystemMessage(content=system_message),
        HumanMessage(content="Generate the set of characters")
    ])

    # Return the characters from the NPC object
    return {"characters": result.characters}