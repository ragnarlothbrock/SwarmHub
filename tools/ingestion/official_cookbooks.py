import os
import sys
import subprocess
import json
import shutil

# Ensure workspace paths are visible for relative tooling cross-imports
sys.path.insert(0, os.getcwd())
from tools.ingestion.classifier import LlamaMetadataClassifier

class OfficialCookbookIngestor:
    """
    Automated high-fidelity ingestion layer for SwarmHub. Re-routed to map 
    next-gen monorepo configurations for AutoGen, LangGraph, and CrewAI.
    """
    def __init__(self, cache_base: str = "dist/cache/official"):
        self.cache_base = cache_base
        self.master_catalog_path = os.path.join("dist", "registry", "registry_index.json")
        self.classifier = LlamaMetadataClassifier()
        
        # Updated targeting coordinates matching current framework branches
        self.targets = {
            "CrewAI": {
                "repo_url": "https://github.com/crewAIInc/crewAI-examples.git",
                "paths": ["crews", "flows"]
            },
            "LangGraph": {
                "repo_url": "https://github.com/langchain-ai/langgraph.git",
                "paths": [os.path.join("docs", "tutorials"), "examples"]
            },
            "AutoGen": {
                "repo_url": "https://github.com/microsoft/autogen.git",
                "paths": [
                    os.path.join("python", "samples"),
                    os.path.join("python", "templates"),
                    os.path.join("docs", "notebooks")
                ]
            }
        }

    def _clone_repo(self, framework: str, repo_url: str) -> str:
        """Performs a localized shallow clone of an official framework repository."""
        repo_dir = os.path.join(self.cache_dir, framework.lower())
        
        if os.path.exists(os.path.join(repo_dir, ".git")):
            print(f"   🔄 Cache folder found for {framework}. Syncing via git pull...")
            try:
                subprocess.run(["git", "-C", repo_dir, "pull"], check=True, capture_output=True, text=True)
                return repo_dir
            except subprocess.CalledProcessError:
                print(f"   ⚠️  Git pull failed for {framework}. Forcing a clean re-clone...")
                shutil.rmtree(repo_dir)

        print(f"   📥 Shallow cloning official {framework} source engine...")
        os.makedirs(repo_dir, exist_ok=True)
        subprocess.run(
            ["git", "clone", "--depth", "1", repo_url, repo_dir],
            check=True, capture_output=True, text=True
        )
        return repo_dir

    def run_pristine_ingestion(self) -> None:
        print("=" * 95)
        print("🧬 SWARMHUB PRISTINE LAYER INGESTION HOOK ACTIVATED")
        print("=" * 95)

        catalog_index_records = []
        if os.path.exists(self.master_catalog_path):
            with open(self.master_catalog_path, "r", encoding="utf-8") as f:
                catalog_index_records = json.load(f)

        self.cache_dir = self.cache_base
        os.makedirs(self.cache_dir, exist_ok=True)

        for framework, config in self.targets.items():
            print(f"\n🛰️  [Target Cluster] -> Processing Official {framework} Ecosystem Blueprints...")
            
            try:
                local_repo_root = self._clone_repo(framework, config["repo_url"])
                
                # Try all candidate paths to find valid directories
                valid_paths_found = []
                for candidate in config["paths"]:
                    test_path = os.path.join(local_repo_root, candidate)
                    if os.path.exists(test_path):
                        valid_paths_found.append(test_path)
                
                if not valid_paths_found:
                    print(f"❌ Error: Failed to find any matching folder candidates for {framework} inside repository.")
                    continue

                for resolved_subpath in valid_paths_found:
                    print(f"   📂 Active directory tracking map locked to: {os.path.relpath(resolved_subpath, local_repo_root)}")
                    
                    child_entries = sorted([
                        os.path.join(resolved_subpath, d) for d in os.listdir(resolved_subpath)
                        if not d.startswith(".")
                    ])
                    
                    child_modules = [
                        e for e in child_entries
                        if os.path.isdir(e) or e.endswith((".ipynb", ".py"))
                    ]
                    
                    print(f"   📊 Discovered {len(child_modules)} high-tier production modules inside this track.")
                    
                    for module_path in child_modules:
                        raw_name = os.path.basename(module_path)
                        folder_name = os.path.splitext(raw_name)[0]
                        clean_slug = f"{framework.lower()}-{folder_name.lower().replace(' ', '-').replace('_', '-')}"
                        
                        if any(item.get("registry_handle", "").endswith(clean_slug) for item in catalog_index_records):
                            continue

                        print(f"      ⚡ Mapping Architectural Module: {folder_name}")
                        
                        try:
                            if os.path.isdir(module_path):
                                context_str = self.classifier._compile_folder_context(module_path)
                            else:
                                with open(module_path, "r", encoding="utf-8", errors="ignore") as f:
                                    context_str = f.read(6000)

                            system_prompt = (
                                "You are an expert software architect acting as a metadata classifier for SwarmHub.\n"
                                "Analyze the provided codebase context and return a valid JSON object matching this blueprint.\n"
                                "Do NOT include conversational text, explanation markers, or markdown formatting.\n\n"
                                "CRITICAL INSTRUCTIONS FOR SMALL MODELS:\n"
                                "1. NEVER use literal words like 'string', 'Generic', or empty brackets as text property targets.\n"
                                "2. 'primary_task': Extrapolate a real, human title summarizing the agent loop (e.g., 'Conversational Matrix Routing').\n"
                                "3. 'complexity_tier': Must evaluate loop depth and return exactly one: 'Beginner', 'Intermediate', or 'Advanced'.\n"
                                "4. 'required_mcp_interfaces': Extract underlying tools/libraries found.\n"
                                "5. 'suggested_llm_baseline': Explicitly name an engine capability level (e.g., 'Llama-3.2-3b', 'GPT-4o').\n\n"
                                "EXPECTED JSON FORMAT ONLY:\n"
                                "{\n"
                                '  "display_name": "Human Readable Title Without Quotes",\n'
                                '  "filters": {\n'
                                '    "industry": "Research & Development",\n'
                                '    "primary_task": "A precise multi-word summary of the actual logic function",\n'
                                f'    "original_framework": "{framework}",\n'
                                '    "complexity_tier": "Intermediate",\n'
                                '    "required_mcp_interfaces": ["web_browser_stdio"],\n'
                                '    "suggested_llm_baseline": "Llama-3.2-3b"\n'
                                "  }\n"
                                "}"
                            )

                            llm_metadata = self.classifier._query_local_llama(system_prompt, context_str)

                            relative_git_subpath = module_path.split(f"{framework.lower()}/")[-1]
                            clean_web_url = config["repo_url"].rstrip(".git") + f"/tree/main/{relative_git_subpath}"

                            final_record = {
                                "registry_handle": f"martinkovacevic/SwarmHub-Registry/{clean_slug}",
                                "display_name": llm_metadata.get("display_name", folder_name.replace("-", " ").replace("_", " ").title()),
                                "original_source_url": clean_web_url,
                                "filters": llm_metadata.get("filters", {
                                    "industry": "Research & Development",
                                    "primary_task": "Agentic Architecture Automation",
                                    "original_framework": framework,
                                    "complexity_tier": "Intermediate",
                                    "required_mcp_interfaces": ["file_server_stdio"],
                                    "suggested_llm_baseline": "Llama-3.2-3b"
                                })
                            }
                            
                            catalog_index_records.append(final_record)
                            with open(self.master_catalog_path, "w", encoding="utf-8") as out_f:
                                json.dump(catalog_index_records, out_f, indent=4)
                                
                            print(f"      ✅ Successfully cataloged pristine asset: {folder_name}")

                        except Exception as inner_err:
                            print(f"      ⚠️  Skipping inner module pass [{folder_name}]: {inner_err}")
                            continue

            except Exception as outer_err:
                print(f"❌ Failed processing target cluster queue block for {framework}: {outer_err}")
                continue

        print("=" * 95)
        print("🏁 PRISTINE INITIAL INDEX SYNCHRONIZATION FINISHED SUCCESSFULLY")
        print(f"💾 Centralized Search Index verified at: {self.master_catalog_path}")
        print(f"💎 Grand Total Live Agentic Solutions on Marketplace: {len(catalog_index_records)} Agents")

if __name__ == "__main__":
    # Index is left intact so CrewAI and LangGraph remain cached on your disk while AutoGen fills in!
    ingestor = OfficialCookbookIngestor()
    try:
        ingestor.run_pristine_ingestion()
    except KeyboardInterrupt:
        print("\n🛑 Ingestion loop suspended safely via terminal sequence.")