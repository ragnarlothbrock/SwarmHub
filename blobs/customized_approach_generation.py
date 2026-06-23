def run(state):
    prompt = ChatPromptTemplate.from_template(
        "Give me a plan of steps to carry out the following task with custom work styles specified."
        "You have to pay extra attention to Work Style mentioned below and adjust the plan accordingly."
        "\n\nTask: {task}\n\nDetails: {details}\n\nWork Style: {style}\n\n"
        "The output must be a numbered list of steps with explanation of why it is needed, what to do and how it considers the Work Style."
    )

    suggestion = llm.invoke(prompt.format(task=approach["task"], details=approach["details"], style=approach["style"]))

    approach['plan'] = suggestion

    return approach