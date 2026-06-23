def run(state):
    print('    🎯 Executing extracted legacy task workflow: task2')
    # Task Context: No description found
    state['context']['last_completed_step'] = 'task2'
    return state
