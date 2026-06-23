def run(state):
    ''' Generate Bug Report '''
    prompt = ChatPromptTemplate.from_template(
        'You are tasked with generating a bug report for a Python function that raised an error.'
        'Function: {function_string}'
        'Error: {error_description}'
        'Your response must be a comprehensive string including only crucial information on the bug report'
    )
    message = HumanMessage(content=prompt.format(function_string=state.function_string, error_description=state.error_description))
    bug_report = llm.invoke([message]).content.strip()

    print('\n📝 Generating Bug Report')
    print('------------------------\n')
    print(bug_report)

    state.bug_report = bug_report
    return state