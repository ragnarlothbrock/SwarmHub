# ==========================================================================
# GENERATED AUTOMATICALLY BY SWARMHUB FOR AGENT: imported-legacy-agent
# TARGET RUNTIME: LangGraph (Memory Layer: in_memory | Thread: swarmhub-recovered-thread)
# ==========================================================================

import importlib
import os
import sys
import sqlite3
import json
import subprocess
import time
import uuid
from typing import Annotated, Dict, Any, List
from typing_extensions import TypedDict
from pydantic import BaseModel, Field
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver

# 1. Patch Runtime Environment Paths to discover localized Code Blobs
sys.path.insert(0, os.getcwd())

# 2. Define functional stubs for cross-compiled tools
# No external tool dependencies declared in universal spec topology.

# 2.5 Initialize Registered Global MCP Capability Interface Targets
GLOBAL_INTERFACES_REGISTRY = {}

# 3. Define strict Data Contract Verification Model schemas
class SharedContextContract(BaseModel):
    pass  # Loose empty context contract layout placeholder

# 4. Define the global State layout contract
class AgentState(TypedDict):
    messages: list
    context: Dict[str, Any]
    next_action: str

# 5. Re-hydrate Execution Anchors and Bind Run Methods
def retrieve(state: AgentState) -> AgentState:
    print(f"\n--- 🟢 Entering Runtime Node: retrieve ---")
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
        print(f"    ⚠️ [Contract Breakage] Incoming schema anomaly caught at entry of retrieve: {contract_err}")
        contract_status = "FAILED_ENTRY"
    try:
        module = importlib.import_module("blobs.retrieve")
        state = module.run(state)
        if contract_status == "VERIFIED":
            try:
                SharedContextContract(**state.get("context", {}))
            except Exception as contract_err_exit:
                print(f"    ❌ [Contract Breakage] Outgoing contract violation caught at exit of retrieve: {contract_err_exit}")
                contract_status = "FAILED_EXIT"
    except Exception as e:
        print(f"    ❌ Execution/Contract Fault inside retrieve: {e}")
        contract_status = "CRASHED"
    latency = round(time.perf_counter() - start_time, 4)
    outgoing_action = state.get("next_action", "PROCEED") or "PROCEED"
    if outgoing_action.upper().startswith("GOTO_"):
        outgoing_action = outgoing_action.upper().replace("GOTO_", "", 1)
    
    # 📊 EMIT UNIFIED SWARMHUB TELEMETRY STRIP LOG
    telemetry_span = {
        "span_id": span_id,
        "thread_id": "swarmhub-recovered-thread",
        "node_id": "retrieve",
        "latency_seconds": latency,
        "incoming_action": incoming_action.upper(),
        "outgoing_action": outgoing_action.upper(),
        "contract_status": contract_status
    }
    print(f"📊 [Telemetry Span Generated]: {json.dumps(telemetry_span)}")
    return state

def grade_documents(state: AgentState) -> AgentState:
    print(f"\n--- 🟢 Entering Runtime Node: grade_documents ---")
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
        print(f"    ⚠️ [Contract Breakage] Incoming schema anomaly caught at entry of grade_documents: {contract_err}")
        contract_status = "FAILED_ENTRY"
    try:
        module = importlib.import_module("blobs.grade_documents")
        state = module.run(state)
        if contract_status == "VERIFIED":
            try:
                SharedContextContract(**state.get("context", {}))
            except Exception as contract_err_exit:
                print(f"    ❌ [Contract Breakage] Outgoing contract violation caught at exit of grade_documents: {contract_err_exit}")
                contract_status = "FAILED_EXIT"
    except Exception as e:
        print(f"    ❌ Execution/Contract Fault inside grade_documents: {e}")
        contract_status = "CRASHED"
    latency = round(time.perf_counter() - start_time, 4)
    outgoing_action = state.get("next_action", "PROCEED") or "PROCEED"
    if outgoing_action.upper().startswith("GOTO_"):
        outgoing_action = outgoing_action.upper().replace("GOTO_", "", 1)
    
    # 📊 EMIT UNIFIED SWARMHUB TELEMETRY STRIP LOG
    telemetry_span = {
        "span_id": span_id,
        "thread_id": "swarmhub-recovered-thread",
        "node_id": "grade_documents",
        "latency_seconds": latency,
        "incoming_action": incoming_action.upper(),
        "outgoing_action": outgoing_action.upper(),
        "contract_status": contract_status
    }
    print(f"📊 [Telemetry Span Generated]: {json.dumps(telemetry_span)}")
    state["next_action"] = "END"
    return state

def generate(state: AgentState) -> AgentState:
    print(f"\n--- 🟢 Entering Runtime Node: generate ---")
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
        print(f"    ⚠️ [Contract Breakage] Incoming schema anomaly caught at entry of generate: {contract_err}")
        contract_status = "FAILED_ENTRY"
    try:
        module = importlib.import_module("blobs.generate")
        state = module.run(state)
        if contract_status == "VERIFIED":
            try:
                SharedContextContract(**state.get("context", {}))
            except Exception as contract_err_exit:
                print(f"    ❌ [Contract Breakage] Outgoing contract violation caught at exit of generate: {contract_err_exit}")
                contract_status = "FAILED_EXIT"
    except Exception as e:
        print(f"    ❌ Execution/Contract Fault inside generate: {e}")
        contract_status = "CRASHED"
    latency = round(time.perf_counter() - start_time, 4)
    outgoing_action = state.get("next_action", "PROCEED") or "PROCEED"
    if outgoing_action.upper().startswith("GOTO_"):
        outgoing_action = outgoing_action.upper().replace("GOTO_", "", 1)
    
    # 📊 EMIT UNIFIED SWARMHUB TELEMETRY STRIP LOG
    telemetry_span = {
        "span_id": span_id,
        "thread_id": "swarmhub-recovered-thread",
        "node_id": "generate",
        "latency_seconds": latency,
        "incoming_action": incoming_action.upper(),
        "outgoing_action": outgoing_action.upper(),
        "contract_status": contract_status
    }
    print(f"📊 [Telemetry Span Generated]: {json.dumps(telemetry_span)}")
    return state

def transform_query(state: AgentState) -> AgentState:
    print(f"\n--- 🟢 Entering Runtime Node: transform_query ---")
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
        print(f"    ⚠️ [Contract Breakage] Incoming schema anomaly caught at entry of transform_query: {contract_err}")
        contract_status = "FAILED_ENTRY"
    try:
        module = importlib.import_module("blobs.transform_query")
        state = module.run(state)
        if contract_status == "VERIFIED":
            try:
                SharedContextContract(**state.get("context", {}))
            except Exception as contract_err_exit:
                print(f"    ❌ [Contract Breakage] Outgoing contract violation caught at exit of transform_query: {contract_err_exit}")
                contract_status = "FAILED_EXIT"
    except Exception as e:
        print(f"    ❌ Execution/Contract Fault inside transform_query: {e}")
        contract_status = "CRASHED"
    latency = round(time.perf_counter() - start_time, 4)
    outgoing_action = state.get("next_action", "PROCEED") or "PROCEED"
    if outgoing_action.upper().startswith("GOTO_"):
        outgoing_action = outgoing_action.upper().replace("GOTO_", "", 1)
    
    # 📊 EMIT UNIFIED SWARMHUB TELEMETRY STRIP LOG
    telemetry_span = {
        "span_id": span_id,
        "thread_id": "swarmhub-recovered-thread",
        "node_id": "transform_query",
        "latency_seconds": latency,
        "incoming_action": incoming_action.upper(),
        "outgoing_action": outgoing_action.upper(),
        "contract_status": contract_status
    }
    print(f"📊 [Telemetry Span Generated]: {json.dumps(telemetry_span)}")
    return state

def retrieve(state: AgentState) -> AgentState:
    print(f"\n--- 🟢 Entering Runtime Node: retrieve ---")
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
        print(f"    ⚠️ [Contract Breakage] Incoming schema anomaly caught at entry of retrieve: {contract_err}")
        contract_status = "FAILED_ENTRY"
    try:
        module = importlib.import_module("blobs.retrieve")
        state = module.run(state)
        if contract_status == "VERIFIED":
            try:
                SharedContextContract(**state.get("context", {}))
            except Exception as contract_err_exit:
                print(f"    ❌ [Contract Breakage] Outgoing contract violation caught at exit of retrieve: {contract_err_exit}")
                contract_status = "FAILED_EXIT"
    except Exception as e:
        print(f"    ❌ Execution/Contract Fault inside retrieve: {e}")
        contract_status = "CRASHED"
    latency = round(time.perf_counter() - start_time, 4)
    outgoing_action = state.get("next_action", "PROCEED") or "PROCEED"
    if outgoing_action.upper().startswith("GOTO_"):
        outgoing_action = outgoing_action.upper().replace("GOTO_", "", 1)
    
    # 📊 EMIT UNIFIED SWARMHUB TELEMETRY STRIP LOG
    telemetry_span = {
        "span_id": span_id,
        "thread_id": "swarmhub-recovered-thread",
        "node_id": "retrieve",
        "latency_seconds": latency,
        "incoming_action": incoming_action.upper(),
        "outgoing_action": outgoing_action.upper(),
        "contract_status": contract_status
    }
    print(f"📊 [Telemetry Span Generated]: {json.dumps(telemetry_span)}")
    return state

def grade_documents(state: AgentState) -> AgentState:
    print(f"\n--- 🟢 Entering Runtime Node: grade_documents ---")
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
        print(f"    ⚠️ [Contract Breakage] Incoming schema anomaly caught at entry of grade_documents: {contract_err}")
        contract_status = "FAILED_ENTRY"
    try:
        module = importlib.import_module("blobs.grade_documents")
        state = module.run(state)
        if contract_status == "VERIFIED":
            try:
                SharedContextContract(**state.get("context", {}))
            except Exception as contract_err_exit:
                print(f"    ❌ [Contract Breakage] Outgoing contract violation caught at exit of grade_documents: {contract_err_exit}")
                contract_status = "FAILED_EXIT"
    except Exception as e:
        print(f"    ❌ Execution/Contract Fault inside grade_documents: {e}")
        contract_status = "CRASHED"
    latency = round(time.perf_counter() - start_time, 4)
    outgoing_action = state.get("next_action", "PROCEED") or "PROCEED"
    if outgoing_action.upper().startswith("GOTO_"):
        outgoing_action = outgoing_action.upper().replace("GOTO_", "", 1)
    
    # 📊 EMIT UNIFIED SWARMHUB TELEMETRY STRIP LOG
    telemetry_span = {
        "span_id": span_id,
        "thread_id": "swarmhub-recovered-thread",
        "node_id": "grade_documents",
        "latency_seconds": latency,
        "incoming_action": incoming_action.upper(),
        "outgoing_action": outgoing_action.upper(),
        "contract_status": contract_status
    }
    print(f"📊 [Telemetry Span Generated]: {json.dumps(telemetry_span)}")
    state["next_action"] = "END"
    return state

