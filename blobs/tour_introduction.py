def run(state):
    out = get_random_art()
    out['app_message'] = tour_instructions
    return out