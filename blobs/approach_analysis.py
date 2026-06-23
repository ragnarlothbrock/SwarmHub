def run(state):
    """Retrieve history approach and let LLM do a qualitative analysis on user approach preference."""
    history = ""
    for h in os.listdir(f"{os.getcwd()}/history"):
        if (h[-4:] == ".txt"):
            with open(os.path.join(os.getcwd(), f"history/{h}")) as f:
                content = f.readlines()
            history = f"{history}\n{content[0]}"

    approach['history'] = history

    prompt = ChatPromptTemplate.from_template(
        "Analyze the work style the following summary of work history portrays. "
        "Provide a brief summary the preference in work style."
        "\n\nWork History: {history}"
    )
    style = llm.invoke(prompt.format(history=approach['history']))
    approach['style'] = style
    return approach