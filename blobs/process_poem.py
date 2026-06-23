def run(state):
    """Process the input text as a poem, rewriting it in a poetic style."""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Rewrite the following text as a short, beautiful poem:"},
            {"role": "user", "content": state["input_text"]}
        ]
    )
    state["processed_text"] = response.choices[0].message.content.strip()
    return state