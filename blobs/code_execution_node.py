def run(state):
    ''' Run Arbitrary Code '''
    try:
        print('\nRunning Arbitrary Function')
        print('--------------------------\n')
        result = state.function(*state.arguments)
        print('\n✅ Arbitrary Function Ran Without Error')
        print(f'Result: {result}')
        print('---------------------------------------\n')
    except Exception as e:
        print(f'❌ Function Raised an Error: {e}')
        state.error = True
        state.error_description = str(e)
    return state