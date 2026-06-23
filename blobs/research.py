def run(state):
    print('    🎯 Executing extracted legacy task workflow: research')
    # Task Context: No description found
    state['context']['last_completed_step'] = 'research'
    return state
