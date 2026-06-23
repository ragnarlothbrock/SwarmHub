def run(state):
    ''' Generate relevant memories based on new bug report '''
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

    print('\n💾 Saving Bug Report to Memory')
    print('------------------------------\n')
    print(response)

    id = str(uuid.uuid4())
    collection.add(
        ids=[id],
        documents=[response],
    )        
    return state