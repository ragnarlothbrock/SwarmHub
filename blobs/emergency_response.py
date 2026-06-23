def run(state):
    """Generate emergency response plan"""
    prompt = ChatPromptTemplate.from_template(
        "Create an emergency response plan for a {disaster_type} situation "
        "with {severity} severity level in {city}. Include immediate actions needed."
    )
    try:
        chain = prompt | llm
        response = chain.invoke({
            "disaster_type": state["disaster_type"],
            "severity": state["severity"],
            "city": state["city"]
        }).content

        return {
            **state,
            "response": response,
            "messages": state["messages"] + [SystemMessage(content="Emergency response plan generated")]
        }
    except Exception as e:
        return {
            **state,
            "response": "Failed to generate response plan",
            "messages": state["messages"] + [SystemMessage(content=f"Failed to generate emergency response: {str(e)}")]
        }