def run(state):
    ''' Fix Arbitrary Code '''
    try:
        print('\n*******************')
        print('\n❤️‍🩹 Patching code...')
        # Store the new function as a string
        new_code = state.new_function_string
        
        # Create namespace for new function
        namespace = {}
        
        # Execute new code in namespace
        exec(new_code, namespace)
        
        # Get function name dynamically
        func_name = state.function.__name__
        
        # Get the new function using dynamic name
        new_function = namespace[func_name]
        
        # Update state
        state.function = new_function
        state.error = False

        # Test the new function
        result = state.function(*state.arguments)

        print('...patch complete 😬\n')
                
    except Exception as e:
        print(f'...patch failed: {e}')
        print(f'Error details: {str(e)}')

    print('******************\n')
    return state