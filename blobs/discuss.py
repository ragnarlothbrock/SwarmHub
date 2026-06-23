def run(state):
    """
    Discuss the artwork with the user
    """
    while True:
        # Capture user message
        user_input = input("type `next` or `exit` or a comment to discuss\n")

        if user_input == 'next':
            state['art_request'] = input("Give a description of what'd you'd like to see next.")
            return {'art_request': state['art_request']}
        if user_input == 'exit':
            state['exit'] = True
            return state

        # Dicuss with the user
        summary = str(
            rag.query(
                f"""
                The user has said:
                {user_input}
                about the artwork:
                {state['artwork']}

                Respond with 1-2 sentences enriching the user with new facts or feedback.
                """,
                param=QueryParam(mode="hybrid"),
            )
        )
        state['header'].value = html_widget_value(f"{state['artwork']} Discussion")
        state['footer'].value = html_widget_value(
            f"{state['artwork_description']} \n## Tour Guide Response:\n {summary}"
        )