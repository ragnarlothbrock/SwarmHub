import json
import urllib.request

def run(state):
    print("\n   🔄 [Blob: Rewriter] Transforming query for enhanced semantic matching...")
    context = state["context"]
    
    user_query = context.get("user_query", "")
    failing_query = context.get("search_query", "")
    
    # 🚨 Circuit Breaker Guardrail: Prevent infinite loop if model keeps failing
    loop_count = int(context.get("loop_counter", 1))
    if loop_count >= 3:
        print("      🛑 [Circuit Breaker] Maximum retry threshold reached. Forcing synthesis pass with current context.")
        context["grade_status"] = "SYNTHESIZE"
        state["context"] = context
        # We route directly back into the system loop via the retrieval pipeline to satisfy graph structures
        state["next_action"] = "RETRY" 
        return state

    # Prompt forcing optimization into clean semantic keyword tokens
    system_instruction = (
        "You are an expert search query optimization engine. Your job is to take an initial user query "
        "and a failing search query, analyze their semantic intent, and output an improved version "
        "optimized for a vector database similarity search. Focus on core technical keywords, synonyms, "
        "and domain-specific terms. Do not include markdown, quotes, preamble, or explanations. "
        "Output ONLY the optimized query string."
    )
    
    user_payload = f"Original Question: {user_query}\nFailing Query: {failing_query}"
    
    api_payload = {
        "model": "llama3.2:3b",
        "messages": [
            {"role": "system", "content": system_instruction},
            {"role": "user", "content": user_payload}
        ],
        "temperature": 0.3,
        "stream": False
    }
    
    url = "http://localhost:11434/v1/chat/completions"
    headers = {"Content-Type": "application/json"}
    
    try:
        req = urllib.request.Request(
            url, 
            data=json.dumps(api_payload).encode("utf-8"), 
            headers=headers, 
            method="POST"
        )
        
        with urllib.request.urlopen(req, timeout=15) as response:
            res_json = json.loads(response.read().decode("utf-8"))
            optimized_query = res_json["choices"][0]["message"]["content"].strip()
            
            # Strip out any residual formatting artifacts the local model might output
            optimized_query = optimized_query.replace('"', '').replace("'", "")
            
            print(f"      🤖 [Ollama Query Evolution]: '{failing_query}' ➔ '{optimized_query}'")
            context["search_query"] = optimized_query
            
    except Exception as e:
        print(f"      ❌ Query rewriting failed due to communication fault: {e}")
        # Secure fallback: default back to the original question to avoid breaking state
        context["search_query"] = user_query
        
    state["context"] = context
    state["next_action"] = "RETRY"  # Signals the framework to pass traffic back to document_retriever
    return state