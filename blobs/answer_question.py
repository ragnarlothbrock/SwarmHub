def run(state):
    """
    Part of the Conversation Sub-Graph.

    Generates a character's response to a question during the investigation.

    Args:
        state (ConversationState): The LangGraph State object containing:
            - messages: List of previous conversation messages. Used to store conversation history
            - character: Character object with persona and character details specifc to the character answering the question
            - story_details: Object containing crime details including:
                - victim_name, time_of_death, location_found
                - murder_weapon, cause_of_death
                - crime_scene_details, initial_clues

    Returns:
        dict: Adds response from the character to the conversation history
            - messages : Response to be added

    Note:
        The character's response:
        - Maintains consistency with their persona and knowledge
        - Considers their relationships with other characters
        - May include deception based on character motivations
        - Takes into account all previous conversation context
    """
    messages = state['messages']
    character = state['character']
    last_message = messages[-1]
    story = state['story_details']
    answer_instructions = """
You are playing the role of a character with the below persona:
{subject_persona}
You are being interviewed by Sherlock Holmes in relationship to the below crime:
Crime Scene Details:
    Victim: {victim}
    Time: {time}
    Location: {location}
    Weapon: {weapon}
    Cause of Death: {cause}

    Scene Description:
    {scene}

    All Characters and their relationships:
    {npc_brief}
Based on the message history, answer the question as the character would, based on:
1. Your character's personality and background
2. Your knowledge of the crime
3. Your relationships with other characters
4. Your potential motives or alibis


Important:
- Stay in character
- Only reveal information this character would know
- Maintain consistency with the story details
- You can lie if your character would have a reason to do so

Question to answer:
{question}
"""
    system_message = answer_instructions.format(
        subject_persona=character.persona,
        victim=story.victim_name,
        time=story.time_of_death,
        location=story.location_found,
        weapon=story.murder_weapon,
        cause=story.cause_of_death,
        scene=story.crime_scene_details,
        npc_brief=story.npc_brief,
        question=last_message.content
    )

    prompt = ChatPromptTemplate.from_messages(
          [
              (
                  "system",
                  system_message,
              ),
              MessagesPlaceholder(variable_name="messages"),
          ]
      )
    chain = prompt | llm
    answer = chain.invoke(messages)

    print_character_answer(character, answer.content)

    return {"messages":[answer]}