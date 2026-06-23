def run(state):

    """ Node to answer a question """

    # Get state
    section = state["section"]
    topic = state["topic"]

    system_message = section_writer_instructions.format(focus=topic)
    section_res = podcast_model.send_message(system_message + f"Use this source to write your section: {section}")

    # Append it to state
    return {"sections": [section_res.text]}