def generate(state: AgentState) -> AgentState:
    print(f"\n--- 🟢 Entering Runtime Node: generate ---")
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
        print(f"    ⚠️ [Contract Breakage] Incoming schema anomaly caught at entry of generate: {contract_err}")
        contract_status = "FAILED_ENTRY"
    try:
        module = importlib.import_module("blobs.generate")
        state = module.run(state)
        if contract_status == "VERIFIED":
            try:
                SharedContextContract(**state.get("context", {}))
            except Exception as contract_err_exit:
                print(f"    ❌ [Contract Breakage] Outgoing contract violation caught at exit of generate: {contract_err_exit}")
                contract_status = "FAILED_EXIT"
    except Exception as e:
        print(f"    ❌ Execution/Contract Fault inside generate: {e}")
        contract_status = "CRASHED"
    latency = round(time.perf_counter() - start_time, 4)
    outgoing_action = state.get("next_action", "PROCEED") or "PROCEED"
    if outgoing_action.upper().startswith("GOTO_"):
        outgoing_action = outgoing_action.upper().replace("GOTO_", "", 1)
    
    # 📊 EMIT UNIFIED SWARMHUB TELEMETRY STRIP LOG
    telemetry_span = {
        "span_id": span_id,
        "thread_id": "swarmhub-recovered-thread",
        "node_id": "generate",
        "latency_seconds": latency,
        "incoming_action": incoming_action.upper(),
        "outgoing_action": outgoing_action.upper(),
        "contract_status": contract_status
    }
    print(f"📊 [Telemetry Span Generated]: {json.dumps(telemetry_span)}")
    return state

def transform_query(state: AgentState) -> AgentState:
    print(f"\n--- 🟢 Entering Runtime Node: transform_query ---")
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
        print(f"    ⚠️ [Contract Breakage] Incoming schema anomaly caught at entry of transform_query: {contract_err}")
        contract_status = "FAILED_ENTRY"
    try:
        module = importlib.import_module("blobs.transform_query")
        state = module.run(state)
        if contract_status == "VERIFIED":
            try:
                SharedContextContract(**state.get("context", {}))
            except Exception as contract_err_exit:
                print(f"    ❌ [Contract Breakage] Outgoing contract violation caught at exit of transform_query: {contract_err_exit}")
                contract_status = "FAILED_EXIT"
    except Exception as e:
        print(f"    ❌ Execution/Contract Fault inside transform_query: {e}")
        contract_status = "CRASHED"
    latency = round(time.perf_counter() - start_time, 4)
    outgoing_action = state.get("next_action", "PROCEED") or "PROCEED"
    if outgoing_action.upper().startswith("GOTO_"):
        outgoing_action = outgoing_action.upper().replace("GOTO_", "", 1)
    
    # 📊 EMIT UNIFIED SWARMHUB TELEMETRY STRIP LOG
    telemetry_span = {
        "span_id": span_id,
        "thread_id": "swarmhub-recovered-thread",
        "node_id": "transform_query",
        "latency_seconds": latency,
        "incoming_action": incoming_action.upper(),
        "outgoing_action": outgoing_action.upper(),
        "contract_status": contract_status
    }
    print(f"📊 [Telemetry Span Generated]: {json.dumps(telemetry_span)}")
    return state

def web_search(state: AgentState) -> AgentState:
    print(f"\n--- 🟢 Entering Runtime Node: web_search ---")
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
        print(f"    ⚠️ [Contract Breakage] Incoming schema anomaly caught at entry of web_search: {contract_err}")
        contract_status = "FAILED_ENTRY"
    try:
        module = importlib.import_module("blobs.web_search")
        state = module.run(state)
        if contract_status == "VERIFIED":
            try:
                SharedContextContract(**state.get("context", {}))
            except Exception as contract_err_exit:
                print(f"    ❌ [Contract Breakage] Outgoing contract violation caught at exit of web_search: {contract_err_exit}")
                contract_status = "FAILED_EXIT"
    except Exception as e:
        print(f"    ❌ Execution/Contract Fault inside web_search: {e}")
        contract_status = "CRASHED"
    latency = round(time.perf_counter() - start_time, 4)
    outgoing_action = state.get("next_action", "PROCEED") or "PROCEED"
    if outgoing_action.upper().startswith("GOTO_"):
        outgoing_action = outgoing_action.upper().replace("GOTO_", "", 1)
    
    # 📊 EMIT UNIFIED SWARMHUB TELEMETRY STRIP LOG
    telemetry_span = {
        "span_id": span_id,
        "thread_id": "swarmhub-recovered-thread",
        "node_id": "web_search",
        "latency_seconds": latency,
        "incoming_action": incoming_action.upper(),
        "outgoing_action": outgoing_action.upper(),
        "contract_status": contract_status
    }
    print(f"📊 [Telemetry Span Generated]: {json.dumps(telemetry_span)}")
    return state

def retrieve(state: AgentState) -> AgentState:
    print(f"\n--- 🟢 Entering Runtime Node: retrieve ---")
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
        print(f"    ⚠️ [Contract Breakage] Incoming schema anomaly caught at entry of retrieve: {contract_err}")
        contract_status = "FAILED_ENTRY"
    try:
        module = importlib.import_module("blobs.retrieve")
        state = module.run(state)
        if contract_status == "VERIFIED":
            try:
                SharedContextContract(**state.get("context", {}))
            except Exception as contract_err_exit:
                print(f"    ❌ [Contract Breakage] Outgoing contract violation caught at exit of retrieve: {contract_err_exit}")
                contract_status = "FAILED_EXIT"
    except Exception as e:
        print(f"    ❌ Execution/Contract Fault inside retrieve: {e}")
        contract_status = "CRASHED"
    latency = round(time.perf_counter() - start_time, 4)
    outgoing_action = state.get("next_action", "PROCEED") or "PROCEED"
    if outgoing_action.upper().startswith("GOTO_"):
        outgoing_action = outgoing_action.upper().replace("GOTO_", "", 1)
    
    # 📊 EMIT UNIFIED SWARMHUB TELEMETRY STRIP LOG
    telemetry_span = {
        "span_id": span_id,
        "thread_id": "swarmhub-recovered-thread",
        "node_id": "retrieve",
        "latency_seconds": latency,
        "incoming_action": incoming_action.upper(),
        "outgoing_action": outgoing_action.upper(),
        "contract_status": contract_status
    }
    print(f"📊 [Telemetry Span Generated]: {json.dumps(telemetry_span)}")
    return state

def grade_documents(state: AgentState) -> AgentState:
    print(f"\n--- 🟢 Entering Runtime Node: grade_documents ---")
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
        print(f"    ⚠️ [Contract Breakage] Incoming schema anomaly caught at entry of grade_documents: {contract_err}")
        contract_status = "FAILED_ENTRY"
    try:
        module = importlib.import_module("blobs.grade_documents")
        state = module.run(state)
        if contract_status == "VERIFIED":
            try:
                SharedContextContract(**state.get("context", {}))
            except Exception as contract_err_exit:
                print(f"    ❌ [Contract Breakage] Outgoing contract violation caught at exit of grade_documents: {contract_err_exit}")
                contract_status = "FAILED_EXIT"
    except Exception as e:
        print(f"    ❌ Execution/Contract Fault inside grade_documents: {e}")
        contract_status = "CRASHED"
    latency = round(time.perf_counter() - start_time, 4)
    outgoing_action = state.get("next_action", "PROCEED") or "PROCEED"
    if outgoing_action.upper().startswith("GOTO_"):
        outgoing_action = outgoing_action.upper().replace("GOTO_", "", 1)
    
    # 📊 EMIT UNIFIED SWARMHUB TELEMETRY STRIP LOG
    telemetry_span = {
        "span_id": span_id,
        "thread_id": "swarmhub-recovered-thread",
        "node_id": "grade_documents",
        "latency_seconds": latency,
        "incoming_action": incoming_action.upper(),
        "outgoing_action": outgoing_action.upper(),
        "contract_status": contract_status
    }
    print(f"📊 [Telemetry Span Generated]: {json.dumps(telemetry_span)}")
    state["next_action"] = "END"
    return state

def generate(state: AgentState) -> AgentState:
    print(f"\n--- 🟢 Entering Runtime Node: generate ---")
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
        print(f"    ⚠️ [Contract Breakage] Incoming schema anomaly caught at entry of generate: {contract_err}")
        contract_status = "FAILED_ENTRY"
    try:
        module = importlib.import_module("blobs.generate")
        state = module.run(state)
        if contract_status == "VERIFIED":
            try:
                SharedContextContract(**state.get("context", {}))
            except Exception as contract_err_exit:
                print(f"    ❌ [Contract Breakage] Outgoing contract violation caught at exit of generate: {contract_err_exit}")
                contract_status = "FAILED_EXIT"
    except Exception as e:
        print(f"    ❌ Execution/Contract Fault inside generate: {e}")
        contract_status = "CRASHED"
    latency = round(time.perf_counter() - start_time, 4)
    outgoing_action = state.get("next_action", "PROCEED") or "PROCEED"
    if outgoing_action.upper().startswith("GOTO_"):
        outgoing_action = outgoing_action.upper().replace("GOTO_", "", 1)
    
    # 📊 EMIT UNIFIED SWARMHUB TELEMETRY STRIP LOG
    telemetry_span = {
        "span_id": span_id,
        "thread_id": "swarmhub-recovered-thread",
        "node_id": "generate",
        "latency_seconds": latency,
        "incoming_action": incoming_action.upper(),
        "outgoing_action": outgoing_action.upper(),
        "contract_status": contract_status
    }
    print(f"📊 [Telemetry Span Generated]: {json.dumps(telemetry_span)}")
    return state

