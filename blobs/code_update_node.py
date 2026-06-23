def run(state):
    ''' Update Arbitratry Code '''
    prompt = ChatPromptTemplate.from_template(
        'You are tasked with fixing a Python function that raised an error.'
        'Function: {function_string}'
        'Error: {error_description}' 
        'You must provide a fix for the present error only.'
        'The bug fix should handle the thrown error case gracefully by returning an error message.'
        'Do not raise an error in your bug fix.'
        'The function must use the exact same name and parameters.'
        'Your response must contain only the function definition with no additional text.'
        'Your response must not contain any additional formatting, such as code delimiters or language declarations.'
    )
    message = HumanMessage(content=prompt.format(function_string=state.function_string, error_description=state.error_description))
    new_function_string = llm.invoke([message]).content.strip()

    print('\n🐛 Buggy Function')
    print('-----------------\n')
    print(state.function_string)
    print('\n🩹 Proposed Bug Fix')
    print('-------------------\n')
    print(new_function_string)
    
    state.new_function_string = new_function_string
    return state