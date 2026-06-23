def run(state):
    """
    Part of the Conversation Sub-Graph.

    Generates and displays a character's introduction to Sherlock Holmes in the murder mystery game.

    Args:
        state (ConversationState): The LangGraph State object containing:
            - messages: List of previous conversation messages. Used to store conversation history
            - character: Character object with persona and character details
            - story_details: Object containing crime details including:
                - victim_name, time_of_death, location_found
                - murder_weapon, cause_of_death
                - crime_scene_details, initial_clues

    Returns:
        dict: Adds the introduction messages to the conversation history
            - messages: Introduction messages to be added

    Note:
        The function uses an LLM to generate appropriate character dialogue while ensuring
        the character doesn't reveal their role or incriminate themselves.
    """

    character = state['character']
    story = state['story_details']
    character_instructions = """You are playing the role of a character with the below persona:
{subject_persona}
You are being interviewed by Sherlock Holmes in relationship to the below crime:
Crime details:
- Victim: {victim}
- Time of death: {time}
- Location: {location}
Please greet and introduce your self to Sherlock Holmes.
Your tone should be conversational and should address Sherlock Holmes directly.
Make sure that you do not reveal your role and incriminate yourself.
"""
    system_message = character_instructions.format(
        subject_persona=character.persona,
        victim=story.victim_name,
        time=story.time_of_death,
        location=story.location_found,
    )
    # Generate narration
    narration = llm.invoke([
        SystemMessage(content=system_message),
        HumanMessage(content="Introduce yourself to Sherlock Holmes")
    ])

    print_introduction(character, narration)

    return {"messages": [narration]}