def transform_query(state: AgentState) -> AgentState:
    print(f"\n--- 🟢 Entering Runtime Node: transform_query ---")
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
        print(f"    ⚠️ [Contract Breakage] Incoming schema anomaly caught at entry of transform_query: {contract_err}")
        contract_status = "FAILED_ENTRY"
    try:
        module = importlib.import_module("blobs.transform_query")
        state = module.run(state)
        if contract_status == "VERIFIED":
            try:
                SharedContextContract(**state.get("context", {}))
            except Exception as contract_err_exit:
                print(f"    ❌ [Contract Breakage] Outgoing contract violation caught at exit of transform_query: {contract_err_exit}")
                contract_status = "FAILED_EXIT"
    except Exception as e:
        print(f"    ❌ Execution/Contract Fault inside transform_query: {e}")
        contract_status = "CRASHED"
    latency = round(time.perf_counter() - start_time, 4)
    outgoing_action = state.get("next_action", "PROCEED") or "PROCEED"
    if outgoing_action.upper().startswith("GOTO_"):
        outgoing_action = outgoing_action.upper().replace("GOTO_", "", 1)
    
    # 📊 EMIT UNIFIED SWARMHUB TELEMETRY STRIP LOG
    telemetry_span = {
        "span_id": span_id,
        "thread_id": "swarmhub-recovered-thread",
        "node_id": "transform_query",
        "latency_seconds": latency,
        "incoming_action": incoming_action.upper(),
        "outgoing_action": outgoing_action.upper(),
        "contract_status": contract_status
    }
    print(f"📊 [Telemetry Span Generated]: {json.dumps(telemetry_span)}")
    return state

def retrieve(state: AgentState) -> AgentState:
    print(f"\n--- 🟢 Entering Runtime Node: retrieve ---")
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
        print(f"    ⚠️ [Contract Breakage] Incoming schema anomaly caught at entry of retrieve: {contract_err}")
        contract_status = "FAILED_ENTRY"
    try:
        module = importlib.import_module("blobs.retrieve")
        state = module.run(state)
        if contract_status == "VERIFIED":
            try:
                SharedContextContract(**state.get("context", {}))
            except Exception as contract_err_exit:
                print(f"    ❌ [Contract Breakage] Outgoing contract violation caught at exit of retrieve: {contract_err_exit}")
                contract_status = "FAILED_EXIT"
    except Exception as e:
        print(f"    ❌ Execution/Contract Fault inside retrieve: {e}")
        contract_status = "CRASHED"
    latency = round(time.perf_counter() - start_time, 4)
    outgoing_action = state.get("next_action", "PROCEED") or "PROCEED"
    if outgoing_action.upper().startswith("GOTO_"):
        outgoing_action = outgoing_action.upper().replace("GOTO_", "", 1)
    
    # 📊 EMIT UNIFIED SWARMHUB TELEMETRY STRIP LOG
    telemetry_span = {
        "span_id": span_id,
        "thread_id": "swarmhub-recovered-thread",
        "node_id": "retrieve",
        "latency_seconds": latency,
        "incoming_action": incoming_action.upper(),
        "outgoing_action": outgoing_action.upper(),
        "contract_status": contract_status
    }
    print(f"📊 [Telemetry Span Generated]: {json.dumps(telemetry_span)}")
    return state

def grade_documents(state: AgentState) -> AgentState:
    print(f"\n--- 🟢 Entering Runtime Node: grade_documents ---")
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
        print(f"    ⚠️ [Contract Breakage] Incoming schema anomaly caught at entry of grade_documents: {contract_err}")
        contract_status = "FAILED_ENTRY"
    try:
        module = importlib.import_module("blobs.grade_documents")
        state = module.run(state)
        if contract_status == "VERIFIED":
            try:
                SharedContextContract(**state.get("context", {}))
            except Exception as contract_err_exit:
                print(f"    ❌ [Contract Breakage] Outgoing contract violation caught at exit of grade_documents: {contract_err_exit}")
                contract_status = "FAILED_EXIT"
    except Exception as e:
        print(f"    ❌ Execution/Contract Fault inside grade_documents: {e}")
        contract_status = "CRASHED"
    latency = round(time.perf_counter() - start_time, 4)
    outgoing_action = state.get("next_action", "PROCEED") or "PROCEED"
    if outgoing_action.upper().startswith("GOTO_"):
        outgoing_action = outgoing_action.upper().replace("GOTO_", "", 1)
    
    # 📊 EMIT UNIFIED SWARMHUB TELEMETRY STRIP LOG
    telemetry_span = {
        "span_id": span_id,
        "thread_id": "swarmhub-recovered-thread",
        "node_id": "grade_documents",
        "latency_seconds": latency,
        "incoming_action": incoming_action.upper(),
        "outgoing_action": outgoing_action.upper(),
        "contract_status": contract_status
    }
    print(f"📊 [Telemetry Span Generated]: {json.dumps(telemetry_span)}")
    state["next_action"] = "END"
    return state

def generate(state: AgentState) -> AgentState:
    print(f"\n--- 🟢 Entering Runtime Node: generate ---")
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
        print(f"    ⚠️ [Contract Breakage] Incoming schema anomaly caught at entry of generate: {contract_err}")
        contract_status = "FAILED_ENTRY"
    try:
        module = importlib.import_module("blobs.generate")
        state = module.run(state)
        if contract_status == "VERIFIED":
            try:
                SharedContextContract(**state.get("context", {}))
            except Exception as contract_err_exit:
                print(f"    ❌ [Contract Breakage] Outgoing contract violation caught at exit of generate: {contract_err_exit}")
                contract_status = "FAILED_EXIT"
    except Exception as e:
        print(f"    ❌ Execution/Contract Fault inside generate: {e}")
        contract_status = "CRASHED"
    latency = round(time.perf_counter() - start_time, 4)
    outgoing_action = state.get("next_action", "PROCEED") or "PROCEED"
    if outgoing_action.upper().startswith("GOTO_"):
        outgoing_action = outgoing_action.upper().replace("GOTO_", "", 1)
    
    # 📊 EMIT UNIFIED SWARMHUB TELEMETRY STRIP LOG
    telemetry_span = {
        "span_id": span_id,
        "thread_id": "swarmhub-recovered-thread",
        "node_id": "generate",
        "latency_seconds": latency,
        "incoming_action": incoming_action.upper(),
        "outgoing_action": outgoing_action.upper(),
        "contract_status": contract_status
    }
    print(f"📊 [Telemetry Span Generated]: {json.dumps(telemetry_span)}")
    return state

def transform_query(state: AgentState) -> AgentState:
    print(f"\n--- 🟢 Entering Runtime Node: transform_query ---")
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
        print(f"    ⚠️ [Contract Breakage] Incoming schema anomaly caught at entry of transform_query: {contract_err}")
        contract_status = "FAILED_ENTRY"
    try:
        module = importlib.import_module("blobs.transform_query")
        state = module.run(state)
        if contract_status == "VERIFIED":
            try:
                SharedContextContract(**state.get("context", {}))
            except Exception as contract_err_exit:
                print(f"    ❌ [Contract Breakage] Outgoing contract violation caught at exit of transform_query: {contract_err_exit}")
                contract_status = "FAILED_EXIT"
    except Exception as e:
        print(f"    ❌ Execution/Contract Fault inside transform_query: {e}")
        contract_status = "CRASHED"
    latency = round(time.perf_counter() - start_time, 4)
    outgoing_action = state.get("next_action", "PROCEED") or "PROCEED"
    if outgoing_action.upper().startswith("GOTO_"):
        outgoing_action = outgoing_action.upper().replace("GOTO_", "", 1)
    
    # 📊 EMIT UNIFIED SWARMHUB TELEMETRY STRIP LOG
    telemetry_span = {
        "span_id": span_id,
        "thread_id": "swarmhub-recovered-thread",
        "node_id": "transform_query",
        "latency_seconds": latency,
        "incoming_action": incoming_action.upper(),
        "outgoing_action": outgoing_action.upper(),
        "contract_status": contract_status
    }
    print(f"📊 [Telemetry Span Generated]: {json.dumps(telemetry_span)}")
    return state

def retrieve(state: AgentState) -> AgentState:
    print(f"\n--- 🟢 Entering Runtime Node: retrieve ---")
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
        print(f"    ⚠️ [Contract Breakage] Incoming schema anomaly caught at entry of retrieve: {contract_err}")
        contract_status = "FAILED_ENTRY"
    try:
        module = importlib.import_module("blobs.retrieve")
        state = module.run(state)
        if contract_status == "VERIFIED":
            try:
                SharedContextContract(**state.get("context", {}))
            except Exception as contract_err_exit:
                print(f"    ❌ [Contract Breakage] Outgoing contract violation caught at exit of retrieve: {contract_err_exit}")
                contract_status = "FAILED_EXIT"
    except Exception as e:
        print(f"    ❌ Execution/Contract Fault inside retrieve: {e}")
        contract_status = "CRASHED"
    latency = round(time.perf_counter() - start_time, 4)
    outgoing_action = state.get("next_action", "PROCEED") or "PROCEED"
    if outgoing_action.upper().startswith("GOTO_"):
        outgoing_action = outgoing_action.upper().replace("GOTO_", "", 1)
    
    # 📊 EMIT UNIFIED SWARMHUB TELEMETRY STRIP LOG
    telemetry_span = {
        "span_id": span_id,
        "thread_id": "swarmhub-recovered-thread",
        "node_id": "retrieve",
        "latency_seconds": latency,
        "incoming_action": incoming_action.upper(),
        "outgoing_action": outgoing_action.upper(),
        "contract_status": contract_status
    }
    print(f"📊 [Telemetry Span Generated]: {json.dumps(telemetry_span)}")
    return state

