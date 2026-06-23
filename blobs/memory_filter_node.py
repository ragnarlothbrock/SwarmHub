def run(state):
    print('\n🗑️ Filtering bug reports...')
    for memory in state.memory_search_results:
        if memory['distance'] < 0.3:
            state.memory_ids_to_update.append(memory['id'])
        
    if state.memory_ids_to_update:
        print(f'...{len(state.memory_ids_to_update)} selected.\n')
    else:
        print('...none selected.\n')
            
    return state