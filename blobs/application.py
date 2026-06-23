def run(state):
    print('    🎯 Executing extracted legacy task workflow: application')
    # Task Context: No description found
    state['context']['last_completed_step'] = 'application'
    return state
