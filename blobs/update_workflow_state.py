def run(state):
    """Reroute the workflow to the main assistant."""
    return {
        "workflow_state": "pop",
    }