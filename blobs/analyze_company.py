def run(state):
    """
    Analyzes company information from website content using LLM.

    Args:
        state (GraphState): Current state containing website_content

    Returns:
        GraphState: Updated state with company_context added

    Notes:
        - Uses structured LLM output for consistent format
        - Analyzes tone, target audience, value proposition, key products, and brand personality
        - Handles cases where no content is available
    """

    # Extract search results from state
    website_data = state.get("website_content")
    if not website_data:
        state["company_context"] = {"error": "No content available to analyze."}
        return state

    content = website_data[0]

    prompt = f"""Analyze this company website content and provide insights in a JSON format with the following structure:
    {{
        "tone": "string describing the brand tone of voice (professional, casual, technical, etc.)",
        "target_audience": "string describing target audience/persona",
        "value_proposition": "string describing their unique value proposition",
        "key_products": ["array", "of", "key", "products", "or", "services"],
        "brand_personality": "string describing 3-5 key brand personality traits"
    }}

    Website Content:
    {website_data}

    Please ensure key_products is always returned as an array/list, even if there's only one product.
    Be specific and base insights on the actual content."""

    structured_llm = llm.with_structured_output(CompanyContext)

    response = structured_llm.invoke([HumanMessage(content=prompt)])
    state["company_context"] = response

    return state