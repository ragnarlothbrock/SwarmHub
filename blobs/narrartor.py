def run(state):
    """
    Part of the Game Loop Graph.

    Generates Dr. Watson's narration of the crime scene for Sherlock Holmes.

    Args:
        state (GenerateGameState): The LangGraph State object containing:
            - story_details: Complete information about the crime

    Returns:
        dict: Contains the narration message. Adds to the State Object.
            - messages: Dr. Watson's narrative description

    Note:
        - Provides a concise (100 words or less) introduction to the crime
        - Maintains Dr. Watson's characteristic narrative style
        - Sets the initial atmosphere for the investigation
    """
    story = state['story_details']

    # Format the message with the story details
    system_message = narrator_instructions.format(
        victim=story.victim_name,
        time=story.time_of_death,
        location=story.location_found,
        weapon=story.murder_weapon,
        cause=story.cause_of_death,
        scene=story.crime_scene_details
    )
    # Generate narration
    narration = llm.invoke([
        SystemMessage(content=system_message),
        HumanMessage(content="Create an atmospheric narration of the crime scene")
    ])

    print_game_header()
    print_narration(narration)

    return {"messages": [narration]}