import os
import json
import sys

# Ensure root paths are accessible for localized tool cross-imports
sys.path.insert(0, os.getcwd())
from tools.ingestion.classifier import LlamaMetadataClassifier

class BulkRegistryCrawler:
    """
    Automated directory sweep system for SwarmHub. Crawls scraped open-source 
    agent asset directories, runs individual metadata classification pipelines, 
    and bundles outputs into a unified global discovery registry array index.
    """
    def __init__(self, target_repo_root: str, github_username: str = "martinkovacevic"):
        self.repo_root = target_repo_root
        self.github_username = github_username
        self.classifier = LlamaMetadataClassifier()
        self.master_catalog_path = os.path.join("dist", "registry", "registry_index.json")

    def run_mass_ingestion(self) -> None:
        agents_dir = os.path.join(self.repo_root, "agents")
        if not os.path.exists(agents_dir):
            raise FileNotFoundError(
                f"❌ Could not find an active 'agents/' directory tree inside target reference: {self.repo_root}\n"
                f"👉 Make sure you have cloned 'ashishpatel26/500-AI-Agents-Projects' locally."
            )

        print(f"🚀 SwarmHub Ingestion Engine Booted.")
        print(f"📂 Scanning subdirectory modules inside target tree: {agents_dir}\n")

        # Capture list of immediate child paths to prevent infinitely looping deep subfolders
        agent_folders = sorted([
            os.path.join(agents_dir, d) for d in os.listdir(agents_dir)
            if os.path.isdir(os.path.join(agents_dir, d)) and not d.startswith(".")
        ])

        total_discovered = len(agent_folders)
        print(f"📊 Identified {total_discovered} distinct multi-agent project workloads ready for indexing.\n")
        print("=" * 90)

        catalog_index_records = []

        for index, folder_path in enumerate(agent_folders, start=1):
            folder_name = os.path.basename(folder_path)
            print(f"🛰️  [Processing Batch {index}/{total_discovered}] -> Working on: {folder_name}")

            try:
                # 1. Trigger the Llama 3.2 Metadata Classifier to output 'blob.json'
                self.classifier.classify_agent_directory(
                    local_folder=folder_path,
                    repository_base_url="https://github.com/ashishpatel26/500-AI-Agents-Projects",
                    github_username=self.github_username
                )

                # 2. Extract the newly written local manifest data losslessly
                manifest_file_path = os.path.join(folder_path, "blob.json")
                if os.path.exists(manifest_file_path):
                    with open(manifest_file_path, "r", encoding="utf-8") as f:
                        record_data = json.load(f)
                    catalog_index_records.append(record_data)
                    print(f"✅ Successfully cataloged and index-mapped: {folder_name}\n")
                else:
                    print(f"⚠️  Warning: Manifest was missing for {folder_name} despite completed run pass.\n")

            except Exception as err:
                print(f"❌ Error encountered processing sub-module folder reference [{folder_name}]: {err}")
                print("⏭️  Skipping corrupted asset layout block safely to protect execution queue continuity...\n")
                print("-" * 80)
                continue

        # 3. Compile individual outputs down into a unified search optimization database array file
        os.makedirs(os.path.dirname(self.master_catalog_path), exist_ok=True)
        with open(self.master_catalog_path, "w", encoding="utf-8") as out_f:
            json.dump(catalog_index_records, out_f, indent=4)

        print("=" * 90)
        print(f"🏁 Global Multi-Agent Index Synchronization Finished Successfully!")
        print(f"💾 Centralized Search Index written to target: {self.master_catalog_path}")
        print(f"💎 Total High-Tier Solutions Live on Registry Marketplace: {len(catalog_index_records)} Agents")

if __name__ == "__main__":
    # Local Testing Loop Execution Configuration Gate
    # To test this against real-world assets, clone Ashish's repo down onto your machine:
    # Git Command: git clone https://github.com/ashishpatel26/500-AI-Agents-Projects.git /tmp/500-agents
    
    mock_source_tree = "tools/ingestion/mock_scraped_repository"
    mock_agents_track = os.path.join(mock_source_tree, "agents")
    
    # Generate 3 separate synthetic target project directories to simulate real batch passes
    mock_agent_samples = ["01-crypto-trading-swarm", "02-clinical-trial-grader", "03-legal-contract-compiler"]
    for sample in mock_agent_samples:
        path = os.path.join(mock_agents_track, sample)
        os.makedirs(path, exist_ok=True)
        with open(os.path.join(path, "agent.py"), "w") as f:
            f.write("def run(state):\n    return state")
        with open(os.path.join(path, "README.md"), "w") as f:
            f.write(f"# {sample.replace('-', ' ').title()}\nAutomated pipeline for processing open datasets.")

    print("🧪 Simulating structural multi-directory ingestion pass sweep...")
    crawler = BulkRegistryCrawler(target_repo_root=mock_source_tree)
    crawler.run_mass_ingestion()