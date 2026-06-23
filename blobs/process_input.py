def run(state):
    max_revision = 2
    messages = state.get('messages', [])

    last_human_index = len(messages) - 1
    for i in reversed(range(len(messages))):
        if isinstance(messages[i], HumanMessage):
            last_human_index = i
            break

    return {"last_human_index": last_human_index, "max_revisions" : max_revision, "revision_num" : 1}