def grade_documents(state: AgentState) -> AgentState:
    print(f"\n--- 🟢 Entering Runtime Node: grade_documents ---")
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
        print(f"    ⚠️ [Contract Breakage] Incoming schema anomaly caught at entry of grade_documents: {contract_err}")
        contract_status = "FAILED_ENTRY"
    try:
        module = importlib.import_module("blobs.grade_documents")
        state = module.run(state)
        if contract_status == "VERIFIED":
            try:
                SharedContextContract(**state.get("context", {}))
            except Exception as contract_err_exit:
                print(f"    ❌ [Contract Breakage] Outgoing contract violation caught at exit of grade_documents: {contract_err_exit}")
                contract_status = "FAILED_EXIT"
    except Exception as e:
        print(f"    ❌ Execution/Contract Fault inside grade_documents: {e}")
        contract_status = "CRASHED"
    latency = round(time.perf_counter() - start_time, 4)
    outgoing_action = state.get("next_action", "PROCEED") or "PROCEED"
    if outgoing_action.upper().startswith("GOTO_"):
        outgoing_action = outgoing_action.upper().replace("GOTO_", "", 1)
    
    # 📊 EMIT UNIFIED SWARMHUB TELEMETRY STRIP LOG
    telemetry_span = {
        "span_id": span_id,
        "thread_id": "swarmhub-recovered-thread",
        "node_id": "grade_documents",
        "latency_seconds": latency,
        "incoming_action": incoming_action.upper(),
        "outgoing_action": outgoing_action.upper(),
        "contract_status": contract_status
    }
    print(f"📊 [Telemetry Span Generated]: {json.dumps(telemetry_span)}")
    state["next_action"] = "END"
    return state

def generate(state: AgentState) -> AgentState:
    print(f"\n--- 🟢 Entering Runtime Node: generate ---")
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
        print(f"    ⚠️ [Contract Breakage] Incoming schema anomaly caught at entry of generate: {contract_err}")
        contract_status = "FAILED_ENTRY"
    try:
        module = importlib.import_module("blobs.generate")
        state = module.run(state)
        if contract_status == "VERIFIED":
            try:
                SharedContextContract(**state.get("context", {}))
            except Exception as contract_err_exit:
                print(f"    ❌ [Contract Breakage] Outgoing contract violation caught at exit of generate: {contract_err_exit}")
                contract_status = "FAILED_EXIT"
    except Exception as e:
        print(f"    ❌ Execution/Contract Fault inside generate: {e}")
        contract_status = "CRASHED"
    latency = round(time.perf_counter() - start_time, 4)
    outgoing_action = state.get("next_action", "PROCEED") or "PROCEED"
    if outgoing_action.upper().startswith("GOTO_"):
        outgoing_action = outgoing_action.upper().replace("GOTO_", "", 1)
    
    # 📊 EMIT UNIFIED SWARMHUB TELEMETRY STRIP LOG
    telemetry_span = {
        "span_id": span_id,
        "thread_id": "swarmhub-recovered-thread",
        "node_id": "generate",
        "latency_seconds": latency,
        "incoming_action": incoming_action.upper(),
        "outgoing_action": outgoing_action.upper(),
        "contract_status": contract_status
    }
    print(f"📊 [Telemetry Span Generated]: {json.dumps(telemetry_span)}")
    return state

def web_search(state: AgentState) -> AgentState:
    print(f"\n--- 🟢 Entering Runtime Node: web_search ---")
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
        print(f"    ⚠️ [Contract Breakage] Incoming schema anomaly caught at entry of web_search: {contract_err}")
        contract_status = "FAILED_ENTRY"
    try:
        module = importlib.import_module("blobs.web_search")
        state = module.run(state)
        if contract_status == "VERIFIED":
            try:
                SharedContextContract(**state.get("context", {}))
            except Exception as contract_err_exit:
                print(f"    ❌ [Contract Breakage] Outgoing contract violation caught at exit of web_search: {contract_err_exit}")
                contract_status = "FAILED_EXIT"
    except Exception as e:
        print(f"    ❌ Execution/Contract Fault inside web_search: {e}")
        contract_status = "CRASHED"
    latency = round(time.perf_counter() - start_time, 4)
    outgoing_action = state.get("next_action", "PROCEED") or "PROCEED"
    if outgoing_action.upper().startswith("GOTO_"):
        outgoing_action = outgoing_action.upper().replace("GOTO_", "", 1)
    
    # 📊 EMIT UNIFIED SWARMHUB TELEMETRY STRIP LOG
    telemetry_span = {
        "span_id": span_id,
        "thread_id": "swarmhub-recovered-thread",
        "node_id": "web_search",
        "latency_seconds": latency,
        "incoming_action": incoming_action.upper(),
        "outgoing_action": outgoing_action.upper(),
        "contract_status": contract_status
    }
    print(f"📊 [Telemetry Span Generated]: {json.dumps(telemetry_span)}")
    return state

def retrieve(state: AgentState) -> AgentState:
    print(f"\n--- 🟢 Entering Runtime Node: retrieve ---")
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
        print(f"    ⚠️ [Contract Breakage] Incoming schema anomaly caught at entry of retrieve: {contract_err}")
        contract_status = "FAILED_ENTRY"
    try:
        module = importlib.import_module("blobs.retrieve")
        state = module.run(state)
        if contract_status == "VERIFIED":
            try:
                SharedContextContract(**state.get("context", {}))
            except Exception as contract_err_exit:
                print(f"    ❌ [Contract Breakage] Outgoing contract violation caught at exit of retrieve: {contract_err_exit}")
                contract_status = "FAILED_EXIT"
    except Exception as e:
        print(f"    ❌ Execution/Contract Fault inside retrieve: {e}")
        contract_status = "CRASHED"
    latency = round(time.perf_counter() - start_time, 4)
    outgoing_action = state.get("next_action", "PROCEED") or "PROCEED"
    if outgoing_action.upper().startswith("GOTO_"):
        outgoing_action = outgoing_action.upper().replace("GOTO_", "", 1)
    
    # 📊 EMIT UNIFIED SWARMHUB TELEMETRY STRIP LOG
    telemetry_span = {
        "span_id": span_id,
        "thread_id": "swarmhub-recovered-thread",
        "node_id": "retrieve",
        "latency_seconds": latency,
        "incoming_action": incoming_action.upper(),
        "outgoing_action": outgoing_action.upper(),
        "contract_status": contract_status
    }
    print(f"📊 [Telemetry Span Generated]: {json.dumps(telemetry_span)}")
    return state

def grade_documents(state: AgentState) -> AgentState:
    print(f"\n--- 🟢 Entering Runtime Node: grade_documents ---")
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
        print(f"    ⚠️ [Contract Breakage] Incoming schema anomaly caught at entry of grade_documents: {contract_err}")
        contract_status = "FAILED_ENTRY"
    try:
        module = importlib.import_module("blobs.grade_documents")
        state = module.run(state)
        if contract_status == "VERIFIED":
            try:
                SharedContextContract(**state.get("context", {}))
            except Exception as contract_err_exit:
                print(f"    ❌ [Contract Breakage] Outgoing contract violation caught at exit of grade_documents: {contract_err_exit}")
                contract_status = "FAILED_EXIT"
    except Exception as e:
        print(f"    ❌ Execution/Contract Fault inside grade_documents: {e}")
        contract_status = "CRASHED"
    latency = round(time.perf_counter() - start_time, 4)
    outgoing_action = state.get("next_action", "PROCEED") or "PROCEED"
    if outgoing_action.upper().startswith("GOTO_"):
        outgoing_action = outgoing_action.upper().replace("GOTO_", "", 1)
    
    # 📊 EMIT UNIFIED SWARMHUB TELEMETRY STRIP LOG
    telemetry_span = {
        "span_id": span_id,
        "thread_id": "swarmhub-recovered-thread",
        "node_id": "grade_documents",
        "latency_seconds": latency,
        "incoming_action": incoming_action.upper(),
        "outgoing_action": outgoing_action.upper(),
        "contract_status": contract_status
    }
    print(f"📊 [Telemetry Span Generated]: {json.dumps(telemetry_span)}")
    state["next_action"] = "END"
    return state

def generate(state: AgentState) -> AgentState:
    print(f"\n--- 🟢 Entering Runtime Node: generate ---")
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
        print(f"    ⚠️ [Contract Breakage] Incoming schema anomaly caught at entry of generate: {contract_err}")
        contract_status = "FAILED_ENTRY"
    try:
        module = importlib.import_module("blobs.generate")
        state = module.run(state)
        if contract_status == "VERIFIED":
            try:
                SharedContextContract(**state.get("context", {}))
            except Exception as contract_err_exit:
                print(f"    ❌ [Contract Breakage] Outgoing contract violation caught at exit of generate: {contract_err_exit}")
                contract_status = "FAILED_EXIT"
    except Exception as e:
        print(f"    ❌ Execution/Contract Fault inside generate: {e}")
        contract_status = "CRASHED"
    latency = round(time.perf_counter() - start_time, 4)
    outgoing_action = state.get("next_action", "PROCEED") or "PROCEED"
    if outgoing_action.upper().startswith("GOTO_"):
        outgoing_action = outgoing_action.upper().replace("GOTO_", "", 1)
    
    # 📊 EMIT UNIFIED SWARMHUB TELEMETRY STRIP LOG
    telemetry_span = {
        "span_id": span_id,
        "thread_id": "swarmhub-recovered-thread",
        "node_id": "generate",
        "latency_seconds": latency,
        "incoming_action": incoming_action.upper(),
        "outgoing_action": outgoing_action.upper(),
        "contract_status": contract_status
    }
    print(f"📊 [Telemetry Span Generated]: {json.dumps(telemetry_span)}")
    return state

def transform_query(state: AgentState) -> AgentState:
    print(f"\n--- 🟢 Entering Runtime Node: transform_query ---")
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
        print(f"    ⚠️ [Contract Breakage] Incoming schema anomaly caught at entry of transform_query: {contract_err}")
        contract_status = "FAILED_ENTRY"
    try:
        module = importlib.import_module("blobs.transform_query")
        state = module.run(state)
        if contract_status == "VERIFIED":
            try:
                SharedContextContract(**state.get("context", {}))
            except Exception as contract_err_exit:
                print(f"    ❌ [Contract Breakage] Outgoing contract violation caught at exit of transform_query: {contract_err_exit}")
                contract_status = "FAILED_EXIT"
    except Exception as e:
        print(f"    ❌ Execution/Contract Fault inside transform_query: {e}")
        contract_status = "CRASHED"
    latency = round(time.perf_counter() - start_time, 4)
    outgoing_action = state.get("next_action", "PROCEED") or "PROCEED"
    if outgoing_action.upper().startswith("GOTO_"):
        outgoing_action = outgoing_action.upper().replace("GOTO_", "", 1)
    
    # 📊 EMIT UNIFIED SWARMHUB TELEMETRY STRIP LOG
    telemetry_span = {
        "span_id": span_id,
        "thread_id": "swarmhub-recovered-thread",
        "node_id": "transform_query",
        "latency_seconds": latency,
        "incoming_action": incoming_action.upper(),
        "outgoing_action": outgoing_action.upper(),
        "contract_status": contract_status
    }
    print(f"📊 [Telemetry Span Generated]: {json.dumps(telemetry_span)}")
    return state

