def run(state):
    """
    The function updates the state with the new business information from tool calls.
    """
    messages = state.get("messages", [])
    
    # Find the most recent tool message
    tool_messages = [msg for msg in messages if msg.type == "tool"]
    if tool_messages:
        latest_tool_message = tool_messages[-1]
        # Parse the JSON content from the tool message
        import json
        try:
            tool_content = json.loads(latest_tool_message.content)
            business_info = tool_content.get("business_information", {})
        except json.JSONDecodeError:
            business_info = state.get("business_information", {})
    else:
        business_info = state.get("business_information", {})

    return {
        "messages": messages,
        "business_information": business_info
    }