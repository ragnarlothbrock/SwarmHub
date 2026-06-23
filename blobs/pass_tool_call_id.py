def run(state):
    tool_call_id = state["messages"][-1].tool_calls[0]["id"]
    return {"tool_call_id": tool_call_id}