def web_search_node(state: AgentState) -> AgentState:
    print(f"\n--- 🟢 Entering Runtime Node: web_search_node ---")
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
        print(f"    ⚠️ [Contract Breakage] Incoming schema anomaly caught at entry of web_search_node: {contract_err}")
        contract_status = "FAILED_ENTRY"
    try:
        module = importlib.import_module("blobs.web_search_node")
        state = module.run(state)
        if contract_status == "VERIFIED":
            try:
                SharedContextContract(**state.get("context", {}))
            except Exception as contract_err_exit:
                print(f"    ❌ [Contract Breakage] Outgoing contract violation caught at exit of web_search_node: {contract_err_exit}")
                contract_status = "FAILED_EXIT"
    except Exception as e:
        print(f"    ❌ Execution/Contract Fault inside web_search_node: {e}")
        contract_status = "CRASHED"
    latency = round(time.perf_counter() - start_time, 4)
    outgoing_action = state.get("next_action", "PROCEED") or "PROCEED"
    if outgoing_action.upper().startswith("GOTO_"):
        outgoing_action = outgoing_action.upper().replace("GOTO_", "", 1)
    
    # 📊 EMIT UNIFIED SWARMHUB TELEMETRY STRIP LOG
    telemetry_span = {
        "span_id": span_id,
        "thread_id": "swarmhub-recovered-thread",
        "node_id": "web_search_node",
        "latency_seconds": latency,
        "incoming_action": incoming_action.upper(),
        "outgoing_action": outgoing_action.upper(),
        "contract_status": contract_status
    }
    print(f"📊 [Telemetry Span Generated]: {json.dumps(telemetry_span)}")
    return state

def web_search(state: AgentState) -> AgentState:
    print(f"\n--- 🟢 Entering Runtime Node: web_search ---")
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
        print(f"    ⚠️ [Contract Breakage] Incoming schema anomaly caught at entry of web_search: {contract_err}")
        contract_status = "FAILED_ENTRY"
    try:
        module = importlib.import_module("blobs.web_search")
        state = module.run(state)
        if contract_status == "VERIFIED":
            try:
                SharedContextContract(**state.get("context", {}))
            except Exception as contract_err_exit:
                print(f"    ❌ [Contract Breakage] Outgoing contract violation caught at exit of web_search: {contract_err_exit}")
                contract_status = "FAILED_EXIT"
    except Exception as e:
        print(f"    ❌ Execution/Contract Fault inside web_search: {e}")
        contract_status = "CRASHED"
    latency = round(time.perf_counter() - start_time, 4)
    outgoing_action = state.get("next_action", "PROCEED") or "PROCEED"
    if outgoing_action.upper().startswith("GOTO_"):
        outgoing_action = outgoing_action.upper().replace("GOTO_", "", 1)
    
    # 📊 EMIT UNIFIED SWARMHUB TELEMETRY STRIP LOG
    telemetry_span = {
        "span_id": span_id,
        "thread_id": "swarmhub-recovered-thread",
        "node_id": "web_search",
        "latency_seconds": latency,
        "incoming_action": incoming_action.upper(),
        "outgoing_action": outgoing_action.upper(),
        "contract_status": contract_status
    }
    print(f"📊 [Telemetry Span Generated]: {json.dumps(telemetry_span)}")
    return state

def retrieve(state: AgentState) -> AgentState:
    print(f"\n--- 🟢 Entering Runtime Node: retrieve ---")
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
        print(f"    ⚠️ [Contract Breakage] Incoming schema anomaly caught at entry of retrieve: {contract_err}")
        contract_status = "FAILED_ENTRY"
    try:
        module = importlib.import_module("blobs.retrieve")
        state = module.run(state)
        if contract_status == "VERIFIED":
            try:
                SharedContextContract(**state.get("context", {}))
            except Exception as contract_err_exit:
                print(f"    ❌ [Contract Breakage] Outgoing contract violation caught at exit of retrieve: {contract_err_exit}")
                contract_status = "FAILED_EXIT"
    except Exception as e:
        print(f"    ❌ Execution/Contract Fault inside retrieve: {e}")
        contract_status = "CRASHED"
    latency = round(time.perf_counter() - start_time, 4)
    outgoing_action = state.get("next_action", "PROCEED") or "PROCEED"
    if outgoing_action.upper().startswith("GOTO_"):
        outgoing_action = outgoing_action.upper().replace("GOTO_", "", 1)
    
    # 📊 EMIT UNIFIED SWARMHUB TELEMETRY STRIP LOG
    telemetry_span = {
        "span_id": span_id,
        "thread_id": "swarmhub-recovered-thread",
        "node_id": "retrieve",
        "latency_seconds": latency,
        "incoming_action": incoming_action.upper(),
        "outgoing_action": outgoing_action.upper(),
        "contract_status": contract_status
    }
    print(f"📊 [Telemetry Span Generated]: {json.dumps(telemetry_span)}")
    return state

def grade_documents(state: AgentState) -> AgentState:
    print(f"\n--- 🟢 Entering Runtime Node: grade_documents ---")
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
        print(f"    ⚠️ [Contract Breakage] Incoming schema anomaly caught at entry of grade_documents: {contract_err}")
        contract_status = "FAILED_ENTRY"
    try:
        module = importlib.import_module("blobs.grade_documents")
        state = module.run(state)
        if contract_status == "VERIFIED":
            try:
                SharedContextContract(**state.get("context", {}))
            except Exception as contract_err_exit:
                print(f"    ❌ [Contract Breakage] Outgoing contract violation caught at exit of grade_documents: {contract_err_exit}")
                contract_status = "FAILED_EXIT"
    except Exception as e:
        print(f"    ❌ Execution/Contract Fault inside grade_documents: {e}")
        contract_status = "CRASHED"
    latency = round(time.perf_counter() - start_time, 4)
    outgoing_action = state.get("next_action", "PROCEED") or "PROCEED"
    if outgoing_action.upper().startswith("GOTO_"):
        outgoing_action = outgoing_action.upper().replace("GOTO_", "", 1)
    
    # 📊 EMIT UNIFIED SWARMHUB TELEMETRY STRIP LOG
    telemetry_span = {
        "span_id": span_id,
        "thread_id": "swarmhub-recovered-thread",
        "node_id": "grade_documents",
        "latency_seconds": latency,
        "incoming_action": incoming_action.upper(),
        "outgoing_action": outgoing_action.upper(),
        "contract_status": contract_status
    }
    print(f"📊 [Telemetry Span Generated]: {json.dumps(telemetry_span)}")
    state["next_action"] = "END"
    return state

def generate(state: AgentState) -> AgentState:
    print(f"\n--- 🟢 Entering Runtime Node: generate ---")
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
        print(f"    ⚠️ [Contract Breakage] Incoming schema anomaly caught at entry of generate: {contract_err}")
        contract_status = "FAILED_ENTRY"
    try:
        module = importlib.import_module("blobs.generate")
        state = module.run(state)
        if contract_status == "VERIFIED":
            try:
                SharedContextContract(**state.get("context", {}))
            except Exception as contract_err_exit:
                print(f"    ❌ [Contract Breakage] Outgoing contract violation caught at exit of generate: {contract_err_exit}")
                contract_status = "FAILED_EXIT"
    except Exception as e:
        print(f"    ❌ Execution/Contract Fault inside generate: {e}")
        contract_status = "CRASHED"
    latency = round(time.perf_counter() - start_time, 4)
    outgoing_action = state.get("next_action", "PROCEED") or "PROCEED"
    if outgoing_action.upper().startswith("GOTO_"):
        outgoing_action = outgoing_action.upper().replace("GOTO_", "", 1)
    
    # 📊 EMIT UNIFIED SWARMHUB TELEMETRY STRIP LOG
    telemetry_span = {
        "span_id": span_id,
        "thread_id": "swarmhub-recovered-thread",
        "node_id": "generate",
        "latency_seconds": latency,
        "incoming_action": incoming_action.upper(),
        "outgoing_action": outgoing_action.upper(),
        "contract_status": contract_status
    }
    print(f"📊 [Telemetry Span Generated]: {json.dumps(telemetry_span)}")
    return state

def transform_query(state: AgentState) -> AgentState:
    print(f"\n--- 🟢 Entering Runtime Node: transform_query ---")
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
        print(f"    ⚠️ [Contract Breakage] Incoming schema anomaly caught at entry of transform_query: {contract_err}")
        contract_status = "FAILED_ENTRY"
    try:
        module = importlib.import_module("blobs.transform_query")
        state = module.run(state)
        if contract_status == "VERIFIED":
            try:
                SharedContextContract(**state.get("context", {}))
            except Exception as contract_err_exit:
                print(f"    ❌ [Contract Breakage] Outgoing contract violation caught at exit of transform_query: {contract_err_exit}")
                contract_status = "FAILED_EXIT"
    except Exception as e:
        print(f"    ❌ Execution/Contract Fault inside transform_query: {e}")
        contract_status = "CRASHED"
    latency = round(time.perf_counter() - start_time, 4)
    outgoing_action = state.get("next_action", "PROCEED") or "PROCEED"
    if outgoing_action.upper().startswith("GOTO_"):
        outgoing_action = outgoing_action.upper().replace("GOTO_", "", 1)
    
    # 📊 EMIT UNIFIED SWARMHUB TELEMETRY STRIP LOG
    telemetry_span = {
        "span_id": span_id,
        "thread_id": "swarmhub-recovered-thread",
        "node_id": "transform_query",
        "latency_seconds": latency,
        "incoming_action": incoming_action.upper(),
        "outgoing_action": outgoing_action.upper(),
        "contract_status": contract_status
    }
    print(f"📊 [Telemetry Span Generated]: {json.dumps(telemetry_span)}")
    return state

