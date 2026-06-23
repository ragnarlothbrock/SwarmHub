def run(state):
    if not "Instagram" in state["platforms"]:
        return {"contents": [""]}
    res = model.invoke(instagram_prompt.invoke({"text": state["text"], "research": state["research"]}))
    return {"contents": [res.content]}