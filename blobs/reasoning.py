def run(state):
    """
    The function provides reasoning for the business categories based on the provided description and retrieved documents.

    Args:
        rag_state (RAGState): The current state containing the description and retrieved documents.

    Returns:
        RAGState: Updated state with reasoned categories of the business.
    """
    print("---REASONING---")
    description = rag_state["description"]
    documents = rag_state["documents"]

    # Reasoning
    rationale = reasoning_runnable.invoke({"description": description, "documents": documents})
    print(f"Rationale:\n {rationale}")
    return {"rationale": rationale}