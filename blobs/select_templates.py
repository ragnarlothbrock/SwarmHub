def run(state):
    """
    Selects appropriate meme templates for each concept.

    Args:
        state (GraphState): Current state containing selected_concepts and available_templates

    Returns:
        GraphState: Updated state with selected_memes added

    Notes:
        - Creates simplified template descriptions for LLM
        - Matches concepts with appropriate templates
        - Falls back to random selection if no match found
        - Handles template selection for each concept
        - Creates structured meme objects with template info
    """

    concepts = state["selected_concepts"]
    templates = state["available_templates"]
    selected_memes = {}

    # Create simplified template descriptions for the LLM
    template_descriptions = [
        {
            'template_id': template_id,
            'name': template_data.name,
            'description': template_data.description,
            'lines': template_data.lines
        }
        for template_id, template_data in templates.items()
    ]

    for idx, concept in enumerate(concepts):
        prompt = f"""Select a meme template that best fits this concept:

        Concept:
        - Message: {concept['message']}
        - Emotion: {concept['emotion']}
        - Audience Relevance: {concept['audience_relevance']}

        Available Templates:
        {json.dumps(template_descriptions, indent=2)}

        Return only the template ID that best matches the concept's message and emotion."""

        try:
            response = llm.invoke([HumanMessage(content=prompt)])
            # Extract template ID from response, removing quotes and whitespace
            template_id = response.content.strip().strip('"').strip("'").lower()

            # Fallback to random template if not found
            if template_id not in templates:
                template_id = random.choice(list(templates.keys()))

            # Create meme object
            selected_memes[f"meme_{idx+1}"] = {
                "meme_id": f"meme_{idx+1}",
                "template_id": template_id,
                "concept": concept,
                "template_info": templates[template_id],
                "blank_template_api_link": templates[template_id].blank_template_api_link,
                "is_text_element1_filled": True,
                "is_text_element2_filled": templates[template_id].lines >= 2
            }

        except Exception as e:
            print(f"Error selecting template: {str(e)}")
            continue

    state["selected_memes"] = selected_memes
    return state