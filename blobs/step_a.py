def run(state):
    print(f"\n--- 🟢 Entering Runtime Node: step_a ---")
    print(f"    🔒 [Permissions] Authorized MCP Interfaces: []")
    span_id = f"span-{uuid.uuid4().hex[:8]}"
    contract_status = "VERIFIED"
    incoming_action = state.get("next_action", "PROCEED") or "PROCEED"
    if incoming_action.upper().startswith("GOTO_"):
        incoming_action = incoming_action.upper().replace("GOTO_", "", 1)
    start_time = time.perf_counter()
    try:
        SharedContextContract(**state["context"])
    except Exception as contract_err:
        print(f"    ⚠️ [Contract Breakage] Incoming schema anomaly caught at entry of step_a: {contract_err}")
        contract_status = "FAILED_ENTRY"
    try:
        module = importlib.import_module("blobs.test_blob")
        state = module.run(state)
        if contract_status == "VERIFIED":
            try:
                SharedContextContract(**state.get("context", {}))
            except Exception as contract_err_exit:
                print(f"    ❌ [Contract Breakage] Outgoing contract violation caught at exit of step_a: {contract_err_exit}")
                contract_status = "FAILED_EXIT"
    except Exception as e:
        print(f"    ❌ Execution/Contract Fault inside step_a: {e}")
        contract_status = "CRASHED"
    latency = round(time.perf_counter() - start_time, 4)
    outgoing_action = state.get("next_action", "PROCEED") or "PROCEED"
    if outgoing_action.upper().startswith("GOTO_"):
        outgoing_action = outgoing_action.upper().replace("GOTO_", "", 1)
    
    # 📊 EMIT UNIFIED SWARMHUB TELEMETRY STRIP LOG
    telemetry_span = {
        "span_id": span_id,
        "thread_id": "checkpoint-session-777",
        "node_id": "step_a",
        "latency_seconds": latency,
        "incoming_action": incoming_action.upper(),
        "outgoing_action": outgoing_action.upper(),
        "contract_status": contract_status
    }
    print(f"📊 [Telemetry Span Generated]: {json.dumps(telemetry_span)}")
    state["next_action"] = "END"
    return state