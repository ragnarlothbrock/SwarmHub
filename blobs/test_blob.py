def run(state):
    state['context']['processed_by_blob'] = True
    state['next_action'] = 'GOTO_PROCEED'
    return state
