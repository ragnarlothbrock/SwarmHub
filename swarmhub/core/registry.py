import os
import ast
import urllib.request
import json
import shutil
from pydantic import BaseModel, Field
from typing import Dict, List, Optional

class PackageManifest(BaseModel):
    """
    The unified structural contract declaration managing both atomic cognitive 
    bricks and complete multi-agent architectural workloads.
    """
    name: str = Field(..., description="Unique slug identifier of the asset, e.g., 'advanced-corrective-rag'")
    version: str = Field("0.1.0", description="Semantic version string tracking release states")
    type: str = Field("brick", description="The classification layer: either 'brick' or 'workload'")
    description: str = Field(..., description="High-level description summarizing what problem this logic solves")
    
    # Brick Specific Schema Contracts
    required_context: Optional[Dict[str, str]] = Field(
        default_factory=dict, 
        description="The precise keys and type primitives expected on state entry"
    )
    produced_context: Optional[Dict[str, str]] = Field(
        default_factory=dict, 
        description="The keys and type primitives this node guarantees to exit with"
    )
    
    # Workload Specific Dependency Layouts
    composition_blueprint: Optional[str] = Field(
        None, description="The primary execution entry file (e.g., examples/advanced_rag_swarm.py)"
    )
    dependencies: Optional[Dict[str, str]] = Field(
        default_factory=dict, 
        description="A map pairing local workspace destinations with remote raw repository paths"
    )

class BaseRegistryLinter:
    """Helper component that uses the AST core engine to validate cognitive function contracts."""
    @staticmethod
    def _lint_source_code(source_code: str, identifier: str) -> bool:
        try:
            tree = ast.parse(source_code)
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef) and node.name == "run":
                    if len(node.args.args) == 1:
                        return True
            print(f"   ❌ [Lint Failure] '{identifier}' violates the universal contract!")
            print("      👉 Reason: Missing a valid 'def run(state):' execution gate signature.")
            return False
        except Exception as e:
            print(f"   ❌ [AST Analysis Error] Could not compile source structure tokens: {e}")
            return False

class RegistryEngine(BaseRegistryLinter):
    """
    The decentralized package manager engine for SwarmHub. Downloads, validates,
    and automatically unpacks complex agent workloads or single atomic bricks from GitHub.
    """
    @classmethod
    def install_blob(cls, package_handle: str) -> None:
        parts = package_handle.strip().split('/')
        if len(parts) != 3:
            raise ValueError(
                "❌ Invalid package identifier format!\n"
                "👉 Expected syntax: owner/repository/blob_slug\n"
                "💡 Example: martinkovacevic/SwarmHub-Registry/advanced-corrective-rag"
            )
            
        owner, repo, blob_slug = parts
        print(f"📡 Connecting to GitHub CDN for workspace environment: {owner}/{repo}...")
        
        base_url = f"https://raw.githubusercontent.com/{owner}/{repo}/main/blobs/{blob_slug}"
        manifest_url = f"{base_url}/blob.json"
        
        try:
            # 1. Fetch package metadata blueprint layout file
            with urllib.request.urlopen(manifest_url, timeout=7) as response:
                manifest_data = json.loads(response.read().decode())
                manifest = PackageManifest(**manifest_data)
                
            print(f"📦 Package verified: {manifest.name} (v{manifest.version}) [{manifest.type.upper()}]")
            print(f"ℹ️  Description: {manifest.description}")
            
            # 2. Branch processing execution logic based on manifest classification types
            if manifest.type == "brick":
                code_url = f"{base_url}/{blob_slug}.py"
                with urllib.request.urlopen(code_url, timeout=5) as response:
                    code_content = response.read().decode()
                    
                if not cls._lint_source_code(code_content, blob_slug):
                    raise RuntimeError("Downloaded community brick asset failed structural contract requirements.")
                    
                os.makedirs("blobs", exist_ok=True)
                target_code_path = os.path.join("blobs", f"{blob_slug}.py")
                target_manifest_path = os.path.join("blobs", f"{blob_slug}.json")
                
                with open(target_code_path, "w") as f:
                    f.write(code_content)
                with open(target_manifest_path, "w") as f:
                    f.write(json.dumps(manifest.model_dump(exclude_none=True), indent=4))
                    
                print(f"🟢 Success! Isolated brick asset installed to: {target_code_path}")
                
            elif manifest.type == "workload":
                print(f"🏗️  Unpacking composite swarm workload structure... ({len(manifest.dependencies or {})} files)")
                
                # Fetch dependencies mapped to their relative repository coordinates
                for local_dest, repo_rel_path in (manifest.dependencies or {}).items():
                    file_download_url = f"https://raw.githubusercontent.com/{owner}/{repo}/main/{repo_rel_path}"
                    print(f"   📥 Downloading component path: {repo_rel_path}")
                    
                    with urllib.request.urlopen(file_download_url, timeout=5) as response:
                        file_content = response.read().decode()
                        
                    # If downloading a logic blob script file, run the core contract check
                    if repo_rel_path.startswith("blobs/") and repo_rel_path.endswith(".py"):
                        cls._lint_source_code(file_content, os.path.basename(repo_rel_path))
                        
                    # Create directory layout paths dynamically to isolate targets safely
                    os.makedirs(os.path.dirname(local_dest), exist_ok=True)
                    with open(local_dest, "w") as f:
                        f.write(file_content)
                        
                print(f"🟢 Success! Full agentic workload unpacked cleanly into workspace root targets.")
                if manifest.composition_blueprint:
                    print(f"👉 Next Steps: Open and configure master orchestration map script at: {manifest.composition_blueprint}")
                    
        except Exception as e:
            raise RuntimeError(
                f"❌ Failed to resolve package path '{blob_slug}' from remote location tracking channel.\n"
                f"📌 Error Tracking ID: {e}"
            )

