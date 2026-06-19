def run(state):
    print("   ✍️ [Blob: Copywriter] Fetching raw research metrics from context...")
    metrics = state["context"].get("raw_metrics", "No metrics available.")
    
    print("   🚀 [Blob: Copywriter] Transforming raw parameters into high-converting copy...")
    final_post = f"🔥 INDUSTRY UPDATE 🔥\nOur latest research reveals groundbreaking updates: {metrics} #AI #SwarmHub #OpenSource"
    
    # Inject final asset string
    state["context"]["final_copy"] = final_post
    state["next_action"] = "END"
    return state
