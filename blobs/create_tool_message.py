def run(state):
    tool_call_id = extra_state["tool_call_id"]
    final_classifications = extra_state["final_classifications"]
    return {
            "messages": [
                ToolMessage(
                    content=""f"Assume the role of the Main Underwriting Assistant and reflect on the previous conversation between the host assistant and the user."
                    f" Based on the initial underwriting analysis, the following categories have been identified as most relevant to the business:"
                    f"{final_classifications}"
                    "Grades have been assigned based on the accuracy of the descriptions and the rationale provided for each category. KEEP THE GRADES PRIVATE AND DO NOT SHARE THEM WITH THE USER."
                    "To confirm their relevance to the business, please ask the user follow-up questions to finalize the validity of these categories.""",
                    tool_call_id=tool_call_id,
                )
            ],
            "workflow_state": "underwriting_assistant"
        }