import os
import json
import urllib.request
import urllib.error

class LlamaMetadataClassifier:
    """
    Automated ecosystem ingestion layer for SwarmHub. Consumes raw, un-vetted 
    agent source code repositories and utilizes a local Llama 3.2 instance to 
    classify, tag, and output standardized schema manifests.
    """
    def __init__(self, ollama_endpoint: str = "http://localhost:11434/api/generate", model_name: str = "llama3.2"):
        self.endpoint = ollama_endpoint
        self.model_name = model_name

    def _compile_folder_context(self, folder_path: str) -> str:
        """Reads and aggregates text assets inside a target folder to construct LLM context."""
        context_pieces = []
        
        # Priority scan targets to avoid reading endless token noise
        priority_extensions = (".md", ".py", ".txt", ".ipynb")
        
        for root, _, files in os.walk(folder_path):
            for file in files:
                if file.endswith(priority_extensions):
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                            content = f.read(4000) # Cap reading per file to prevent overflow
                        context_pieces.append(f"--- File: {file} ---\n{content}\n")
                    except Exception:
                        continue
                        
        return "\n".join(context_pieces)[:12000] # Safe token bounding box window

    def _query_local_llama(self, system_prompt: str, user_content: str) -> dict:
        """Dispatches a synchronous request to the local Ollama daemon enforcing strict JSON parsing."""
        payload = {
            "model": self.model_name,
            "prompt": f"{system_prompt}\n\nAnalyze this codebase content:\n{user_content}",
            "format": "json", # Ollama native structural constraint flag
            "stream": False,
            "options": {
                "temperature": 0.0 # Force maximum analytical determinism
            }
        }
        
        req = urllib.request.Request(
            self.endpoint,
            data=json.dumps(payload).encode("utf-8"),
            headers={"Content-Type": "application/json"}
        )
        
        try:
            with urllib.request.urlopen(req, timeout=45) as response:
                raw_res = json.loads(response.read().decode("utf-8"))
                return json.loads(raw_res["response"])
        except urllib.error.URLError as e:
            raise RuntimeError(
                f"❌ Unable to communicate with local Ollama daemon at {self.endpoint}.\n"
                f"👉 Ensure your server is active by running: ollama run {self.model_name}\n"
                f"Tracking Info: {e}"
            )
        except json.JSONDecodeError as je:
            raise RuntimeError(f"❌ Llama 3.2 broke JSON schema compliance: {je}")

    def classify_agent_directory(self, local_folder: str, repository_base_url: str, github_username: str) -> None:
        """Scans a local agent folder, runs the LLM filter gate, and generates the target manifest file."""
        if not os.path.exists(local_folder):
            raise FileNotFoundError(f"Target path '{local_folder}' does not exist.")

        folder_slug = os.path.basename(os.path.normpath(local_folder))
        print(f"🔍 Analyzing unstructured codebase stack inside: [{folder_slug}]...")
        
        context_str = self._compile_folder_context(local_folder)
        if not context_str.strip():
            print(f"⚠️  Skipping [{folder_slug}] - No readable code assets found.")
            return

        system_prompt = (
            "You are an expert software architect acting as a metadata classifier for SwarmHub.\n"
            "Your task is to analyze the provided multi-agent codebase and extract its metadata fields.\n"
            "You MUST respond with a single, valid JSON object matching this schema blueprint precisely.\n"
            "Do NOT include conversational text, explanation markers, or markdown formatting.\n\n"
            "CRITICAL CONSTRAINTS FOR VALUES:\n"
            "1. 'display_name': Clean, professional human-readable title.\n"
            "2. 'industry': Must map to exactly one: 'Finance', 'Healthcare', 'E-commerce', 'Supply Chain', 'Legal', 'Customer Support', 'Research & Development', or 'Generic'.\n"
            "3. 'primary_task': Two to four words summarizing operation (e.g., 'Web Scraping & Synthesis', 'Risk Evaluation').\n"
            "4. 'original_framework': Identify primary architecture: 'LangGraph', 'CrewAI', 'AutoGen', or 'Vanilla Python'.\n"
            "5. 'complexity_tier': Evaluate depth and assign either 'Beginner', 'Intermediate', or 'Advanced'.\n"
            "6. 'required_mcp_interfaces': Extract underlying tools or endpoints needed. Match to names like 'web_browser_stdio', 'file_server_stdio', 'financial_market_service', etc.\n"
            "7. 'suggested_llm_baseline': Suggest default model capability tier (e.g., 'Llama-3.2-3b', 'GPT-4o').\n\n"
            "EXPECTED JSON FORMAT ONLY:\n"
            "{\n"
            '  "display_name": "string",\n'
            '  "filters": {\n'
            '    "industry": "string",\n'
            '    "primary_task": "string",\n'
            '    "original_framework": "string",\n'
            '    "complexity_tier": "string",\n'
            '    "required_mcp_interfaces": ["string"],\n'
            '    "suggested_llm_baseline": "string"\n'
            "  }\n"
            "}"
        )

        # Execute LLM classification pass
        llm_metadata = self._query_local_llama(system_prompt, context_str)
        
        # Deterministically patch infrastructure handles and URLs
        asset_name_slug = folder_slug.lower().replace(" ", "-").replace("_", "-")
        registry_handle = f"{github_username}/SwarmHub-Registry/{asset_name_slug}"
        original_source_url = f"{repository_base_url.rstrip('/')}/tree/main/{local_folder.replace(os.sep, '/')}"

        # Assemble the final unified package contract layout
        final_manifest = {
            "registry_handle": registry_handle,
            "display_name": llm_metadata.get("display_name", folder_slug.replace("-", " ").replace("_", " ").title()),
            "original_source_url": original_source_url,
            "filters": llm_metadata.get("filters", {})
        }

        # Write output straight into the local agent directory target path
        output_manifest_path = os.path.join(local_folder, "blob.json")
        with open(output_manifest_path, "w", encoding="utf-8") as out_f:
            json.dump(final_manifest, out_f, indent=4)
            
        print(f"🟢 Success! Standardized manifest cataloged to: {output_manifest_path}")
        print(json.dumps(final_manifest, indent=2))
        print("-" * 80)

if __name__ == "__main__":
    # Mock loop driver testing a localized target folder extraction pass
    # Setup directory anchors to simulate a mock project tree
    mock_agent_path = "tools/ingestion/sample_scraped_agent"
    os.makedirs(mock_agent_path, exist_ok=True)
    
    with open(os.path.join(mock_agent_path, "research.py"), "w") as f:
        f.write(
            "import requests\n"
            "from bs4 import BeautifulSoup\n"
            "from crewai import Agent, Crew\n\n"
            "def run(state):\n"
            "    print('Scraping health metrics summaries via requests...')\n"
            "    return state"
        )
        
    with open(os.path.join(mock_agent_path, "README.md"), "w") as f:
        f.write("# Medical Literature Scraper\nAn automated clinical data aggregator built on CrewAI.")

    # Initialize and execute the gatekeeper classifier helper
    classifier = LlamaMetadataClassifier()
    
    try:
        classifier.classify_agent_directory(
            local_folder=mock_agent_path,
            repository_base_url="https://github.com/ashishpatel26/500-AI-Agents-Projects",
            github_username="martinkovacevic"
        )
    except Exception as err:
        print(err)