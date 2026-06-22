# ==========================================================================
# GENERATED AUTOMATICALLY BY SWARMHUB FOR AGENT SWARM: advanced-corrective-rag-swarm
# TARGET RUNTIME: CrewAI (Memory Layer: sqlite | Thread: local-rag-session-001)
# ==========================================================================

import importlib
import os
import sys
import sqlite3
import json
from pydantic import BaseModel, Field
# === SWARMHUB METADATA SOURCE MAP (LOSSLESS ROUND-TRIP ASSURANCE) ===
# SWARMHUB_METADATA_START
# {
#   "version": "agentic.io/v1alpha1",
#   "kind": "UniversalAgent",
#   "name": "advanced-corrective-rag-swarm",
#   "runtime": {
#     "provider": "openai",
#     "model": "llama3.2:3b",
#     "temperature": 0.1,
#     "max_tokens": null
#   },
#   "memory": {
#     "storage_backend": "sqlite",
#     "thread_id": "local-rag-session-001",
#     "connection_string": "dist/advanced_rag/rag_memory_vault.db"
#   },
#   "system_prompt": "You are a professional autonomous agent instance engineered via SwarmHub SDK.",
#   "interfaces": [
#     {
#       "name": "vector_store_service",
#       "protocol": "mcp",
#       "transport": "stdio",
#       "endpoint": "python",
#       "args": [
#         "tools/advanced_rag/vector_service_daemon.py"
#       ],
#       "metadata": {}
#     }
#   ],
#   "state_schema": {
#     "user_query": "str",
#     "search_query": "str",
#     "retrieved_chunks": "str",
#     "grade_status": "str",
#     "loop_counter": "int"
#   },
#   "topology": {
#     "type": "StateMachine",
#     "initial_node": "document_retriever",
#     "nodes": [
#       {
#         "id": "document_retriever",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/advanced_rag/rag_retriever.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_PROCEED",
#             "target_node": "context_grader"
#           }
#         ],
#         "tools": [],
#         "interfaces": [
#           "vector_store_service"
#         ]
#       },
#       {
#         "id": "context_grader",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/advanced_rag/rag_grader.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_SYNTHESIZE",
#             "target_node": "synthesis_generator"
#           },
#           {
#             "on_condition": "GOTO_REWRITE",
#             "target_node": "query_rewriter"
#           }
#         ],
#         "tools": [],
#         "interfaces": []
#       },
#       {
#         "id": "query_rewriter",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/advanced_rag/rag_rewriter.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_RETRY",
#             "target_node": "document_retriever"
#           }
#         ],
#         "tools": [],
#         "interfaces": []
#       },
#       {
#         "id": "synthesis_generator",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/advanced_rag/rag_generator.py",
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
# Selected Provider Context: openai
# Selected Model Target: llama3.2:3b

# 3. Define functional stubs for cross-compiled tools
# No external tool dependencies declared in universal spec topology.

# 3.2 Initialize Registered Global MCP Capability Interface Targets
GLOBAL_INTERFACES_REGISTRY = {
    "vector_store_service": {"protocol": "mcp", "transport": "stdio", "endpoint": "python", "args": ['tools/advanced_rag/vector_service_daemon.py']},
}

# 4. Define strict Data Contract Verification Model schemas
class SharedContextContract(BaseModel):
    user_query: str = ""
    search_query: str = ""
    retrieved_chunks: str = ""
    grade_status: str = ""
    loop_counter: int = 0

# 5. Define Autonomous Agent Personas dynamically from Topology
document_retriever_agent = Agent(
    role="Document Retriever",
    goal="Execute capabilities defined under the workspace node document_retriever",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: ['vector_store_service']",
    tools=[],
    verbose=True,
    allow_delegation=False
)

context_grader_agent = Agent(
    role="Context Grader",
    goal="Execute capabilities defined under the workspace node context_grader",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[],
    verbose=True,
    allow_delegation=False
)

query_rewriter_agent = Agent(
    role="Query Rewriter",
    goal="Execute capabilities defined under the workspace node query_rewriter",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[],
    verbose=True,
    allow_delegation=False
)

synthesis_generator_agent = Agent(
    role="Synthesis Generator",
    goal="Execute capabilities defined under the workspace node synthesis_generator",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[],
    verbose=True,
    allow_delegation=False
)

# 6. Define Concrete Task Assignments linked back to Code Blobs
document_retriever_task = Task(
    description="Execute processing code logic anchored at: blobs/advanced_rag/rag_retriever.py. Authorized Connection Boundaries: ['vector_store_service']",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=document_retriever_agent
)

context_grader_task = Task(
    description="Execute processing code logic anchored at: blobs/advanced_rag/rag_grader.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=context_grader_agent
)

