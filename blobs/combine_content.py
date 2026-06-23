def run(state):
    final_content = ""
    for content in state["contents"]:
        final_content += content + "\n\n"
    return {"generated_content": final_content}