class PublisherEngine(BaseRegistryLinter):
    """
    The publishing wizard subsystem for SwarmHub. Guides developers through
    packaging, documenting, and formatting single files or full multi-agent workloads.
    """
    @staticmethod
    def _parse_contract_input(raw_input: str) -> Dict[str, str]:
        contract = {}
        if not raw_input.strip():
            return contract
        pairs = raw_input.split(",")
        for pair in pairs:
            if ":" in pair:
                k, v = pair.split(":", 1)
                contract[k.strip()] = v.strip()
            else:
                contract[pair.strip()] = "str"
        return contract

    @classmethod
    def package_blob(cls, source_path: str) -> None:
        """
        Runs an interactive CLI wizard to generate standard schema declarations,
        creates a validated manifest, and stages a deployment ready asset folder.
        """
        if not os.path.exists(source_path):
            raise FileNotFoundError(f"❌ Target path reference '{source_path}' does not exist inside active directory tree.")

        # Determine structural processing branches automatically via path analysis parameters
        is_directory = os.path.isdir(source_path)
        pkg_type = "workload" if is_directory else "brick"
        
        print(f"\n📦 SwarmHub Hub of Blobs Packaging Assistant Initialized [{pkg_type.upper()} MODE].")
        print("💡 Let's prepare your custom multi-agent assets for global open-source release!\n")

        if not is_directory:
            # Atomic Brick Compilation Strategy Trace
            with open(source_path, "r") as f:
                local_code_str = f.read()
            print(f"🔍 Pre-linting module functions signature track: {source_path}")
            if not cls._lint_source_code(local_code_str, os.path.basename(source_path)):
                print("\n⚠️  [Publish Blocked] Refusing to package code that breaks runtime specifications.")
                return

        # 1. Collect baseline metadata values across all packages
        raw_name = input("🏷️  Enter unique asset name slug (e.g., 'advanced-corrective-rag'): ").strip()
        blob_slug = raw_name.replace(" ", "-").lower() if raw_name else "unnamed-package"
        version = input("🔄 Enter version string [0.1.0]: ").strip() or "0.1.0"
        description = input("ℹ️  Enter a brief description of what task this agentic layer solves: ").strip() or "No description."

        dependencies_map = {}
        blueprint_file = None
        required_context = {}
        produced_context = {}

        if is_directory:
            # 2a. Execute Workload Auto-Scanning Discovery Loop Pass
            print("\n📂 Scanning targeted workload directory files recursively for staging preparation...")
            blueprint_file = input("🎮 Enter relative path to master composition orchestrator [examples/advanced_rag_swarm.py]: ").strip() or "examples/advanced_rag_swarm.py"
            
            # Automatically catalog everything inside the directory to make deployment turn-key
            for root, _, files in os.walk(source_path):
                for file in files:
                    # Avoid capturing git configurations or local sqlite cache outputs
                    if any(x in root for x in [".git", "__pycache__", ".venv", "dist/registry"]):
                        continue
                    if file.endswith((".db", ".db-journal", ".DS_Store")):
                        continue
                        
                    full_local_path = os.path.join(root, file)
                    dependencies_map[full_local_path] = full_local_path
                    
            # Explicitly include the composition script path to avoid missing deployment files
            if os.path.exists(blueprint_file):
                dependencies_map[blueprint_file] = blueprint_file

        else:
            # 2b. Collect structural contract details for single node bricks
            print("\n🔑 Data Contract Declarations (Format as comma separated list 'key_id:type')")
            req_raw = input("📥 Required incoming context keys (Leave empty if none): ").strip()
            prod_raw = input("📤 Guaranteed outgoing/modified context keys (Leave empty if none): ").strip()
            required_context = cls._parse_contract_input(req_raw)
            produced_context = cls._parse_contract_input(prod_raw)

        # 3. Assemble unified model architecture manifest blueprint parameters
        manifest = PackageManifest(
            name=blob_slug,
            version=version,
            type=pkg_type,
            description=description,
            required_context=required_context if pkg_type == "brick" else None,
            produced_context=produced_context if pkg_type == "brick" else None,
            composition_blueprint=blueprint_file,
            dependencies=dependencies_map if pkg_type == "workload" else None
        )

        # 4. Generate clean staged release target folders
        staging_dir = os.path.join("dist", "registry", blob_slug)
        os.makedirs(staging_dir, exist_ok=True)
        target_json_path = os.path.join(staging_dir, "blob.json")

        if pkg_type == "brick":
            target_code_path = os.path.join(staging_dir, f"{blob_slug}.py")
            shutil.copyfile(source_path, target_code_path)
        else:
            # Deep mirror structural files straight into localized registry folder blocks
            for local_src in dependencies_map.keys():
                dest_staged_path = os.path.join(staging_dir, local_src)
                os.makedirs(os.path.dirname(dest_staged_path), exist_ok=True)
                shutil.copyfile(local_src, dest_staged_path)

        with open(target_json_path, "w") as f:
            f.write(json.dumps(manifest.model_dump(exclude_none=True), indent=4))

        print(f"\n🟢 Success! Staged registry package prepared inside: {staging_dir}")
        print(f"📄 Generated Package Manifest Metadata: {target_json_path}")
        print("\n🚀 Next Steps to push your package to the SwarmHub Registry:")
        print(f" 1. Copy the folder contents of '{staging_dir}' into your public git repository asset tree under 'blobs/{blob_slug}/'.")
        print(" 2. Execute: git add . && git commit -m 'Publish package workforce stack' && git push")
        print(f" 3. The community can now pull down your setup instantly using:\n    👉 swarmhub install <your_username>/<your_repo_name>/{blob_slug}\n")