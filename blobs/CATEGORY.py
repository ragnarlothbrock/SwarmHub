def run(state):
    """
    This node handles the categorization of the user input to identify the intended actions.
    """
    query = state["current_query"]
    actions = get_user_actions(query)
    return {"actions": actions}