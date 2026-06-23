def run(state):
    print("CRITIQUE")
    draft = state["draft"]
    review_plan = state['systematic_review_outline']

    messages = [SystemMessage(content=critique_draft_prompt)] + review_plan + draft
    response = model.invoke(messages, temperature=temperature)
    print(response)

    # every critique is a call for revision
    return {'messages' : [response], "revision_num": state.get("revision_num", 1) + 1}