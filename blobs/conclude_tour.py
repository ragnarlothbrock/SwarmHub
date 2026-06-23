def run(state):
    summary = str(
        rag.query(
            f"""
            Build a narrative and summarize the themes of an art tour you just gave with these artworks
            {[state['artwork_metadata']] + state['past_artworks']}
            Start by writing a short introduction.
            Write no more than 2 sentences about any particular artwork.
            End by writing a short conclusion.
            Thank the user for their engagement.
            """,
            param=QueryParam(mode="hybrid"),
        )
    )

    tour_conclusion = f"""
    Thank you for doing a tour!
    These are the artworks you viewed:
    {", ".join(state['past_artworks'])}

    Here's a summary of the themes:
    {summary}
    """
    state['header'].value = html_widget_value("Art Tour Completed")
    state['image'].value = html_widget_value(summary)
    state['footer'].value = html_widget_value("Thank you")
    return {'app_message': tour_conclusion}