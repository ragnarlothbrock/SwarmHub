def run(state):
    print('    🎯 Executing extracted legacy task workflow: task3')
    # Task Context: No description found
    state['context']['last_completed_step'] = 'task3'
    return state
