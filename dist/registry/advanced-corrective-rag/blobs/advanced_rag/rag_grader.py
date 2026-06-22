import json
import urllib.request

def run(state):
    print("\n   🧠 [Blob: Grader] Passing vector chunks to Llama 3.2 for evaluation...")
    context = state["context"]
    
    user_query = context.get("user_query", "")
    retrieved_context = context.get("retrieved_chunks", "")
    
    # Rigorous engineering prompt forcing a clean, standardized classification token output
    system_instruction = (
        "You are a high-performance QA relevance evaluator. Your sole duty is to judge if the provided text context "
        "contains accurate, sufficient domain information to thoroughly answer the user's query.\n"
        "Analyze the context carefully and reply with exactly one word, without formatting or punctuation:\n"
        "- 'SYNTHESIZE' if the context contains enough relevant data to answer the user's question.\n"
        "- 'REWRITE' if the context is irrelevant, missing the answer, or unrelated to the question.\n"
        "Do not provide explanations, preamble, conversational text, or markdown blocks. Output exactly one word."
    )
    
    user_payload = f"User Query: {user_query}\n\nRetrieved Context:\n{retrieved_context}"
    
    api_payload = {
        "model": "llama3.2:3b",
        "messages": [
            {"role": "system", "content": system_instruction},
            {"role": "user", "content": user_payload}
        ],
        "temperature": 0.0,
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
            model_response = res_json["choices"][0]["message"]["content"].strip().upper()
            
            print(f"      🤖 [Ollama Grader Judgment Output]: '{model_response}'")
            
            # Map the model's token response directly to our compiled workflow triggers
            if "SYNTHESIZE" in model_response:
                context["grade_status"] = "SYNTHESIZE"
                state["next_action"] = "SYNTHESIZE"
            else:
                context["grade_status"] = "REWRITE"
                state["next_action"] = "REWRITE"
                
    except Exception as e:
        print(f"      ❌ Local inference transaction error caught during grading pass: {e}")
        # Secure fallback strategy: default to a rewrite iteration to stay safe
        context["grade_status"] = "REWRITE"
        state["next_action"] = "REWRITE"
        
    state["context"] = context
    return state