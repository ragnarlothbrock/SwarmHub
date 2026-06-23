def run(state):
    llm = ChatOpenAI(model="gpt-4o", temperature=0)

    analyses_text = "\n\n".join(
        f"**{name}:**\n{analysis}"
        for name, analysis in state["competitor_analyses"].items()
    )

    response = llm.invoke([
        SystemMessage(content="""You are a strategic consultant. Create a competitive analysis report with:
1. Executive Summary (3 sentences)
2. Competitive Landscape Table (company, strength, weakness, price)
3. Market Gaps & Opportunities (3 bullet points)
4. Strategic Recommendations for {company} (5 action items)
5. Threat Assessment (High/Medium/Low for each competitor)""".replace("{company}", state["company"])),
        HumanMessage(content=f"Company: {state['company']}\nIndustry: {state['industry']}\n\nCompetitor analyses:\n{analyses_text}"),
    ])

    return {"final_report": response.content, "messages": [response]}