def run(state):
    print('    🎯 Executing extracted legacy task workflow: write')
    # Task Context: No description found
    state['context']['last_completed_step'] = 'write'
    return state
