import os
import sys
import subprocess
import json
import re
import shutil

sys.path.insert(0, os.getcwd())
from tools.ingestion.crawler import BulkRegistryCrawler
from tools.ingestion.classifier import LlamaMetadataClassifier

class LiveRepositoryHook:
    """
    Decomposes deep subfolder and file URLs from external markdown registries,
    clones base roots, targets internal subpaths, and runs local Llama passes.
    """
    def __init__(self, repo_url: str, cache_dir: str = "dist/cache/500-agents"):
        self.repo_url = repo_url
        self.cache_dir = cache_dir
        self.master_catalog_path = os.path.join("dist", "registry", "registry_index.json")
        self.classifier = LlamaMetadataClassifier()

    def _sync_remote_repository(self) -> None:
        """Clones or updates the main repository index via git."""
        print(f"📡 Connecting to master repository data feed at: {self.repo_url}")
        if os.path.exists(os.path.join(self.cache_dir, ".git")):
            print("🔄 Local repository cache found. Synchronizing changes via git pull...")
            try:
                subprocess.run(["git", "-C", self.cache_dir, "pull"], check=True, capture_output=True, text=True)
                print("🟢 Success! Cache is fully up-to-date with upstream changes.")
            except subprocess.CalledProcessError:
                print("⚠️  Git pull failed. Clearing corrupted cache path to force a clean reset...")
                shutil.rmtree(self.cache_dir)
                self._execute_fresh_clone()
        else:
            if os.path.exists(self.cache_dir):
                print("⚠️  Cache folder exists but lacks Git memory tracking. Wiping directory to prevent clone collision...")
                shutil.rmtree(self.cache_dir)
            self._execute_fresh_clone()

    def _execute_fresh_clone(self) -> None:
        """Performs a lightweight, high-speed shallow clone of the target repository tree."""
        print("📥 Initializing a high-speed shallow clone of the repository...")
        os.makedirs(os.path.dirname(self.cache_dir), exist_ok=True)
        try:
            subprocess.run(["git", "clone", "--depth", "1", self.repo_url, self.cache_dir], check=True, capture_output=True, text=True)
            print("🟢 Success! Master repository layout cloned safely to local workspace.")
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"❌ Critical Error: Failed to mirror remote target: {e.stderr}")

    def _parse_readme_tables(self) -> list:
        """Parses README.md tables using a split approach to extract agent details and true target links."""
        readme_path = os.path.join(self.cache_dir, "README.md")
        if not os.path.exists(readme_path):
            return []

        print("📖 Parsing README.md database tables to discover cloud and local workflows...")
        with open(readme_path, "r", encoding="utf-8", errors="ignore") as f:
            lines = f.readlines()

        extracted_records = []
        for line in lines:
            clean_line = line.strip()
            if not clean_line.startswith("|") or clean_line.count("|") < 3:
                continue

            cells = [c.strip() for c in clean_line.split("|")][1:-1]
            if not cells or "Use Case" in cells[0] or "---" in cells[0]:
                continue

            display_name = re.sub(r'[^\w\s\-]', '', cells[0]).strip()
            industry = cells[1] if len(cells) > 1 else "Research & Development"
            description = cells[2] if len(cells) > 2 else "Agentic Workflow Blueprint Portfolio Asset."
            
            raw_parentheses_contents = re.findall(r'\(([^)]+)\)', clean_line)
            valid_links = [
                link.strip() for link in raw_parentheses_contents
                if "shields.io" not in link 
                and "badge" not in link 
                and not link.strip().endswith(('.png', '.svg', '.jpg', '.jpeg'))
            ]

            if valid_links:
                target_url = valid_links[0]
                if not target_url.startswith("http"):
                    normalized_rel = target_url.lstrip("./")
                    target_url = f"https://github.com/ashishpatel26/500-AI-Agents-Projects/tree/main/{normalized_rel}"

                extracted_records.append({
                    "name": display_name,
                    "industry": industry,
                    "description": description,
                    "url": target_url
                })

        return extracted_records

    def _decompose_github_url(self, url: str) -> tuple:
        """Deconstructs deep GitHub paths into base cloneable links and focus directories."""
        if "github.com" not in url:
            return url, ""
            
        match = re.match(r'(https://github\.com/[^/]+/[^/]+)(/(tree|blob)/[^/]+/(.*))?', url)
        if match:
            base_repo = match.group(1)
            subpath = match.group(4) if match.group(4) else ""
            return base_repo, subpath
            
        return url, ""

    def execute_pipeline(self) -> None:
        """Runs the multi-pass compilation loop across local and remote agent sources."""
        print("=" * 95)
        print("🐝 SWARMHUB PRODUCTION INGESTION HOOK ACTIVATED")
        print("=" * 95)

        self._sync_remote_repository()
        print("\n" + "-" * 95 + "\n")

        existing_records = []
        if os.path.exists(self.master_catalog_path):
            try:
                with open(self.master_catalog_path, "r", encoding="utf-8") as f:
                    existing_records = json.load(f)
                print(f"📦 Found {len(existing_records)} pre-existing agent profiles in index. Securing boundaries...")
            except Exception:
                existing_records = []

        # PASS 1: Sweep the native physical directories inside agents/
        crawler = BulkRegistryCrawler(target_repo_root=self.cache_dir)
        crawler.run_mass_ingestion()
        print("\n" + "-" * 95 + "\n")

        # PASS 2: Parse markdown tables and process external links
        table_records = self._parse_readme_tables()
        if not table_records:
            print("🏁 Ingestion pass complete. No additional external records found.")
            return

        print(f"\n🚀 Launching Ingestion Pass 2: Decomposing and mapping {len(table_records)} deep repositories...")
        print("=" * 95)

        catalog_index_records = []
        if os.path.exists(self.master_catalog_path):
            with open(self.master_catalog_path, "r", encoding="utf-8") as f:
                catalog_index_records = json.load(f)

        for ex_rec in existing_records:
            if not any(item.get("registry_handle") == ex_rec.get("registry_handle") for item in catalog_index_records):
                catalog_index_records.append(ex_rec)
        
        for index, record in enumerate(table_records, start=1):
            if not record["name"].strip():
                continue
                
            clean_slug = record["name"].lower().replace(" ", "-").replace("_", "-")
            if "#" in record["url"] or "CONTRIBUTION" in record["url"] or record["url"].endswith("agents/"):
                continue

            print(f"🛰  [Cloud Ingestion Batch {index}/{len(table_records)}] -> Indexing: {record['name']}")
            
            if any(item.get("registry_handle", "").endswith(clean_slug) for item in catalog_index_records):
                print(f"    skip  Asset '{clean_slug}' already exists in index. Skipping safely.\n")
                continue

            try:
                active_scan_path = ""
                if record["url"].startswith("https://github.com/ashishpatel26/500-AI-Agents-Projects/tree/main/"):
                    relative_path = record["url"].split("/tree/main/")[-1].replace("%20", " ")
                    active_scan_path = os.path.join(self.cache_dir, relative_path)
                else:
                    base_repo, subpath = self._decompose_github_url(record["url"])
                    if not base_repo.startswith("http") or "github.io" in base_repo:
                        print(f"    info  Skipping raw web page index documentation link: {record['url']}\n")
                        continue

                    # ROUTE TO A PERMANENT CACHE PATH FOR EXTERNAL PROJECTS
                    external_repo_cache = os.path.join("dist", "cache", "external", clean_slug)
                    
                    if not os.path.exists(os.path.join(external_repo_cache, ".git")):
                        if os.path.exists(external_repo_cache):
                            shutil.rmtree(external_repo_cache)
                        print(f"    📥 Cloning root repo coordinate to permanent cache: {base_repo}")
                        subprocess.run(
                            ["git", "clone", "--depth", "1", base_repo, external_repo_cache],
                            check=True, capture_output=True, timeout=45, text=True
                        )
                    else:
                        print(f"    🔄 External asset folder cache hit. Syncing upstream...")
                        subprocess.run(["git", "-C", external_repo_cache, "pull"], capture_output=True)
                    
                    active_scan_path = os.path.join(external_repo_cache, subpath) if subpath else external_repo_cache

                if not os.path.exists(active_scan_path):
                    print(f"    ⚠️  Target subpath folder does not exist inside repository structure: {active_scan_path}\n")
                    continue

                if os.path.isdir(active_scan_path):
                    context_str = self.classifier._compile_folder_context(active_scan_path)
                else:
                    try:
                        with open(active_scan_path, "r", encoding="utf-8", errors="ignore") as f:
                            context_str = f.read(6000)
                    except Exception:
                        context_str = ""

                if not context_str.strip():
                    print("    ⚠️  Skipping: Empty context code boundaries encountered.\n")
                    continue

                system_prompt = (
                    "You are an expert software architect acting as a metadata classifier for SwarmHub.\n"
                    "Analyze the provided codebase and return a valid JSON object matching this schema blueprint precisely.\n"
                    "Do NOT include conversational text, explanation markers, or markdown formatting.\n\n"
                    "CRITICAL INSTRUCTIONS FOR SMALL MODELS:\n"
                    "1. NEVER use literal guide words like 'string', 'Generic', or empty arrays.\n"
                    "2. 'primary_task': Generate an explicit descriptive title summarizing the logic function (e.g., 'Autonomous Market Microstructure Analysis').\n"
                    "3. 'original_framework': Extract the framework layer found (e.g., 'LangGraph', 'CrewAI', 'AutoGen', 'Vanilla Python').\n"
                    "4. 'complexity_tier': Evaluate depth and return exactly one: 'Beginner', 'Intermediate', or 'Advanced'.\n\n"
                    "EXPECTED JSON FORMAT ONLY:\n"
                    "{\n"
                    f'  "display_name": "{record["name"]}",\n'
                    '  "filters": {\n'
                    f'    "industry": "{record["industry"]}",\n'
                    '    "primary_task": "A precise multi-word summary of the actual logic execution function",\n'
                    '    "original_framework": "Vanilla Python",\n'
                    '    "complexity_tier": "Intermediate",\n'
                    '    "required_mcp_interfaces": ["web_browser_stdio"],\n'
                    '    "suggested_llm_baseline": "Llama-3.2-3b"\n'
                    "  }\n"
                    "}"
                )

                llm_metadata = self.classifier._query_local_llama(system_prompt, context_str)

                final_record = {
                    "registry_handle": f"martinkovacevic/SwarmHub-Registry/{clean_slug}",
                    "display_name": record["name"],
                    "original_source_url": record["url"],
                    "filters": llm_metadata.get("filters", {
                        "industry": record["industry"],
                        "primary_task": "Agentic Automation Loop",
                        "original_framework": "Vanilla Python",
                        "complexity_tier": "Intermediate",
                        "required_mcp_interfaces": ["file_server_stdio"],
                        "suggested_llm_baseline": "Llama-3.2-3b"
                    })
                }
                
                catalog_index_records.append(final_record)
                with open(self.master_catalog_path, "w", encoding="utf-8") as out_f:
                    json.dump(catalog_index_records, out_f, indent=4)
                    
                print(f"    ✅ Successfully cataloged cloud asset subpath!\n")

            except Exception as e:
                print(f"    ❌ Failed processing external link: {e}\n")
                continue

        print("=" * 95)
        print("🏁 Global Ingestion and Cloud Mapping Finished Successfully!")
        print(f"💾 Centralized Search Index updated at: {self.master_catalog_path}")
        print(f"💎 Grand Total Live Agentic Solutions on Marketplace: {len(catalog_index_records)} Agents")

if __name__ == "__main__":
    TARGET_REPO = "https://github.com/ashishpatel26/500-AI-Agents-Projects.git"
    hook = LiveRepositoryHook(repo_url=TARGET_REPO)
    try:
        hook.execute_pipeline()
    except KeyboardInterrupt:
        print("\n🛑 Ingestion loop suspended safely via terminal shortcut sequence.")