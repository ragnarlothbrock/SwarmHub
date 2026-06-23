def run(state):
    """
    Generates meme text based on selected concepts and templates.

    Args:
        state (GraphState): Current state containing selected_memes and company_context

    Returns:
        GraphState: Updated state with pre_generated_memes added

    Notes:
        - Generates appropriate text for each template
        - Considers template format and number of lines
        - Maintains brand tone and target audience
        - Creates concise, punchy text elements
        - Handles errors gracefully for each meme
    """

    selected_memes = state["selected_memes"]
    context = state["company_context"]
    pre_generated_memes = {}

    for meme_id, meme in selected_memes.items():
        concept = meme["concept"]
        template_info = meme["template_info"]

        prompt = f"""Create text for a meme based on this template and concept:

        Template: {template_info.name}
        Number of lines: {template_info.lines}
        Example Text 1: {template_info.example_text_1}
        Example Text 2: {template_info.example_text_2}
        Concept Message: {concept['message']}
        Emotion: {concept['emotion']}

        Company Context:
        Target Audience: {context.target_audience}
        Brand Tone: {context.tone}

        Return ONLY the text lines, one per line. Keep each line concise and punchy.

        """

        try:
            response = llm.invoke([HumanMessage(content=prompt)])
            text_elements = response.content.strip().split('\n')

            generated_text1 = text_elements[0] if len(text_elements) > 0 else ""
            generated_text2 = text_elements[1] if len(text_elements) > 1 else ""

            pre_generated_memes[meme_id] = {
                **meme,
                "generated_text_element1": generated_text1,
                "generated_text_element2": generated_text2
            }

        except Exception as e:
            print(f"Error generating text: {str(e)}")
            continue

    state["pre_generated_memes"] = pre_generated_memes
    return state