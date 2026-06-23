def run(state):
    """Process general content (no specific processing, return as-is)."""
    state["processed_text"] = state["input_text"]
    return state