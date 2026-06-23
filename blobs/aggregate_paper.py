def run(state):
    print("AGGREGATE")
    abstract = state['abstract'][-1].content
    introduction = state['introduction'][-1].content
    methods = state['methods'][-1].content
    results = state['results'][-1].content
    conclusion = state['conclusion'][-1].content
    references = state['references'][-1].content

    messages = [
            SystemMessage(content="Make a title for this systematic review based on the abstract. Write it in markdown."),
            HumanMessage(content=abstract)
        ]
    title = model.invoke(messages, temperature=0.1).content

    draft = title + "\n\n" + abstract + "\n\n" + introduction + "\n\n" + methods + "\n\n" + results + "\n\n" + conclusion + "\n\n" + references

    return {"draft" : [draft]}