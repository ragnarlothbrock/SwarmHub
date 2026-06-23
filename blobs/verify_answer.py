def run(state):
    """Evaluates user answers against checkpoint criteria using relevant context chunks."""
    structured_llm = llm.with_structured_output(LearningVerification)
    current_checkpoint = state['current_checkpoint']
    checkpoint_info = state['checkpoints'].checkpoints[current_checkpoint]
    
    context = context_store.get_context(state['context_key'])
    chunks = context['chunks']
    chunk_embeddings = context['embeddings']
    
    query = embeddings.embed_query(checkpoint_info.verification)
    
    similarities = cosine_similarity([query], chunk_embeddings)[0]
    top_3_indices = sorted(range(len(similarities)), 
                         key=lambda i: similarities[i], 
                         reverse=True)[:3]
    relevant_chunks = [chunks[i] for i in top_3_indices]
    
    messages = [
        answer_verifier,
        HumanMessage(content=f"""
        Question: {state['current_question']}
        Answer: {state['current_answer']}
        
        Checkpoint Description: {checkpoint_info.description}
        Success Criteria:
        {chr(10).join(f"- {c}" for c in checkpoint_info.criteria)}
        Verification Method: {checkpoint_info.verification}
        
        Context:
        {chr(10).join(relevant_chunks)}
        
        Assess the answer.""")
    ]
    
    verification = structured_llm.invoke(messages)
    return {"verifications": verification}