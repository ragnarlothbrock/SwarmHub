def run(state):
    """
    Part of the Game Loop Graph.

    Manages the final phase where the player attempts to identify the killer.

    Args:
        state (GenerateGameState): The LangGraph State object containing:
            - num_guesses_left: Number of remaining guess attempts
            - characters: List of all character objects

    Returns:
        dict: Contains:
            - result: "end" if game is over, "sherlock" to continue investigation
            - num_guesses_left: Updated number of remaining guesses

    Note:
        - Handles the win/loss conditions
        - Maintains guess counter
        - Provides feedback on incorrect guesses
        - Excludes victim from suspect list
    """
    console = Console()
    num_guesses_left = state['num_guesses_left']
    all_characters = state['characters']
    non_victims = [char for char in all_characters if char.role != 'Victim']
    killer_character = next(char for char in all_characters if char.role == KILLER_ROLE)
    characters = list(sorted(non_victims, key=lambda x: x.name))

    # Print initial state
    console.rule("[bold red]🔍 Final Deduction[/bold red]")
    print_guesses_remaining(num_guesses_left)
    print_suspect_list(characters)

    is_win, is_lose = False, False

    while True:
        try:
            # Get user input
            choice = Prompt.ask(
                "\n[bold red]Who is the killer?[/bold red] (Enter suspect number)",
                default="",
                show_default=False
            )

            choice = int(choice)
            if 0 < choice <= len(characters):
                selected_character_id = choice - 1
                selected_character = characters[selected_character_id]

                if selected_character.role == KILLER_ROLE:
                    is_win = True
                    break
                else:
                    print_incorrect_guess()
                    num_guesses_left -= 1
                    if num_guesses_left > 0:
                        print_guesses_remaining(num_guesses_left)

                if num_guesses_left == 0:
                    is_lose = True
                    break

            else:
                console.print("[red]Invalid input. Please enter a valid suspect number.[/red]")
        except ValueError:
            console.print("[red]Invalid input. Please enter a number.[/red]")

    # Print final result
    print_result(is_win, is_lose, killer_character.name)

    is_end = is_win or is_lose
    return {"result": "end", "num_guesses_left": num_guesses_left} if is_end else {"result": "sherlock", "num_guesses_left": num_guesses_left}