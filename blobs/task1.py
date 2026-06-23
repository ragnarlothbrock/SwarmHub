def run(state):
    print('    🎯 Executing extracted legacy task workflow: task1')
    # Task Context: No description found
    state['context']['last_completed_step'] = 'task1'
    return state
