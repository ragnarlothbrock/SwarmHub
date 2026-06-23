def run(state):
    """Classifies user input to determine if it requires database access."""
    
    # Define a system prompt for classifying input into predefined categories
    system_prompt = """You are an input classifier. Classify the user's input into one of these categories:
    - DATABASE_QUERY: Questions about data, requiring database access
    - GREETING: General greetings, how are you, etc.
    - CHITCHAT: General conversation not requiring database
    - FAREWELL: Goodbye messages

    Respond with ONLY the category name."""

    # Prepare messages for the LLM, including the system prompt and user's input
    messages = [
        ("system", system_prompt),  # Instructions for the LLM
        ("user", state['question'])  # User's question for classification
    ]

    # Invoke the LLM with a zero-temperature setting for deterministic output
    llm = ChatOpenAI(temperature=0)
    response = llm.invoke(messages)
    classification = response.content.strip()  # Extract the category from the response

    # Log the classification result
    logger.info(f"Input classified as: {classification}")

    # Update the conversation state with the input classification
    return {
        **state,
        "input_type": classification
    }