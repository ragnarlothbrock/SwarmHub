def run(state):
    prev_artwork = state['artwork_metadata']
    next_artwork = state['art_request']
    past_artworks = state['past_artworks']
    prompt = f"""You are an art tour guide.
    The have discussed these artworks earlier in the tour: {past_artworks}
    You just discussed this artwork:
    {prev_artwork}

    The user has requested the following for their next artwork. Choose a related artwork.
    {next_artwork}

    Return the name of the artwork and nothing else.
    """
    next_artwork = rag.query(prompt, param=QueryParam(mode="hybrid"))
    art_data = describe_artwork({'artwork': next_artwork})
    out = {
        "artwork": next_artwork,
        "past_artworks": past_artworks + [prev_artwork],
        **art_data,  # metadata + description
    }
    out.update(art_data)
    return out