def run(state):
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    analyses = {}

    for competitor in state["competitors"]:
        response = llm.invoke([
            SystemMessage(content="Provide a concise competitive analysis in 100 words covering: main products, strengths (2), weaknesses (2), pricing model, target market."),
            HumanMessage(content=f"Analyze {competitor} vs {state['company']} in {state['industry']}:"),
        ])
        analyses[competitor] = response.content

    return {"competitor_analyses": analyses}