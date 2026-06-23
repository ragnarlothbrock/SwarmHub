def run(state):
    ''' Modify relevant memories based on new interaction '''
    prompt = ChatPromptTemplate.from_template(
        'Update the following memories based on the new interaction:'
        'Current Bug Report: {bug_report}'
        'Prior Bug Report: {memory_to_update}'
        'Your response must be a concise but cumulative string including only crucial information on the current and prior bug reports for future reference.'
        'Format: # function_name ## error_description ### error_analysis'
    )
    memory_to_update_id = state.memory_ids_to_update.pop(0)
    state.memory_search_results.pop(0)
    results = collection.get(ids=[memory_to_update_id])
    memory_to_update = results['documents'][0]
    message = HumanMessage(content=prompt.format(
        bug_report=state.bug_report,
        memory_to_update=memory_to_update,
    ))
    
    response = llm.invoke([message]).content.strip()
    
    print('\nCurrent Bug Report')
    print('------------------\n')
    print(memory_to_update)
    print('\nWill be Replaced With')
    print('---------------------\n')
    print(response)
    
    collection.update(
        ids=[memory_to_update_id],
        documents=[response],
    )
        
    return state