def run(state):
    print("PLANNER")
    relevant_messages = get_relevant_messages(state)
    messages = [SystemMessage(content=planner_prompt)] + relevant_messages
    response = model.invoke(messages, temperature=temperature)
    print(response)
    print()
    return {"systematic_review_outline" : [response]}