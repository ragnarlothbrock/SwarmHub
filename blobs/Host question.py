def run(state):
    """ Node to generate a question """

    # Get state
    topic = state["topic"]
    messages = state["messages"]

    # Generate question
    system_message = question_instructions.format(topic=topic)
    question = podcast_gpt.invoke([SystemMessage(content=system_message)]+messages)

    # Write messages to state
    return {"messages": [question]}