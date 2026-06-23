def run(state):
    if not "Blog" in state["platforms"]:
        return {"contents": [""]}
    res = model.invoke(blog_prompt.invoke({"text": state["text"], "research": state["research"]}))
    return { "contents": [res.content]}