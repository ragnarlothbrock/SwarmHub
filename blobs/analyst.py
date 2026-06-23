def run(state):
    print('    🎯 Executing extracted legacy task workflow: analyst')
    # Task Context: No description found
    state['context']['last_completed_step'] = 'analyst'
    return state
