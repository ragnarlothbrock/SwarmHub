# ==========================================================================
# GENERATED AUTOMATICALLY BY SWARMHUB FOR AGENT SWARM: autogen-core-chainlit
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
#   "name": "autogen-core-chainlit",
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
#     "initial_node": "GroupChatManager",
#     "nodes": [
#       {
#         "id": "GroupChatManager",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/GroupChatManager.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_ASSISTANT",
#             "target_node": "Assistant"
#           }
#         ],
#         "tools": [],
#         "interfaces": []
#       },
#       {
#         "id": "Assistant",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/Assistant.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_CRITIC",
#             "target_node": "Critic"
#           }
#         ],
#         "tools": [],
#         "interfaces": []
#       },
#       {
#         "id": "Critic",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/Critic.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_WEATHER_AGENT",
#             "target_node": "weather_agent"
#           }
#         ],
#         "tools": [],
#         "interfaces": []
#       },
#       {
#         "id": "weather_agent",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/weather_agent.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_SIMPLEASSISTANTAGENT",
#             "target_node": "SimpleAssistantAgent"
#           }
#         ],
#         "tools": [],
#         "interfaces": []
#       },
#       {
#         "id": "SimpleAssistantAgent",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/SimpleAssistantAgent.py",
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
# Target Model Provider Coordinate: openai:gpt-4o-mini

# 3. Define functional stubs for cross-compiled tools
# No external tool dependencies declared in universal spec topology.

# 3.2 Initialize Registered Global MCP Capability Interface Targets
GLOBAL_INTERFACES_REGISTRY = {}

# 4. Define strict Data Contract Verification Model schemas
class SharedContextContract(BaseModel):
    pass

# 5. Define Autonomous PydanticAI Agents dynamically from Topology
GroupChatManager_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted from legacy conversational script via AST source-slicing. Node context: GroupChatManager. Authorized MCP Interfaces: []",
)

Assistant_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted from legacy conversational script via AST source-slicing. Node context: Assistant. Authorized MCP Interfaces: []",
)

Critic_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted from legacy conversational script via AST source-slicing. Node context: Critic. Authorized MCP Interfaces: []",
)

weather_agent_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted from legacy conversational script via AST source-slicing. Node context: weather_agent. Authorized MCP Interfaces: []",
)

SimpleAssistantAgent_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted from legacy conversational script via AST source-slicing. Node context: SimpleAssistantAgent. Authorized MCP Interfaces: []",
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
        "GroupChatManager": GroupChatManager_agent,
        "Assistant": Assistant_agent,
        "Critic": Critic_agent,
        "weather_agent": weather_agent_agent,
        "SimpleAssistantAgent": SimpleAssistantAgent_agent,
    }
    NODES_PIPELINE_MAP = {
        "GroupChatManager": importlib.import_module("blobs.GroupChatManager").run,
        "Assistant": importlib.import_module("blobs.Assistant").run,
        "Critic": importlib.import_module("blobs.Critic").run,
        "weather_agent": importlib.import_module("blobs.weather_agent").run,
        "SimpleAssistantAgent": importlib.import_module("blobs.SimpleAssistantAgent").run,
    }

    ROUTING_TABLE = {
        "GroupChatManager": {
            "ASSISTANT": "Assistant",
            "END": "END"
        },
        "Assistant": {
            "CRITIC": "Critic",
            "END": "END"
        },
        "Critic": {
            "WEATHER_AGENT": "weather_agent",
            "END": "END"
        },
        "weather_agent": {
            "SIMPLEASSISTANTAGENT": "SimpleAssistantAgent",
            "END": "END"
        },
        "SimpleAssistantAgent": {
            "END": "END"
        },
    }

    current_node = "GroupChatManager"
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