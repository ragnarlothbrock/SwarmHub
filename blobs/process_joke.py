def run(state):
    """Process the input text as a joke, turning it into a short, funny joke."""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Turn the following text into a short, funny joke:"},
            {"role": "user", "content": state["input_text"]}
        ]
    )
    state["processed_text"] = response.choices[0].message.content.strip()
    return state