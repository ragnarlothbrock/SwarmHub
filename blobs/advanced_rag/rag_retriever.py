import json
import subprocess
import sys

def run(state):
    print("\n   📥 [Blob: Retriever] Connecting to live MCP Vector Daemon process...")
    context = state["context"]
    
    # Extract the active search criteria; default to base user query if unoptimized
    query = context.get("search_query", "") or context.get("user_query", "")
    
    # Safe state tracking increment for our circuit breaker
    current_loops = context.get("loop_counter", 0)
    if isinstance(current_loops, str) and current_loops == "":
        current_loops = 0
    context["loop_counter"] = int(current_loops) + 1
    
    print(f"      Scanning high-dimensional PDF embeddings for: '{query}' (Loop: {context['loop_counter']})")
    
    # Locate our background tool daemon path
    daemon_script = "tools/advanced_rag/vector_service_daemon.py"
    
    try:
        # Open a secure standard I/O communication link with our MCP tool server
        proc = subprocess.Popen(
            [sys.executable, daemon_script],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        # Formulate the query request transaction
        payload = {"query": query}
        
        # Dispatch the message through the pipe and wait for the response vector matching blocks
        stdout_data, stderr_data = proc.communicate(input=json.dumps(payload) + "\n", timeout=30)
        
        if proc.returncode == 0 and stdout_data:
            response = json.loads(stdout_data.strip())
            if response.get("status") == "SUCCESS":
                context["retrieved_chunks"] = response.get("results", "")
                print("      ✅ SOTA Cosine similarity search complete. Top chunks loaded into context state.")
            else:
                context["retrieved_chunks"] = "No contextual vector hits located."
                print("      ⚠️ Daemon returned empty or unsuccessful status.")
        else:
            print(f"      ❌ Daemon process failure. Stderr context log: {stderr_data}")
            context["retrieved_chunks"] = "Error: Vector service tool execution breakdown."
            
    except Exception as e:
        print(f"      ❌ Failed to establish communication link with MCP daemon tool: {e}")
        context["retrieved_chunks"] = f"Error: IPC link failure ({e})"
        
    # Satisfy strict global Pydantic contract validation expectations before exiting
    if "search_query" not in context or not context["search_query"]:
        context["search_query"] = query
    if "grade_status" not in context:
        context["grade_status"] = ""
        
    state["context"] = context
    state["next_action"] = "PROCEED"  # Unconditional transition directing traffic to the grader
    return state