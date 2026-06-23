def run(state):
    """
    Creates final meme URLs using the Memegen.link API format.

    Args:
        state (GraphState): Current state containing pre_generated_memes

    Returns:
        GraphState: Updated state with generated_memes added

    Notes:
        - Processes text elements for URL compatibility
        - Handles URL encoding of text
        - Extracts and manages file extensions
        - Constructs final meme URLs
        - Maintains all meme metadata in state
    """

    pre_generated_memes = state["pre_generated_memes"]
    generated_memes = {}

    for meme_id, meme in pre_generated_memes.items():
        # Process text elements
        text1 = quote(meme["generated_text_element1"].replace(' ', '_'))
        text2 = quote(meme["generated_text_element2"].replace(' ', '_'))

        # Get template info
        template_info = meme["template_info"]
        base_url = template_info.blank_template_api_link

        # Extract extension
        extension = os.path.splitext(base_url)[1]
        base_url = base_url.rsplit('.', 1)[0]

        # Construct final URL
        final_url = f"{base_url}/{text1}/{text2}{extension}"

        generated_memes[meme_id] = {
            **meme,
            "final_url": final_url,
            "text_elements": [text1, text2]
        }

    state["generated_memes"] = generated_memes
    return state