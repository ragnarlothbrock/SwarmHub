def run(state):
    print("WRITE REFERENCES")
    review_plan = state['systematic_review_outline']
    analyses = state['analyses']
    messages = [SystemMessage(content=references_prompt)] + review_plan + analyses
    model = ChatOpenAI(model='gpt-4o-mini')
    response = _make_api_call(model, messages)
    print(response)
    print()
    return {"references" : [response]}