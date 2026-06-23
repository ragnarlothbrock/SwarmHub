def run(state):
    """Classify the input text into one of four categories: general, poem, news, or joke."""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Classify the content as one of: 'general', 'poem', 'news', 'joke'."},
            {"role": "user", "content": state["input_text"]}
        ]
    )
    state["content_type"] = response.choices[0].message.content.strip().lower()
    return state