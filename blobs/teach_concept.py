def run(state):
    """Creates simplified Feynman-style explanations for concepts that need reinforcement."""
    structured_llm = llm.with_structured_output(FeynmanTeaching)
    current_checkpoint = state['current_checkpoint']
    checkpoint_info = state['checkpoints'].checkpoints[current_checkpoint]
    
    messages = [
        feynman_teacher,
        HumanMessage(content=f"""
        Criteria: {checkpoint_info.criteria}
        Verification: {state['verifications']}
        
        Context:
        {state['context_chunks']}
        
        Create a Feynman teaching explanation.""")
    ]
    
    teaching = structured_llm.invoke(messages)
    return {"teachings": teaching}