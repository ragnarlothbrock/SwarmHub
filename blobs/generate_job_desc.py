def run(state):
    """
    Generate job description with human-in-the-loop review.

    Args:
        state: Current recruitment workflow state

    Returns:
        Dict with state updates

    Raises:
        NodeInterrupt: To get human review of generated description
    """
    if not state["job_requirements"]:
        raise ValueError("Job requirements missing")

    messages = [
        SystemMessage(content="""Create a professional and compelling job description with:
        1. About the Company
        2. Role Overview
        3. Key Responsibilities
        4. Required Qualifications
        5. What We Offer (Benefits)
        6. Location and Work Mode"""),
        HumanMessage(content=str(state["job_requirements"]))
    ]

    response = llm.invoke(messages)

    raise NodeInterrupt(
        f"Please review the generated job description:\n\n{response.content}"
    )