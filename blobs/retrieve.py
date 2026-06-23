def run(state):
    """
    The function will first generate a detailed description of the business and then retrieve relevant documents.

    Args:
        state (dict): The current graph state

    Returns:
        state (dict): New key added to state, documents, that contains retrieved documents
    """
    print("---Rewrite Description---")
    nature_of_ops = state["business_information"]
    description = retriever_runnable.invoke({"business_information": nature_of_ops})
    print(f"Description:\n {description}")

    print("---RETRIEVE---")
    # Retrieval
    documents = retriever.invoke(description)
    print(f"Documents:\n {documents}")
    return {"description": description, "documents": documents}