def run(state):
    """Ask user initial questions to define their needs for the car."""
    messages = state.get("messages", [])    
    if len(messages) == 0:
        system_message = "You are a car buying assistant. Your goal is to help the user find a car that meets their needs. Start by introducing yourself and asking about their requirements, such as intended usage (e.g., commuting, family trips), budget, size preferences, and any specific constraints or features they value. Use their responses to guide them toward the best options."
    else:
        system_message = "Ask the user for any additional information that can help narrow down the search. If he asked any questions before, answer them before asking for more information. When answering, make sure to provide clear and concise information, with relevant examples."
        
    existing_needs = state.get("user_needs", "")
    if existing_needs:
        system_message += f" Here's what we know about the needs of the user so far:\n\n{existing_needs}"

    messages.append(SystemMessage(content=system_message))

    # Get message from the LLM
    response = GPT.invoke(messages).content
    messages += [AIMessage(response)]
    show_assistant_output(f"\033[92m{messages[-1].content}\033[0m", flush=True)
    
    messages += [HumanMessage(get_user_input(response))]
    print(f"\033[94m{messages[-1].content}\033[0m", flush=True)
    
    summarization_messages = messages.copy()
    
    summarization_messages += [
        SystemMessage(
            "Summarize the user's car-buying needs in clear and concise bullet points based on their input and any prior knowledge.\n"
            "Provide the next step, such as asking for more details or answer questions under ask_user_needs or going forward to build_filter:\n"
            "- Use 'ask_user_needs' if you need more information or if the user asked a question.\n"
            "- Use 'build_filters' if you have enough details to search for cars online.\n"
            "If the user's query is irrelevant to the matter at hand (buying a car), respond 'irrelevant'."
        )
    ]
    
    response = json.loads(USER_NEEDS_GPT.invoke(summarization_messages).content)

    state["user_needs"] = response["user_needs"]
    
    messages += [AIMessage("I have summarized your car-buying needs as follows:\n" + state["user_needs"])]
    
    show_assistant_output(f"\033[92m{messages[-1].content}\033[0m")
    
    state["next_node"] = response["next_step"]
        
    print(f"\nNext node: {state['next_node']}", flush=True)

    return state