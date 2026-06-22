import json
import urllib.request

def run(state):
    print("\n   🏁 [Blob: Generator] Synthesizing final response from verified document context...")
    context = state["context"]
    
    user_query = context.get("user_query", "")
    verified_context = context.get("retrieved_chunks", "")
    loop_count = context.get("loop_counter", 1)
    
    # Prompt engineering designed to completely neutralize LLM hallucinations
    system_instruction = (
        "You are an enterprise-grade QA synthesis engine. Your task is to provide a comprehensive, clear, "
        "and direct answer to the user's query based strictly on the provided text context.\n"
        "Rules:\n"
        "1. Ground your response entirely in the provided retrieved context.\n"
        "2. If the context does not contain enough data to thoroughly answer, state exactly what is missing.\n"
        "3. Do not make up facts, rely on outside knowledge, or introduce hallucinations."
    )
    
    # If the circuit breaker forced execution through, gently inform the model
    if "No contextual vector hits" in verified_context or "Fallback Unrelated Context" in verified_context:
        user_payload = f"Context: (Note: No matching documentation was located after multiple search optimizations.)\n\nQuestion: {user_query}"
    else:
        user_payload = f"Verified Context:\n{verified_context}\n\nUser Question: {user_query}"
    
    api_payload = {
        "model": "llama3.2:3b",
        "messages": [
            {"role": "system", "content": system_instruction},
            {"role": "user", "content": user_payload}
        ],
        "temperature": 0.4,
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
        
        with urllib.request.urlopen(req, timeout=30) as response:
            res_json = json.loads(response.read().decode("utf-8"))
            final_answer = res_json["choices"][0]["message"]["content"].strip()
            
            print("\n========================= 🎉 SWARMHUB ANSWER =========================")
            print(final_answer)
            print(f"======================================================================\n(Total Iterations Required: {loop_count})")
            
            # Store final output safely in your state layer tracking matrix
            context["final_response"] = final_answer
            
    except Exception as e:
        print(f"      ❌ Answer synthesis failed due to system fault: {e}")
        context["final_response"] = "Error: Prompt execution timeout during final synthesis."
        
    state["context"] = context
    state["next_action"] = "COMPLETE"
    return state