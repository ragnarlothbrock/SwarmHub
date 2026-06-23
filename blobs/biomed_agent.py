def run(state):
    print('    🎯 Executing extracted legacy task workflow: biomed_agent')
    # Task Context: Conduct a thorough research about {weaviate_feature}
        Make sure you find any interesting and relevant information using the web and Weaviate blogs.
    state['context']['last_completed_step'] = 'biomed_agent'
    return state
