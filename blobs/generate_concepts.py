def run(state):
    """
    Generates meme concepts based on analyzed company insights.

    Args:
        state (GraphState): Current state containing company_context

    Returns:
        GraphState: Updated state with meme_concepts and selected_concepts added

    Notes:
        - Creates 3 meme concepts based on company insights
        - Each concept includes message, emotion, and audience relevance
        - Parses JSON response to extract structured concepts
        - Selects top 3 concepts for further processing
    """

    insights = state["company_context"]

    prompt = f"""Create 3 meme concepts based on these company insights:

    Tone: {insights.tone}
    Target Audience: {insights.target_audience}
    Value Proposition: {insights.value_proposition}
    Key Products: {', '.join(insights.key_products)}
    Brand Personality: {insights.brand_personality}

    For each meme concept, provide:
    1. The main message/joke
    2. The intended emotional response
    3. How it relates to the target audience

    Format the response as JSON array with structure:
    [{{"message": "string", "emotion": "string", "audience_relevance": "string"}}]"""

    response = llm.invoke([HumanMessage(content=prompt)])

    # Find JSON array in response using regex
    json_match = re.search(r'\[\s*{.*}\s*\]', response.content, re.DOTALL)
    if json_match:
        concepts_json = json_match.group(0)
        try:
            concepts = json.loads(concepts_json)
            state["meme_concepts"] = concepts
            state["selected_concepts"] = concepts[:3]  # Select top 3 concepts
            return state
        except json.JSONDecodeError:
            print("Failed to parse JSON response")

    return state