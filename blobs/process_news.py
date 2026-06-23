def run(state):
    """Process the input text as news, rewriting it in a formal news anchor style."""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Rewrite the following text in a formal news anchor style:"},
            {"role": "user", "content": state["input_text"]}
        ]
    )
    state["processed_text"] = response.choices[0].message.content.strip()
    return state