def agent(state: AgentState) -> AgentState:
    print(f"\n--- 🟢 Entering Runtime Node: agent ---")
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
        print(f"    ⚠️ [Contract Breakage] Incoming schema anomaly caught at entry of agent: {contract_err}")
        contract_status = "FAILED_ENTRY"
    try:
        module = importlib.import_module("blobs.agent")
        state = module.run(state)
        if contract_status == "VERIFIED":
            try:
                SharedContextContract(**state.get("context", {}))
            except Exception as contract_err_exit:
                print(f"    ❌ [Contract Breakage] Outgoing contract violation caught at exit of agent: {contract_err_exit}")
                contract_status = "FAILED_EXIT"
    except Exception as e:
        print(f"    ❌ Execution/Contract Fault inside agent: {e}")
        contract_status = "CRASHED"
    latency = round(time.perf_counter() - start_time, 4)
    outgoing_action = state.get("next_action", "PROCEED") or "PROCEED"
    if outgoing_action.upper().startswith("GOTO_"):
        outgoing_action = outgoing_action.upper().replace("GOTO_", "", 1)
    
    # 📊 EMIT UNIFIED SWARMHUB TELEMETRY STRIP LOG
    telemetry_span = {
        "span_id": span_id,
        "thread_id": "swarmhub-recovered-thread",
        "node_id": "agent",
        "latency_seconds": latency,
        "incoming_action": incoming_action.upper(),
        "outgoing_action": outgoing_action.upper(),
        "contract_status": contract_status
    }
    print(f"📊 [Telemetry Span Generated]: {json.dumps(telemetry_span)}")
    state["next_action"] = "END"
    return state

def retrieve(state: AgentState) -> AgentState:
    print(f"\n--- 🟢 Entering Runtime Node: retrieve ---")
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
        print(f"    ⚠️ [Contract Breakage] Incoming schema anomaly caught at entry of retrieve: {contract_err}")
        contract_status = "FAILED_ENTRY"
    try:
        module = importlib.import_module("blobs.retrieve")
        state = module.run(state)
        if contract_status == "VERIFIED":
            try:
                SharedContextContract(**state.get("context", {}))
            except Exception as contract_err_exit:
                print(f"    ❌ [Contract Breakage] Outgoing contract violation caught at exit of retrieve: {contract_err_exit}")
                contract_status = "FAILED_EXIT"
    except Exception as e:
        print(f"    ❌ Execution/Contract Fault inside retrieve: {e}")
        contract_status = "CRASHED"
    latency = round(time.perf_counter() - start_time, 4)
    outgoing_action = state.get("next_action", "PROCEED") or "PROCEED"
    if outgoing_action.upper().startswith("GOTO_"):
        outgoing_action = outgoing_action.upper().replace("GOTO_", "", 1)
    
    # 📊 EMIT UNIFIED SWARMHUB TELEMETRY STRIP LOG
    telemetry_span = {
        "span_id": span_id,
        "thread_id": "swarmhub-recovered-thread",
        "node_id": "retrieve",
        "latency_seconds": latency,
        "incoming_action": incoming_action.upper(),
        "outgoing_action": outgoing_action.upper(),
        "contract_status": contract_status
    }
    print(f"📊 [Telemetry Span Generated]: {json.dumps(telemetry_span)}")
    return state

def rewrite(state: AgentState) -> AgentState:
    print(f"\n--- 🟢 Entering Runtime Node: rewrite ---")
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
        print(f"    ⚠️ [Contract Breakage] Incoming schema anomaly caught at entry of rewrite: {contract_err}")
        contract_status = "FAILED_ENTRY"
    try:
        module = importlib.import_module("blobs.rewrite")
        state = module.run(state)
        if contract_status == "VERIFIED":
            try:
                SharedContextContract(**state.get("context", {}))
            except Exception as contract_err_exit:
                print(f"    ❌ [Contract Breakage] Outgoing contract violation caught at exit of rewrite: {contract_err_exit}")
                contract_status = "FAILED_EXIT"
    except Exception as e:
        print(f"    ❌ Execution/Contract Fault inside rewrite: {e}")
        contract_status = "CRASHED"
    latency = round(time.perf_counter() - start_time, 4)
    outgoing_action = state.get("next_action", "PROCEED") or "PROCEED"
    if outgoing_action.upper().startswith("GOTO_"):
        outgoing_action = outgoing_action.upper().replace("GOTO_", "", 1)
    
    # 📊 EMIT UNIFIED SWARMHUB TELEMETRY STRIP LOG
    telemetry_span = {
        "span_id": span_id,
        "thread_id": "swarmhub-recovered-thread",
        "node_id": "rewrite",
        "latency_seconds": latency,
        "incoming_action": incoming_action.upper(),
        "outgoing_action": outgoing_action.upper(),
        "contract_status": contract_status
    }
    print(f"📊 [Telemetry Span Generated]: {json.dumps(telemetry_span)}")
    return state

def generate(state: AgentState) -> AgentState:
    print(f"\n--- 🟢 Entering Runtime Node: generate ---")
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
        print(f"    ⚠️ [Contract Breakage] Incoming schema anomaly caught at entry of generate: {contract_err}")
        contract_status = "FAILED_ENTRY"
    try:
        module = importlib.import_module("blobs.generate")
        state = module.run(state)
        if contract_status == "VERIFIED":
            try:
                SharedContextContract(**state.get("context", {}))
            except Exception as contract_err_exit:
                print(f"    ❌ [Contract Breakage] Outgoing contract violation caught at exit of generate: {contract_err_exit}")
                contract_status = "FAILED_EXIT"
    except Exception as e:
        print(f"    ❌ Execution/Contract Fault inside generate: {e}")
        contract_status = "CRASHED"
    latency = round(time.perf_counter() - start_time, 4)
    outgoing_action = state.get("next_action", "PROCEED") or "PROCEED"
    if outgoing_action.upper().startswith("GOTO_"):
        outgoing_action = outgoing_action.upper().replace("GOTO_", "", 1)
    
    # 📊 EMIT UNIFIED SWARMHUB TELEMETRY STRIP LOG
    telemetry_span = {
        "span_id": span_id,
        "thread_id": "swarmhub-recovered-thread",
        "node_id": "generate",
        "latency_seconds": latency,
        "incoming_action": incoming_action.upper(),
        "outgoing_action": outgoing_action.upper(),
        "contract_status": contract_status
    }
    print(f"📊 [Telemetry Span Generated]: {json.dumps(telemetry_span)}")
    return state

def web_search(state: AgentState) -> AgentState:
    print(f"\n--- 🟢 Entering Runtime Node: web_search ---")
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
        print(f"    ⚠️ [Contract Breakage] Incoming schema anomaly caught at entry of web_search: {contract_err}")
        contract_status = "FAILED_ENTRY"
    try:
        module = importlib.import_module("blobs.web_search")
        state = module.run(state)
        if contract_status == "VERIFIED":
            try:
                SharedContextContract(**state.get("context", {}))
            except Exception as contract_err_exit:
                print(f"    ❌ [Contract Breakage] Outgoing contract violation caught at exit of web_search: {contract_err_exit}")
                contract_status = "FAILED_EXIT"
    except Exception as e:
        print(f"    ❌ Execution/Contract Fault inside web_search: {e}")
        contract_status = "CRASHED"
    latency = round(time.perf_counter() - start_time, 4)
    outgoing_action = state.get("next_action", "PROCEED") or "PROCEED"
    if outgoing_action.upper().startswith("GOTO_"):
        outgoing_action = outgoing_action.upper().replace("GOTO_", "", 1)
    
    # 📊 EMIT UNIFIED SWARMHUB TELEMETRY STRIP LOG
    telemetry_span = {
        "span_id": span_id,
        "thread_id": "swarmhub-recovered-thread",
        "node_id": "web_search",
        "latency_seconds": latency,
        "incoming_action": incoming_action.upper(),
        "outgoing_action": outgoing_action.upper(),
        "contract_status": contract_status
    }
    print(f"📊 [Telemetry Span Generated]: {json.dumps(telemetry_span)}")
    return state

def retrieve(state: AgentState) -> AgentState:
    print(f"\n--- 🟢 Entering Runtime Node: retrieve ---")
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
        print(f"    ⚠️ [Contract Breakage] Incoming schema anomaly caught at entry of retrieve: {contract_err}")
        contract_status = "FAILED_ENTRY"
    try:
        module = importlib.import_module("blobs.retrieve")
        state = module.run(state)
        if contract_status == "VERIFIED":
            try:
                SharedContextContract(**state.get("context", {}))
            except Exception as contract_err_exit:
                print(f"    ❌ [Contract Breakage] Outgoing contract violation caught at exit of retrieve: {contract_err_exit}")
                contract_status = "FAILED_EXIT"
    except Exception as e:
        print(f"    ❌ Execution/Contract Fault inside retrieve: {e}")
        contract_status = "CRASHED"
    latency = round(time.perf_counter() - start_time, 4)
    outgoing_action = state.get("next_action", "PROCEED") or "PROCEED"
    if outgoing_action.upper().startswith("GOTO_"):
        outgoing_action = outgoing_action.upper().replace("GOTO_", "", 1)
    
    # 📊 EMIT UNIFIED SWARMHUB TELEMETRY STRIP LOG
    telemetry_span = {
        "span_id": span_id,
        "thread_id": "swarmhub-recovered-thread",
        "node_id": "retrieve",
        "latency_seconds": latency,
        "incoming_action": incoming_action.upper(),
        "outgoing_action": outgoing_action.upper(),
        "contract_status": contract_status
    }
    print(f"📊 [Telemetry Span Generated]: {json.dumps(telemetry_span)}")
    return state

