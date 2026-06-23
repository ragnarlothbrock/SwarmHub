def run(state):
    """
    Part of the Game Loop Graph.

    Handles the character selection phase of the investigation.

    Args:
        state (GenerateGameState): The LangGraph State object containing:
            - characters: List of all character objects

    Returns:
        dict: Result of get_character_selection containing. Adds to the State Object.
            - selected_character_id: Index of selected character or None for guessing phase

    Note:
        - Displays character list with randomized order
        - Maintains mapping between display order and original character indices
        - Prevents selection of the victim character
    """
    characters = state['characters']

    # Display characters and get the mapping of displayed order to original indices
    display_to_original = print_characters_list(characters)

    # Get user selection
    return get_character_selection(characters, display_to_original)