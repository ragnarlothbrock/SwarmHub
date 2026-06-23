def run(state):
    print("ANALYZE PAPERS")
    analyses=""
    for paper in state['papers'][-1].content:
        md_text = pymupdf4llm.to_markdown(f"./{paper['paper']}")
        messages = [
            SystemMessage(content=analyze_paper_prompt),
            HumanMessage(content=md_text)
        ]

        model = ChatOpenAI(model='gpt-4o')
        response = model.invoke(messages, temperature=0.1)
        print(response)
        analyses+=response.content
    return {
        "analyses": [analyses]
    }