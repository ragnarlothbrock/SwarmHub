def run(state):
    print("DECISION-MAKER")
    review_plan = state['systematic_review_outline']
    relevant_messages = get_relevant_messages(state)
    messages = [SystemMessage(content=decision_prompt)] + review_plan + relevant_messages
    response = model.invoke(messages, temperature=temperature)
    print(response)
    print()
    return {"messages" : [response]}