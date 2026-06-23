def run(state):
    ''' Get last message from agent state.
    If we get to this state, the language model wanted to use a tool.
    The tool calls attribute will be attached to message in the Agent State. Can be a list of tool calls.
    Find relevant tool and invoke it, passing in the arguments
    '''
    print("GET SEARCH RESULTS")
    last_message = state["messages"][-1]

    if not hasattr(last_message, 'tool_calls') or not last_message.tool_calls:
        return {"messages": state['messages']}

    results = []
    for t in last_message.tool_calls:
        print(f'Calling: {t}')

        if not t['name'] in tools: # check for bad tool name
            print("\n ....bad tool name....")
            result = "bad tool name, retry" # instruct llm to retry if bad
        else:
            # pass in arguments for tool call
            result = tools[t['name']].invoke(t['args'])

        # append result as a tool message
        results.append(ToolMessage(tool_call_id = t['id'], name=t['name'], content=str(result)))

    return {"messages" : results} # langgraph adding to state in between iterations