def run(state):
    if not "Twitter" in state["platforms"]:
        return {"contents": [""]}
    res = model.invoke(twitter_prompt.invoke({"text": state["text"], "research": state["research"]}))
    return {"contents": [res.content]}