def run(state):
    """Generate specific image prompts for each frame of the GIF."""
    plot = state["plot"]
    character_description = state["character_description"]
    response = llm.invoke([HumanMessage(content=f"""Based on this plot: '{plot}' and featuring this description: {character_description}, generate 5 specific, family-friendly image prompts, one for each step. Each prompt should be detailed enough for image generation, maintaining consistency, and suitable for DALL-E. 

Always include the following in EVERY prompt to maintain consistency:
1. A brief reminder of the main character or object's key features
2. The specific action or scene described in the plot step
3. Any relevant background or environmental details

Format each prompt as a numbered list item, like this:
1. [Your prompt here]
2. [Your prompt here]
... and so on.""")])
    
    prompts = []
    for line in response.content.split('\n'):
        if line.strip().startswith(('1.', '2.', '3.', '4.', '5.')):
            prompt = line.split('.', 1)[1].strip()
            prompts.append(f"Create a detailed, photorealistic image of the following scene: {prompt}")
    
    if len(prompts) != 5:
        raise ValueError(f"Expected 5 prompts, but got {len(prompts)}. Please try again.")
    
    state["image_prompts"] = prompts
    return state