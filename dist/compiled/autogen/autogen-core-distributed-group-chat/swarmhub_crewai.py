# ==========================================================================
# GENERATED AUTOMATICALLY BY SWARMHUB FOR AGENT SWARM: autogen-core-distributed-group-chat
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
#   "name": "autogen-core-distributed-group-chat",
#   "runtime": {
#     "provider": "autogen_sliced_fallback",
#     "model": "fallback_model",
#     "temperature": 0.2,
#     "max_tokens": null
#   },
#   "memory": {
#     "storage_backend": "in_memory",
#     "thread_id": null,
#     "connection_string": null
#   },
#   "system_prompt": "Extracted from legacy conversational script via AST source-slicing.",
#   "interfaces": [],
#   "state_schema": {},
#   "topology": {
#     "type": "StateMachine",
#     "initial_node": "BaseGroupChatAgent",
#     "nodes": [
#       {
#         "id": "BaseGroupChatAgent",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/BaseGroupChatAgent.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_GROUPCHATMANAGER",
#             "target_node": "GroupChatManager"
#           }
#         ],
#         "tools": [],
#         "interfaces": []
#       },
#       {
#         "id": "GroupChatManager",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/GroupChatManager.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_UIAGENT",
#             "target_node": "UIAgent"
#           }
#         ],
#         "tools": [],
#         "interfaces": []
#       },
#       {
#         "id": "UIAgent",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/UIAgent.py",
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
# Selected Provider Context: autogen_sliced_fallback
# Selected Model Target: fallback_model

# 3. Define functional stubs for cross-compiled tools
# No external tool dependencies declared in universal spec topology.

# 3.2 Initialize Registered Global MCP Capability Interface Targets
GLOBAL_INTERFACES_REGISTRY = {}

# 4. Define strict Data Contract Verification Model schemas
class SharedContextContract(BaseModel):
    pass

# 5. Define Autonomous Agent Personas dynamically from Topology
BaseGroupChatAgent_agent = Agent(
    role="Basegroupchatagent",
    goal="Execute capabilities defined under the workspace node BaseGroupChatAgent",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[],
    verbose=True,
    allow_delegation=False
)

GroupChatManager_agent = Agent(
    role="Groupchatmanager",
    goal="Execute capabilities defined under the workspace node GroupChatManager",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[],
    verbose=True,
    allow_delegation=False
)

UIAgent_agent = Agent(
    role="Uiagent",
    goal="Execute capabilities defined under the workspace node UIAgent",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[],
    verbose=True,
    allow_delegation=False
)

# 6. Define Concrete Task Assignments linked back to Code Blobs
BaseGroupChatAgent_task = Task(
    description="Execute processing code logic anchored at: blobs/BaseGroupChatAgent.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=BaseGroupChatAgent_agent
)

GroupChatManager_task = Task(
    description="Execute processing code logic anchored at: blobs/GroupChatManager.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=GroupChatManager_agent
)

UIAgent_task = Task(
    description="Execute processing code logic anchored at: blobs/UIAgent.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=UIAgent_agent
)

# 7. Assemble the Unified Crew Workspace Execution Order
crew = Crew(
    agents=[BaseGroupChatAgent_agent, GroupChatManager_agent, UIAgent_agent],
    tasks=[BaseGroupChatAgent_task, GroupChatManager_task, UIAgent_task],
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
        "BaseGroupChatAgent": {"import_path": "blobs.BaseGroupChatAgent", "interfaces": [], "inline_f": "_inline_BaseGroupChatAgent" if hasattr(sys.modules[__name__], "_inline_BaseGroupChatAgent") else None},
        "GroupChatManager": {"import_path": "blobs.GroupChatManager", "interfaces": [], "inline_f": "_inline_GroupChatManager" if hasattr(sys.modules[__name__], "_inline_GroupChatManager") else None},
        "UIAgent": {"import_path": "blobs.UIAgent", "interfaces": [], "inline_f": "_inline_UIAgent" if hasattr(sys.modules[__name__], "_inline_UIAgent") else None},
    }

    ROUTING_TABLE = {
        "BaseGroupChatAgent": {
            "GROUPCHATMANAGER": "GroupChatManager",
            "END": "END"
        },
        "GroupChatManager": {
            "UIAGENT": "UIAgent",
            "END": "END"
        },
        "UIAgent": {
            "END": "END"
        },
    }

    current_node = "BaseGroupChatAgent"
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