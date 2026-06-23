def run(state):
    print("REVISE PAPER")
    critique = state["messages"][-1].content
    draft = state["draft"]

    messages = [SystemMessage(content=revise_draft_prompt)] + [critique] + draft
    response = model.invoke(messages, temperature=temperature)
    print(response)

    return {'draft' : [response]}