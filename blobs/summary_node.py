def run(state):
    print("******* Generating summary of the given text *************")
    summary = summ_model.invoke(state["text"]).content
    return {"text": state["text"], "platforms": state["platforms"], "text_summary": summary}