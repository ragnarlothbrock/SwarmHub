def run(state):
    # Full set of sections
    sections = state["sections"]
    topic = state["topic"]

    # Concat all sections together
    formatted_str_sections = "\n\n".join([f"{section}" for section in sections])

    # Summarize the sections into a final report

    instructions = intro_instructions.format(topic=topic, formatted_str_sections=formatted_str_sections)
    intro = podcast_model.send_message(instructions)
    return {"introduction": intro.text}