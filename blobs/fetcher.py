def run(state):
    print("   🔍 [Blob: Researcher] Reading target topic from context...")
    topic = state["context"].get("target_topic", "")
    
    # Defensive default if the initial state passed an empty string
    if not topic:
        topic = "Agentic AI Cross-Compilers"
    
    print(f"   📊 [Blob: Researcher] Running deep industry analysis on: '{topic}'...")
    extracted_metrics = f"Metrics for {topic} [Target Year: 2026]: Developer adoption grew 300%, framework fragmentation neutralized by SwarmHub."
    
    # Mutate the context layout contract safely
    state["context"]["target_topic"] = topic
    state["context"]["raw_metrics"] = extracted_metrics
    state["next_action"] = "GOTO_PROCEED"
    return state
