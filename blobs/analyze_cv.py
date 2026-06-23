def run(state):
    # Implementation to analyze candidate CVs and send appropriate responses
    """Analyze CV and send appropriate response"""
    messages = [
        SystemMessage(content="""Analyze the CV against job requirements. Score from 0-10 on:
        1. Skills Match
        2. Experience Level
        3. Overall Fit

        Provide detailed feedback and clear recommendation."""),
        HumanMessage(content=f"""
        Job Requirements:
        {state.job_requirements.model_dump_json()}

        CV Content:
        {state.candidates[-1].cv_content}
        """)
    ]

    analysis = llm.invoke(messages)
    score = float(re.search(r"Overall Score:\s*(\d+\.?\d*)", analysis.content).group(1))

    tool_node = ToolNode([send_linkedin_message])

    if score >= 7.0:
        status = "approved"
        message = f"Congratulations! You've been selected for an interview on {state.job_requirements.interview_date}"
    else:
        status = "rejected"
        message = "Thank you for your application. Unfortunately..."

    # Send response via LinkedIn
    tool_node.invoke({
        "name": "send_linkedin_message",
        "args": {
            "profile_url": state.candidates[-1].linkedin_url,
            "message": message
        }
    })

    return {
        "cv_score": score,
        "status": status,
        "feedback": analysis.content,
        "phase": "prepare_interview" if status == "approved" else "complete"
    }