def run(state):
    """
    Converts processed text into speech using a voice mapped to the content type.
    Optionally saves the audio to a file.

    Args:
        state (AgentState): Dictionary containing the processed text and content type.
        save_file (bool, optional): If True, saves the audio to a file. Defaults to False.

    Returns:
        AgentState: Updated state with audio data and file path (if saved).
    """
    
    # Map content type to a voice, defaulting to "alloy"
    voice_map = {
        "general": "alloy",
        "poem": "nova",
        "news": "onyx",
        "joke": "shimmer"
    }
    voice = voice_map.get(state["content_type"], "alloy")
    
    audio_data = io.BytesIO()

    # Generate speech and stream audio data into memory
    with client.audio.speech.with_streaming_response.create(
        model="tts-1",
        voice=voice,
        input=state["processed_text"]
    ) as response:
        for chunk in response.iter_bytes():
            audio_data.write(chunk)
    
    state["audio_data"] = audio_data.getvalue()
    
    # Save audio to a file if requested
    if save_file:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio:
            temp_audio.write(state["audio_data"])
            state["audio_path"] = temp_audio.name
    else:
        state["audio_path"] = ""
    
    return state