query_rewriter_task = Task(
    description="Execute processing code logic anchored at: blobs/advanced_rag/rag_rewriter.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=query_rewriter_agent
)

synthesis_generator_task = Task(
    description="Execute processing code logic anchored at: blobs/advanced_rag/rag_generator.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=synthesis_generator_agent
)

# 7. Assemble the Unified Crew Workspace Execution Order
crew = Crew(
    agents=[document_retriever_agent, context_grader_agent, query_rewriter_agent, synthesis_generator_agent],
    tasks=[document_retriever_task, context_grader_task, query_rewriter_task, synthesis_generator_task],
    process=Process.sequential,
    verbose=True
)

# 8. Execution and Localized Blob Verification Pipeline
if __name__ == "__main__":
    print("🚀 Running compiled SwarmHub execution pipeline validation...")
    print("⚠️ [Mode: Local Offline Execution] State-Machine verification pass ignited.\n")
    db = sqlite3.connect("dist/advanced_rag/rag_memory_vault.db")
    cursor = db.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS swarmhub_checkpoints (thread_id TEXT PRIMARY KEY, state_json TEXT)")
    db.commit()
    cursor.execute("SELECT state_json FROM swarmhub_checkpoints WHERE thread_id = 'local-rag-session-001'")
    row = cursor.fetchone()
    user_prompt = input("❓ Enter your workflow query: ")
    default_state = {"messages": [], "context": {"user_query": user_prompt, "search_query": "", "retrieved_chunks": "", "grade_status": "", "loop_counter": 0}, "next_action": ""}
    if row:
        print("    ⏳ [Memory] Found active checkpoint snapshot. Re-hydrating context state...")
        state = json.loads(row[0])
    else:
        state = default_state

    # Target framework execution state-machine routing configuration maps
    NODES_CONFIG = {
        "document_retriever": {"import_path": "blobs.advanced_rag.rag_retriever", "interfaces": ['vector_store_service'], "inline_f": "_inline_document_retriever" if hasattr(sys.modules[__name__], "_inline_document_retriever") else None},
        "context_grader": {"import_path": "blobs.advanced_rag.rag_grader", "interfaces": [], "inline_f": "_inline_context_grader" if hasattr(sys.modules[__name__], "_inline_context_grader") else None},
        "query_rewriter": {"import_path": "blobs.advanced_rag.rag_rewriter", "interfaces": [], "inline_f": "_inline_query_rewriter" if hasattr(sys.modules[__name__], "_inline_query_rewriter") else None},
        "synthesis_generator": {"import_path": "blobs.advanced_rag.rag_generator", "interfaces": [], "inline_f": "_inline_synthesis_generator" if hasattr(sys.modules[__name__], "_inline_synthesis_generator") else None},
    }

    ROUTING_TABLE = {
        "document_retriever": {
            "PROCEED": "context_grader",
            "END": "END"
        },
        "context_grader": {
            "SYNTHESIZE": "synthesis_generator",
            "REWRITE": "query_rewriter",
            "END": "END"
        },
        "query_rewriter": {
            "RETRY": "document_retriever",
            "END": "END"
        },
        "synthesis_generator": {
            "END": "END"
        },
    }

    current_node = "document_retriever"
    while current_node and current_node != "END":
        cfg = NODES_CONFIG.get(current_node)
        if not cfg:
            break
        print(f"\n--- 🟢 Entering Runtime Task Node: {current_node} ---")
        print(f"    🔒 [Permissions] Authorized MCP Interfaces: {cfg['interfaces']}")
        
        try:
            SharedContextContract(**state["context"])
        except Exception as contract_err:
            print(f"    ⚠️ [Contract Breakage] Incoming schema anomaly caught at entry of {current_node}: {contract_err}")
        
        try:
            if cfg["inline_f"] and cfg["inline_f"] in globals():
                state = globals()[cfg["inline_f"]](state)
            else:
                module = importlib.import_module(cfg["import_path"])
                state = module.run(state)
            
            SharedContextContract(**state["context"])
            cursor.execute("INSERT OR REPLACE INTO swarmhub_checkpoints VALUES ('local-rag-session-001', ?)", (json.dumps(state),))
            db.commit()
        except Exception as e:
            print(f"    ❌ Execution/Contract Fault inside {current_node}: {e}")
            break
        
        action = state.get("next_action", "PROCEED").upper()
        if action.startswith("GOTO_"):
            action = action.replace("GOTO_", "", 1)
        current_node = ROUTING_TABLE.get(current_node, {}).get(action, "END")

    print("\n🏁 Local CrewAI Task Blob Pipeline Successfully Executed!")
    print("Final Verified State Context Payload:", state["context"])
    db.close()