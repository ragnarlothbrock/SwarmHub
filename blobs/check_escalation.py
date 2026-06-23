def run(state):
    text = state["user_input"].lower()
    needs_escalation = any(kw in text for kw in ESCALATION_KEYWORDS)
    return {"escalate": needs_escalation}