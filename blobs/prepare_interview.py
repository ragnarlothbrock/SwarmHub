def run(state):
    """Generate interview questions with human approval"""
    messages = [
        SystemMessage(content="""Generate 10 interview questions covering:
        - Technical Skills (4)
        - Experience (3)
        - Problem Solving (3)"""),
        HumanMessage(content=f"""
        Position: {state.job_requirements.title}
        Required Skills: {', '.join(state.job_requirements.skills_required)}
        """)
    ]

    response = llm.invoke(messages)

    # Raise NodeInterrupt for human review
    raise NodeInterrupt(
        f"Please review the interview questions:\n\n{response.content}"
    )