def run(state):
    ''' Find memories relevant to the current bug report '''
    prompt = ChatPromptTemplate.from_template(
        'You are tasked with archiving a bug report for a Python function that raised an error.'
        'Bug Report: {bug_report}.'
        'Your response must be a concise string including only crucial information on the bug report for future reference.'
        'Format: # function_name ## error_description ### error_analysis'
    )
    
    message = HumanMessage(content=prompt.format(
        bug_report=state.bug_report,
    ))
    
    response = llm.invoke([message]).content.strip()

    results = collection.query(query_texts=[response])

    print('\n🔎 Searching bug reports...')
    if results['ids'][0]:
        print(f'...{len(results["ids"][0])} found.\n')
        print(results)
        state.memory_search_results = [{'id':results['ids'][0][index], 'memory':results['documents'][0][index], 'distance':results['distances'][0][index]} for index, id in enumerate(results['ids'][0])]
    else:
        print('...none found.\n')
            
    return state