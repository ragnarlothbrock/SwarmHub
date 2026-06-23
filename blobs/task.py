def run(state):
    print('    🎯 Executing extracted legacy task workflow: task')
    # Task Context: No description found
    state['context']['last_completed_step'] = 'task'
    return state
