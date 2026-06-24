# ==========================================================================
# GENERATED AUTOMATICALLY BY SWARMHUB FOR AGENT SWARM: crewai-game-builder-crew
# TARGET RUNTIME: PydanticAI (Memory Layer: in_memory | Thread: swarmhub-default-thread)
# ==========================================================================

import importlib
import os
import sys
import sqlite3
import json
import time
import uuid
from pydantic import BaseModel, Field
# === SWARMHUB METADATA SOURCE MAP (LOSSLESS ROUND-TRIP ASSURANCE) ===
# SWARMHUB_METADATA_START
# {
#   "version": "agentic.io/v1alpha1",
#   "kind": "UniversalAgent",
#   "name": "crewai-game-builder-crew",
#   "runtime": {
#     "provider": "unknown_crew_imported",
#     "model": "unknown_crew_imported",
#     "temperature": 0.2,
#     "max_tokens": null
#   },
#   "memory": {
#     "storage_backend": "in_memory",
#     "thread_id": null,
#     "connection_string": null
#   },
#   "system_prompt": "Extracted sequentially from legacy CrewAI manifest.",
#   "interfaces": [],
#   "state_schema": {},
#   "topology": {
#     "type": "Sequential",
#     "initial_node": "unknown_start",
#     "nodes": [
#       {
#         "id": "unknown_start",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/unknown_start.py",
#         "transitions": [],
#         "tools": [],
#         "interfaces": []
#       }
#     ]
#   }
# }
# SWARMHUB_METADATA_END

from pydantic_ai import Agent, RunContext

# 1. Patch Runtime Environment Paths to discover localized Code Blobs
sys.path.insert(0, os.getcwd())

# 2. Initialize Global Runtime Configurations
# Target Model Provider Coordinate: unknown_crew_imported:unknown_crew_imported

# 3. Define functional stubs for cross-compiled tools
# No external tool dependencies declared in universal spec topology.

# 3.2 Initialize Registered Global MCP Capability Interface Targets
GLOBAL_INTERFACES_REGISTRY = {}

# 4. Define strict Data Contract Verification Model schemas
class SharedContextContract(BaseModel):
    pass

# 5. Define Autonomous PydanticAI Agents dynamically from Topology
unknown_start_agent = Agent(
    "unknown_crew_imported:unknown_crew_imported",
    system_prompt="Extracted sequentially from legacy CrewAI manifest. Node context: unknown_start. Authorized MCP Interfaces: []",
)

# 6. Assemble the State-Machine Execution Architecture Runtime Maps
if __name__ == "__main__":
    print("🚀 Running compiled SwarmHub execution pipeline validation...")
    print("⚠️ [Mode: Local Offline Execution] PydanticAI state-machine verification pass ignited.\n")
    initial_state_context = {}
    if "row" in locals() and row:
        state = json.loads(row[0])
    else:
        state = {
            "messages": [],
            "context": initial_state_context,
            "next_action": "PROCEED"
        }

    NODES_REGISTRY = {
        "unknown_start": unknown_start_agent,
    }
    NODES_PIPELINE_MAP = {
        "unknown_start": importlib.import_module("blobs.unknown_start").run,
    }

    ROUTING_TABLE = {
        "unknown_start": {
            "END": "END"
        },
    }

    current_node = "unknown_start"
    incoming_action = "INITIAL_ENTRY"
    while current_node and current_node != "END":
        agent_instance = NODES_REGISTRY.get(current_node)
        node_executor = NODES_PIPELINE_MAP.get(current_node)
        if not agent_instance or not node_executor:
            break
        print(f"\n--- 🟢 Entering PydanticAI Core Node: {current_node} ---")
        
        span_id = f"span-{uuid.uuid4().hex[:8]}"
        contract_status = "VERIFIED"
        start_time = time.perf_counter()
        
        try:
            SharedContextContract(**state["context"])
        except Exception as contract_err:
            print(f"    ⚠️ [Contract Breakage] Incoming schema anomaly caught at entry of {current_node}: {contract_err}")
            contract_status = "FAILED_ENTRY"
        
        try:
            # Execute the node context mutation pass through the runtime executor hook
            state = node_executor(state)
            
            if contract_status == "VERIFIED":
                try:
                    SharedContextContract(**state["context"])
                except Exception as contract_err_exit:
                    print(f"    ❌ [Contract Breakage] Outgoing contract violation caught at exit of {current_node}: {contract_err_exit}")
                    contract_status = "FAILED_EXIT"
        except Exception as e:
            print(f"    ❌ Execution/Contract Fault inside node [{current_node}]: {e}")
            contract_status = "CRASHED"
            break
        
        latency = round(time.perf_counter() - start_time, 4)
        action = state.get("next_action", "PROCEED").upper()
        if action.startswith("GOTO_"):
            action = action.replace("GOTO_", "", 1)
        
        # 📊 EMIT UNIFIED SWARMHUB TELEMETRY STRIP LOG
        telemetry_span = {
            "span_id": span_id,
            "thread_id": "swarmhub-default-thread",
            "node_id": current_node,
            "latency_seconds": latency,
            "incoming_action": incoming_action,
            "outgoing_action": action,
            "contract_status": contract_status
        }
        print(f"📊 [Telemetry Span Generated]: {json.dumps(telemetry_span)}")
        
        incoming_action = action
        current_node = ROUTING_TABLE.get(current_node, {}).get(action, "END")

    print("\n🏁 PydanticAI Task Step Loop Pipeline Successfully Executed!")
    print("Final Verified State Context Payload:", state["context"])