# ==========================================================================
# GENERATED AUTOMATICALLY BY SWARMHUB FOR AGENT SWARM: 12-travel-planner-agent
# TARGET RUNTIME: CrewAI (Memory Layer: in_memory | Thread: swarmhub-default-thread)
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
#   "name": "12-travel-planner-agent",
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
#     "initial_node": "research",
#     "nodes": [
#       {
#         "id": "research",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/research.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_PLANNING",
#             "target_node": "planning"
#           }
#         ],
#         "tools": [],
#         "interfaces": []
#       },
#       {
#         "id": "planning",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/planning.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_BUDGET",
#             "target_node": "budget"
#           }
#         ],
#         "tools": [],
#         "interfaces": []
#       },
#       {
#         "id": "budget",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/budget.py",
#         "transitions": [],
#         "tools": [],
#         "interfaces": []
#       }
#     ]
#   }
# }
# SWARMHUB_METADATA_END

from crewai import Agent, Task, Crew, Process
from crewai.tools import tool

# 1. Patch Runtime Environment Paths to discover localized Code Blobs
sys.path.insert(0, os.getcwd())

# 2. Initialize Global Runtime Configurations
# Selected Provider Context: unknown_crew_imported
# Selected Model Target: unknown_crew_imported

# 3. Define functional stubs for cross-compiled tools
# No external tool dependencies declared in universal spec topology.

# 3.2 Initialize Registered Global MCP Capability Interface Targets
GLOBAL_INTERFACES_REGISTRY = {}

# 4. Define strict Data Contract Verification Model schemas
class SharedContextContract(BaseModel):
    pass

# 5. Define Autonomous Agent Personas dynamically from Topology
research_agent = Agent(
    role="Research",
    goal="Execute capabilities defined under the workspace node research",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[],
    verbose=True,
    allow_delegation=False
)

planning_agent = Agent(
    role="Planning",
    goal="Execute capabilities defined under the workspace node planning",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[],
    verbose=True,
    allow_delegation=False
)

budget_agent = Agent(
    role="Budget",
    goal="Execute capabilities defined under the workspace node budget",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[],
    verbose=True,
    allow_delegation=False
)

# 6. Define Concrete Task Assignments linked back to Code Blobs
research_task = Task(
    description="Execute processing code logic anchored at: blobs/research.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=research_agent
)

planning_task = Task(
    description="Execute processing code logic anchored at: blobs/planning.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=planning_agent
)

budget_task = Task(
    description="Execute processing code logic anchored at: blobs/budget.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=budget_agent
)

# 7. Assemble the Unified Crew Workspace Execution Order
crew = Crew(
    agents=[research_agent, planning_agent, budget_agent],
    tasks=[research_task, planning_task, budget_task],
    process=Process.sequential,
    verbose=True
)

# 8. Execution and Localized Blob Verification Pipeline
if __name__ == "__main__":
    print("🚀 Running compiled SwarmHub execution pipeline validation...")
    print("⚠️ [Mode: Local Offline Execution] State-Machine verification pass ignited.\n")
    default_state = {"messages": [], "context": {}, "next_action": ""}
    state = default_state

    # Target framework execution state-machine routing configuration maps
    NODES_CONFIG = {
        "research": {"import_path": "blobs.research", "interfaces": [], "inline_f": "_inline_research" if hasattr(sys.modules[__name__], "_inline_research") else None},
        "planning": {"import_path": "blobs.planning", "interfaces": [], "inline_f": "_inline_planning" if hasattr(sys.modules[__name__], "_inline_planning") else None},
        "budget": {"import_path": "blobs.budget", "interfaces": [], "inline_f": "_inline_budget" if hasattr(sys.modules[__name__], "_inline_budget") else None},
    }

    ROUTING_TABLE = {
        "research": {
            "PLANNING": "planning",
            "END": "END"
        },
        "planning": {
            "BUDGET": "budget",
            "END": "END"
        },
        "budget": {
            "END": "END"
        },
    }

    current_node = "research"
    incoming_action = "INITIAL_ENTRY"
    while current_node and current_node != "END":
        cfg = NODES_CONFIG.get(current_node)
        if not cfg:
            break
        print(f"\n--- 🟢 Entering Runtime Task Node: {current_node} ---")
        print(f"    🔒 [Permissions] Authorized MCP Interfaces: {cfg['interfaces']}")
        
        span_id = f"span-{uuid.uuid4().hex[:8]}"
        contract_status = "VERIFIED"
        start_time = time.perf_counter()
        
        try:
            SharedContextContract(**state["context"])
        except Exception as contract_err:
            print(f"    ⚠️ [Contract Breakage] Incoming schema anomaly caught at entry of {current_node}: {contract_err}")
            contract_status = "FAILED_ENTRY"
        
        try:
            if cfg["inline_f"] and cfg["inline_f"] in globals():
                state = globals()[cfg["inline_f"]](state)
            else:
                module = importlib.import_module(cfg["import_path"])
                state = module.run(state)
            
            if contract_status == "VERIFIED":
                try:
                    SharedContextContract(**state["context"])
                except Exception as contract_err_exit:
                    print(f"    ❌ [Contract Breakage] Outgoing contract violation caught at exit of {current_node}: {contract_err_exit}")
                    contract_status = "FAILED_EXIT"
        except Exception as e:
            print(f"    ❌ Execution/Contract Fault inside {current_node}: {e}")
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

    print("\n🏁 Local CrewAI Task Blob Pipeline Successfully Executed!")
    print("Final Verified State Context Payload:", state["context"])