def grade_documents(state: AgentState) -> AgentState:
    print(f"\n--- 🟢 Entering Runtime Node: grade_documents ---")
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
        print(f"    ⚠️ [Contract Breakage] Incoming schema anomaly caught at entry of grade_documents: {contract_err}")
        contract_status = "FAILED_ENTRY"
    try:
        module = importlib.import_module("blobs.grade_documents")
        state = module.run(state)
        if contract_status == "VERIFIED":
            try:
                SharedContextContract(**state.get("context", {}))
            except Exception as contract_err_exit:
                print(f"    ❌ [Contract Breakage] Outgoing contract violation caught at exit of grade_documents: {contract_err_exit}")
                contract_status = "FAILED_EXIT"
    except Exception as e:
        print(f"    ❌ Execution/Contract Fault inside grade_documents: {e}")
        contract_status = "CRASHED"
    latency = round(time.perf_counter() - start_time, 4)
    outgoing_action = state.get("next_action", "PROCEED") or "PROCEED"
    if outgoing_action.upper().startswith("GOTO_"):
        outgoing_action = outgoing_action.upper().replace("GOTO_", "", 1)
    
    # 📊 EMIT UNIFIED SWARMHUB TELEMETRY STRIP LOG
    telemetry_span = {
        "span_id": span_id,
        "thread_id": "swarmhub-recovered-thread",
        "node_id": "grade_documents",
        "latency_seconds": latency,
        "incoming_action": incoming_action.upper(),
        "outgoing_action": outgoing_action.upper(),
        "contract_status": contract_status
    }
    print(f"📊 [Telemetry Span Generated]: {json.dumps(telemetry_span)}")
    state["next_action"] = "END"
    return state

def generate(state: AgentState) -> AgentState:
    print(f"\n--- 🟢 Entering Runtime Node: generate ---")
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
        print(f"    ⚠️ [Contract Breakage] Incoming schema anomaly caught at entry of generate: {contract_err}")
        contract_status = "FAILED_ENTRY"
    try:
        module = importlib.import_module("blobs.generate")
        state = module.run(state)
        if contract_status == "VERIFIED":
            try:
                SharedContextContract(**state.get("context", {}))
            except Exception as contract_err_exit:
                print(f"    ❌ [Contract Breakage] Outgoing contract violation caught at exit of generate: {contract_err_exit}")
                contract_status = "FAILED_EXIT"
    except Exception as e:
        print(f"    ❌ Execution/Contract Fault inside generate: {e}")
        contract_status = "CRASHED"
    latency = round(time.perf_counter() - start_time, 4)
    outgoing_action = state.get("next_action", "PROCEED") or "PROCEED"
    if outgoing_action.upper().startswith("GOTO_"):
        outgoing_action = outgoing_action.upper().replace("GOTO_", "", 1)
    
    # 📊 EMIT UNIFIED SWARMHUB TELEMETRY STRIP LOG
    telemetry_span = {
        "span_id": span_id,
        "thread_id": "swarmhub-recovered-thread",
        "node_id": "generate",
        "latency_seconds": latency,
        "incoming_action": incoming_action.upper(),
        "outgoing_action": outgoing_action.upper(),
        "contract_status": contract_status
    }
    print(f"📊 [Telemetry Span Generated]: {json.dumps(telemetry_span)}")
    return state

def llm_fallback(state: AgentState) -> AgentState:
    print(f"\n--- 🟢 Entering Runtime Node: llm_fallback ---")
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
        print(f"    ⚠️ [Contract Breakage] Incoming schema anomaly caught at entry of llm_fallback: {contract_err}")
        contract_status = "FAILED_ENTRY"
    try:
        module = importlib.import_module("blobs.llm_fallback")
        state = module.run(state)
        if contract_status == "VERIFIED":
            try:
                SharedContextContract(**state.get("context", {}))
            except Exception as contract_err_exit:
                print(f"    ❌ [Contract Breakage] Outgoing contract violation caught at exit of llm_fallback: {contract_err_exit}")
                contract_status = "FAILED_EXIT"
    except Exception as e:
        print(f"    ❌ Execution/Contract Fault inside llm_fallback: {e}")
        contract_status = "CRASHED"
    latency = round(time.perf_counter() - start_time, 4)
    outgoing_action = state.get("next_action", "PROCEED") or "PROCEED"
    if outgoing_action.upper().startswith("GOTO_"):
        outgoing_action = outgoing_action.upper().replace("GOTO_", "", 1)
    
    # 📊 EMIT UNIFIED SWARMHUB TELEMETRY STRIP LOG
    telemetry_span = {
        "span_id": span_id,
        "thread_id": "swarmhub-recovered-thread",
        "node_id": "llm_fallback",
        "latency_seconds": latency,
        "incoming_action": incoming_action.upper(),
        "outgoing_action": outgoing_action.upper(),
        "contract_status": contract_status
    }
    print(f"📊 [Telemetry Span Generated]: {json.dumps(telemetry_span)}")
    return state

# 6. Build the workflow graph structural topology
workflow = StateGraph(AgentState)

workflow.add_node("retrieve", retrieve)
workflow.add_node("grade_documents", grade_documents)
workflow.add_node("generate", generate)
workflow.add_node("transform_query", transform_query)
workflow.add_node("retrieve", retrieve)
workflow.add_node("grade_documents", grade_documents)
workflow.add_node("generate", generate)
workflow.add_node("transform_query", transform_query)
workflow.add_node("web_search", web_search)
workflow.add_node("retrieve", retrieve)
workflow.add_node("grade_documents", grade_documents)
workflow.add_node("generate", generate)
workflow.add_node("transform_query", transform_query)
workflow.add_node("retrieve", retrieve)
workflow.add_node("grade_documents", grade_documents)
workflow.add_node("generate", generate)
workflow.add_node("transform_query", transform_query)
workflow.add_node("retrieve", retrieve)
workflow.add_node("grade_documents", grade_documents)
workflow.add_node("generate", generate)
workflow.add_node("web_search", web_search)
workflow.add_node("retrieve", retrieve)
workflow.add_node("grade_documents", grade_documents)
workflow.add_node("generate", generate)
workflow.add_node("transform_query", transform_query)
workflow.add_node("web_search_node", web_search_node)
workflow.add_node("web_search", web_search)
workflow.add_node("retrieve", retrieve)
workflow.add_node("grade_documents", grade_documents)
workflow.add_node("generate", generate)
workflow.add_node("transform_query", transform_query)
workflow.add_node("agent", agent)
workflow.add_node("retrieve", retrieve)
workflow.add_node("rewrite", rewrite)
workflow.add_node("generate", generate)
workflow.add_node("web_search", web_search)
workflow.add_node("retrieve", retrieve)
workflow.add_node("grade_documents", grade_documents)
workflow.add_node("generate", generate)
workflow.add_node("llm_fallback", llm_fallback)

workflow.add_edge(START, "agent")

# Symmetrical routing normalizer to resolve action tokens dynamically
def route_normalizer(state: AgentState) -> str:
    action = state.get("next_action", "END").upper()
    if not action.startswith("GOTO_") and action != "END":
        return f"GOTO_{action}"
    return action

