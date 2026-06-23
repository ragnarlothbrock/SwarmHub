def run(state):
    print('    🎯 Executing extracted legacy task workflow: writing')
    # Task Context: No description found
    state['context']['last_completed_step'] = 'writing'
    return state
