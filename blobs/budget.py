def run(state):
    print('    🎯 Executing extracted legacy task workflow: budget')
    # Task Context: No description found
    state['context']['last_completed_step'] = 'budget'
    return state