# Define routing conditions rules
workflow.add_conditional_edges(
    "retrieve",
    route_normalizer,
    {
        "GOTO_GRADE_DOCUMENTS": "grade_documents",
        "GOTO_GRADE_DOCUMENTS": "grade_documents",
        "GOTO_GRADE_DOCUMENTS": "grade_documents",
        "GOTO_GRADE_DOCUMENTS": "grade_documents",
        "GOTO_GRADE_DOCUMENTS": "grade_documents",
        "GOTO_GRADE_DOCUMENTS": "grade_documents",
        "GOTO_GRADE_DOCUMENTS": "grade_documents",
        "GOTO_GRADE_DOCUMENTS": "grade_documents",
        "GOTO_END": END,
        "END": END
    }
)
workflow.add_edge("grade_documents", END)
workflow.add_conditional_edges(
    "generate",
    route_normalizer,
    {
        "GOTO_END": "END",
        "GOTO_END": "END",
        "GOTO_END": "END",
        "GOTO_END": END,
        "END": END
    }
)
workflow.add_conditional_edges(
    "transform_query",
    route_normalizer,
    {
        "GOTO_RETRIEVE": "retrieve",
        "GOTO_RETRIEVE": "retrieve",
        "GOTO_RETRIEVE": "retrieve",
        "GOTO_RETRIEVE": "retrieve",
        "GOTO_WEB_SEARCH_NODE": "web_search_node",
        "GOTO_RETRIEVE": "retrieve",
        "GOTO_END": END,
        "END": END
    }
)
workflow.add_conditional_edges(
    "retrieve",
    route_normalizer,
    {
        "GOTO_GRADE_DOCUMENTS": "grade_documents",
        "GOTO_GRADE_DOCUMENTS": "grade_documents",
        "GOTO_GRADE_DOCUMENTS": "grade_documents",
        "GOTO_GRADE_DOCUMENTS": "grade_documents",
        "GOTO_GRADE_DOCUMENTS": "grade_documents",
        "GOTO_GRADE_DOCUMENTS": "grade_documents",
        "GOTO_GRADE_DOCUMENTS": "grade_documents",
        "GOTO_GRADE_DOCUMENTS": "grade_documents",
        "GOTO_END": END,
        "END": END
    }
)
workflow.add_edge("grade_documents", END)
workflow.add_conditional_edges(
    "generate",
    route_normalizer,
    {
        "GOTO_END": "END",
        "GOTO_END": "END",
        "GOTO_END": "END",
        "GOTO_END": END,
        "END": END
    }
)
workflow.add_conditional_edges(
    "transform_query",
    route_normalizer,
    {
        "GOTO_RETRIEVE": "retrieve",
        "GOTO_RETRIEVE": "retrieve",
        "GOTO_RETRIEVE": "retrieve",
        "GOTO_RETRIEVE": "retrieve",
        "GOTO_WEB_SEARCH_NODE": "web_search_node",
        "GOTO_RETRIEVE": "retrieve",
        "GOTO_END": END,
        "END": END
    }
)
workflow.add_conditional_edges(
    "web_search",
    route_normalizer,
    {
        "GOTO_GENERATE": "generate",
        "GOTO_GENERATE": "generate",
        "GOTO_GENERATE": "generate",
        "GOTO_GENERATE": "generate",
        "GOTO_END": END,
        "END": END
    }
)
workflow.add_conditional_edges(
    "retrieve",
    route_normalizer,
    {
        "GOTO_GRADE_DOCUMENTS": "grade_documents",
        "GOTO_GRADE_DOCUMENTS": "grade_documents",
        "GOTO_GRADE_DOCUMENTS": "grade_documents",
        "GOTO_GRADE_DOCUMENTS": "grade_documents",
        "GOTO_GRADE_DOCUMENTS": "grade_documents",
        "GOTO_GRADE_DOCUMENTS": "grade_documents",
        "GOTO_GRADE_DOCUMENTS": "grade_documents",
        "GOTO_GRADE_DOCUMENTS": "grade_documents",
        "GOTO_END": END,
        "END": END
    }
)
workflow.add_edge("grade_documents", END)
workflow.add_conditional_edges(
    "generate",
    route_normalizer,
    {
        "GOTO_END": "END",
        "GOTO_END": "END",
        "GOTO_END": "END",
        "GOTO_END": END,
        "END": END
    }
)
workflow.add_conditional_edges(
    "transform_query",
    route_normalizer,
    {
        "GOTO_RETRIEVE": "retrieve",
        "GOTO_RETRIEVE": "retrieve",
        "GOTO_RETRIEVE": "retrieve",
        "GOTO_RETRIEVE": "retrieve",
        "GOTO_WEB_SEARCH_NODE": "web_search_node",
        "GOTO_RETRIEVE": "retrieve",
        "GOTO_END": END,
        "END": END
    }
)
workflow.add_conditional_edges(
    "retrieve",
    route_normalizer,
    {
        "GOTO_GRADE_DOCUMENTS": "grade_documents",
        "GOTO_GRADE_DOCUMENTS": "grade_documents",
        "GOTO_GRADE_DOCUMENTS": "grade_documents",
        "GOTO_GRADE_DOCUMENTS": "grade_documents",
        "GOTO_GRADE_DOCUMENTS": "grade_documents",
        "GOTO_GRADE_DOCUMENTS": "grade_documents",
        "GOTO_GRADE_DOCUMENTS": "grade_documents",
        "GOTO_GRADE_DOCUMENTS": "grade_documents",
        "GOTO_END": END,
        "END": END
    }
)
workflow.add_edge("grade_documents", END)
workflow.add_conditional_edges(
    "generate",
    route_normalizer,
    {
        "GOTO_END": "END",
        "GOTO_END": "END",
        "GOTO_END": "END",
        "GOTO_END": END,
        "END": END
    }
)
workflow.add_conditional_edges(
    "transform_query",
    route_normalizer,
    {
        "GOTO_RETRIEVE": "retrieve",
        "GOTO_RETRIEVE": "retrieve",
        "GOTO_RETRIEVE": "retrieve",
        "GOTO_RETRIEVE": "retrieve",
        "GOTO_WEB_SEARCH_NODE": "web_search_node",
        "GOTO_RETRIEVE": "retrieve",
        "GOTO_END": END,
        "END": END
    }
)
workflow.add_conditional_edges(
    "retrieve",
    route_normalizer,
    {
        "GOTO_GRADE_DOCUMENTS": "grade_documents",
        "GOTO_GRADE_DOCUMENTS": "grade_documents",
        "GOTO_GRADE_DOCUMENTS": "grade_documents",
        "GOTO_GRADE_DOCUMENTS": "grade_documents",
        "GOTO_GRADE_DOCUMENTS": "grade_documents",
        "GOTO_GRADE_DOCUMENTS": "grade_documents",
        "GOTO_GRADE_DOCUMENTS": "grade_documents",
        "GOTO_GRADE_DOCUMENTS": "grade_documents",
        "GOTO_END": END,
        "END": END
    }
)
workflow.add_edge("grade_documents", END)
workflow.add_conditional_edges(
    "generate",
    route_normalizer,
    {
        "GOTO_END": "END",
        "GOTO_END": "END",
        "GOTO_END": "END",
        "GOTO_END": END,
        "END": END
    }
)
workflow.add_conditional_edges(
    "web_search",
    route_normalizer,
    {
        "GOTO_GENERATE": "generate",
        "GOTO_GENERATE": "generate",
        "GOTO_GENERATE": "generate",
        "GOTO_GENERATE": "generate",
        "GOTO_END": END,
        "END": END
    }
)
workflow.add_conditional_edges(
    "retrieve",
    route_normalizer,
    {
        "GOTO_GRADE_DOCUMENTS": "grade_documents",
        "GOTO_GRADE_DOCUMENTS": "grade_documents",
        "GOTO_GRADE_DOCUMENTS": "grade_documents",
        "GOTO_GRADE_DOCUMENTS": "grade_documents",
        "GOTO_GRADE_DOCUMENTS": "grade_documents",
        "GOTO_GRADE_DOCUMENTS": "grade_documents",
        "GOTO_GRADE_DOCUMENTS": "grade_documents",
        "GOTO_GRADE_DOCUMENTS": "grade_documents",
        "GOTO_END": END,
        "END": END
    }
)
workflow.add_edge("grade_documents", END)
workflow.add_conditional_edges(
    "generate",
    route_normalizer,
    {
        "GOTO_END": "END",
        "GOTO_END": "END",
        "GOTO_END": "END",
        "GOTO_END": END,
        "END": END
    }
)
workflow.add_conditional_edges(
    "transform_query",
    route_normalizer,
    {
        "GOTO_RETRIEVE": "retrieve",
        "GOTO_RETRIEVE": "retrieve",
        "GOTO_RETRIEVE": "retrieve",
        "GOTO_RETRIEVE": "retrieve",
        "GOTO_WEB_SEARCH_NODE": "web_search_node",
        "GOTO_RETRIEVE": "retrieve",
        "GOTO_END": END,
        "END": END
    }
)
workflow.add_conditional_edges(
    "web_search_node",
    route_normalizer,
    {
        "GOTO_GENERATE": "generate",
        "GOTO_END": END,
        "END": END
    }
)
workflow.add_conditional_edges(
    "web_search",
    route_normalizer,
    {
        "GOTO_GENERATE": "generate",
        "GOTO_GENERATE": "generate",
        "GOTO_GENERATE": "generate",
        "GOTO_GENERATE": "generate",
        "GOTO_END": END,
        "END": END
    }
)
workflow.add_conditional_edges(
    "retrieve",
    route_normalizer,
    {
        "GOTO_GRADE_DOCUMENTS": "grade_documents",
        "GOTO_GRADE_DOCUMENTS": "grade_documents",
        "GOTO_GRADE_DOCUMENTS": "grade_documents",
        "GOTO_GRADE_DOCUMENTS": "grade_documents",
        "GOTO_GRADE_DOCUMENTS": "grade_documents",
        "GOTO_GRADE_DOCUMENTS": "grade_documents",
        "GOTO_GRADE_DOCUMENTS": "grade_documents",
        "GOTO_GRADE_DOCUMENTS": "grade_documents",
        "GOTO_END": END,
        "END": END
    }
)
workflow.add_edge("grade_documents", END)
workflow.add_conditional_edges(
    "generate",
    route_normalizer,
    {
        "GOTO_END": "END",
        "GOTO_END": "END",
        "GOTO_END": "END",
        "GOTO_END": END,
        "END": END
    }
)
workflow.add_conditional_edges(
    "transform_query",
    route_normalizer,
    {
        "GOTO_RETRIEVE": "retrieve",
        "GOTO_RETRIEVE": "retrieve",
        "GOTO_RETRIEVE": "retrieve",
        "GOTO_RETRIEVE": "retrieve",
        "GOTO_WEB_SEARCH_NODE": "web_search_node",
        "GOTO_RETRIEVE": "retrieve",
        "GOTO_END": END,
        "END": END
    }
)
workflow.add_edge("agent", END)
workflow.add_conditional_edges(
    "retrieve",
    route_normalizer,
    {
        "GOTO_GRADE_DOCUMENTS": "grade_documents",
        "GOTO_GRADE_DOCUMENTS": "grade_documents",
        "GOTO_GRADE_DOCUMENTS": "grade_documents",
        "GOTO_GRADE_DOCUMENTS": "grade_documents",
        "GOTO_GRADE_DOCUMENTS": "grade_documents",
        "GOTO_GRADE_DOCUMENTS": "grade_documents",
        "GOTO_GRADE_DOCUMENTS": "grade_documents",
        "GOTO_GRADE_DOCUMENTS": "grade_documents",
        "GOTO_END": END,
        "END": END
    }
)
workflow.add_conditional_edges(
    "rewrite",
    route_normalizer,
    {
        "GOTO_AGENT": "agent",
        "GOTO_END": END,
        "END": END
    }
)
workflow.add_conditional_edges(
    "generate",
    route_normalizer,
    {
        "GOTO_END": "END",
        "GOTO_END": "END",
        "GOTO_END": "END",
        "GOTO_END": END,
        "END": END
    }
)
workflow.add_conditional_edges(
    "web_search",
    route_normalizer,
    {
        "GOTO_GENERATE": "generate",
        "GOTO_GENERATE": "generate",
        "GOTO_GENERATE": "generate",
        "GOTO_GENERATE": "generate",
        "GOTO_END": END,
        "END": END
    }
)
workflow.add_conditional_edges(
    "retrieve",
    route_normalizer,
    {
        "GOTO_GRADE_DOCUMENTS": "grade_documents",
        "GOTO_GRADE_DOCUMENTS": "grade_documents",
        "GOTO_GRADE_DOCUMENTS": "grade_documents",
        "GOTO_GRADE_DOCUMENTS": "grade_documents",
        "GOTO_GRADE_DOCUMENTS": "grade_documents",
        "GOTO_GRADE_DOCUMENTS": "grade_documents",
        "GOTO_GRADE_DOCUMENTS": "grade_documents",
        "GOTO_GRADE_DOCUMENTS": "grade_documents",
        "GOTO_END": END,
        "END": END
    }
)
workflow.add_edge("grade_documents", END)
workflow.add_conditional_edges(
    "generate",
    route_normalizer,
    {
        "GOTO_END": "END",
        "GOTO_END": "END",
        "GOTO_END": "END",
        "GOTO_END": END,
        "END": END
    }
)
workflow.add_conditional_edges(
    "llm_fallback",
    route_normalizer,
    {
        "GOTO_END": "END",
        "GOTO_END": END,
        "END": END
    }
)

# 6.5 Mount Checkpointer System Instance
memory_saver = MemorySaver()

# 7. Compile the graph execution app binary with active checkpointer
app = workflow.compile(checkpointer=memory_saver)

if __name__ == "__main__":
    print("🚀 Running compiled SwarmHub execution pipeline validation...")
    initial_state = {"messages": [], "context": {}, "next_action": ""}
    execution_config = {"configurable": {"thread_id": "swarmhub-recovered-thread"}}
    final_output = app.invoke(initial_state, config=execution_config)
    print("\n🏁 Workflow Execution Successfully Finished!")
    print("Final State Context Payload:", final_output["context"])