def run(state):
    print('    🎯 Executing extracted legacy task workflow: task0')
    # Task Context: No description found
    state['context']['last_completed_step'] = 'task0'
    return state
