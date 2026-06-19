import os
import urllib.request
import json
import shutil
from pydantic import BaseModel, Field
from typing import Dict, List

class BlobManifest(BaseModel):
    """
    The structural contract declaration required for every shareable community blob.
    """
    name: str = Field(..., description="The unique name slug of the community blob, e.g., 'llm-cost-optimizer'")
    version: str = Field("0.1.0", description="Semantic version string")
    description: str = Field(..., description="Explanation of what task this cognitive logic solves")
    required_context: Dict[str, str] = Field(
        default_factory=dict, 
        description="The keys and types the blob expects to find in the state context on entry"
    )
    produced_context: Dict[str, str] = Field(
        default_factory=dict, 
        description="The keys and types this blob guarantees to append or modify on exit"
    )

class RegistryEngine:
    """
    The package manager engine for SwarmHub. Downloads, validates,
    and mounts shared cognitive blocks from any public GitHub repository.
    """
    @classmethod
    def install_blob(cls, package_handle: str) -> None:
        parts = package_handle.strip().split('/')
        if len(parts) != 3:
            raise ValueError(
                "❌ Invalid package identifier format!\n"
                "👉 Expected syntax: owner/repository/blob_slug\n"
                "💡 Example: ragnarlothbrock/SwarmHub-Registry/llm-cost-optimizer"
            )
            
        owner, repo, blob_slug = parts
        print(f"📡 Connecting to GitHub CDN for registry workspace: {owner}/{repo}...")
        print(f"🔍 Fetching active cognitive token: '{blob_slug}'...")
        
        base_url = f"https://raw.githubusercontent.com/{owner}/{repo}/main/blobs/{blob_slug}"
        manifest_url = f"{base_url}/blob.json"
        code_url = f"{base_url}/{blob_slug}.py"
        
        try:
            with urllib.request.urlopen(manifest_url, timeout=5) as response:
                manifest_data = json.loads(response.read().decode())
                manifest = BlobManifest(**manifest_data)
                
            print(f"📦 Found verified package: {manifest.name} (v{manifest.version})")
            print(f"ℹ️  Description: {manifest.description}")
            
            with urllib.request.urlopen(code_url, timeout=5) as response:
                code_content = response.read().decode()
                
            os.makedirs("blobs", exist_ok=True)
            target_code_path = os.path.join("blobs", f"{blob_slug}.py")
            target_manifest_path = os.path.join("blobs", f"{blob_slug}.json")
            
            with open(target_code_path, "w") as f:
                f.write(code_content)
                
            with open(target_manifest_path, "w") as f:
                f.write(json.dumps(manifest.model_dump(), indent=4))
                
            print(f"🟢 Success! Installed '{blob_slug}' cleanly into your workspace.")
            print(f"👉 Code written to: {target_code_path}")
            if manifest.required_context:
                print(f"🔑 Required context parameters: {list(manifest.required_context.keys())}")
                
        except Exception as e:
            raise RuntimeError(
                f"❌ Failed to resolve package '{blob_slug}' from repository '{owner}/{repo}'.\n"
                f"⚠️  Ensure the target repository is public and contains the files under 'blobs/{blob_slug}/'.\n"
                f"📌 Details: {e}"
            )


class PublisherEngine:
    """
    The publishing wizard subsystem for SwarmHub. Guides developers through
    packaging, documenting, and pre-formatting blobs for repository registration.
    """
    @staticmethod
    def _parse_contract_input(raw_input: str) -> Dict[str, str]:
        """Helper to convert user string inputs 'key:type, key:type' into structured dicts."""
        contract = {}
        if not raw_input.strip():
            return contract
        
        pairs = raw_input.split(",")
        for pair in pairs:
            if ":" in pair:
                k, v = pair.split(":", 1)
                contract[k.strip()] = v.strip()
            else:
                # Fallback default type to string if unspecified
                contract[pair.strip()] = "str"
        return contract

    @classmethod
    def package_blob(cls, source_file_path: str) -> None:
        """
        Runs an interactive CLI wizard to generate standard schema declarations,
        creates a validated manifest, and stages a deployment ready asset folder.
        """
        if not os.path.exists(source_file_path) or not source_file_path.endswith(".py"):
            raise FileNotFoundError(f"❌ Target path '{source_file_path}' must be a valid, existing local .py code asset.")

        print("\n📦 SwarmHub Hub of Blobs Packaging Assistant Initialized.")
        print("💡 Let's prepare your custom cognitive module for global open-source release!\n")

        # 1. Gather descriptive metadata interactively
        raw_name = input("🏷️  Enter unique blob name slug (e.g., 'llm-cost-optimizer'): ").strip()
        blob_slug = raw_name.replace(" ", "-").lower() if raw_name else "unnamed-blob"
        
        version = input("🔄 Enter version string [0.1.0]: ").strip() or "0.1.0"
        description = input("ℹ️  Enter a brief description of what task this logic solves: ").strip() or "No description provided."

        print("\n🔑 Data Contract Declarations (Format as comma separated list 'key_id:type')")
        print("👉 Example: 'customer_id:str, account_balance:float'")
        
        req_raw = input("📥 Required incoming context keys (Leave empty if none): ").strip()
        prod_raw = input("📤 Guaranteed outgoing/modified context keys (Leave empty if none): ").strip()

        required_context = cls._parse_contract_input(req_raw)
        produced_context = cls._parse_contract_input(prod_raw)

        # 2. Build and validate our baseline manifest model
        manifest = BlobManifest(
            name=blob_slug,
            version=version,
            description=description,
            required_context=required_context,
            produced_context=produced_context
        )

        # 3. Create a staged, clean release layout folder for easy export/git commits
        staging_dir = os.path.join("dist", "registry", blob_slug)
        os.makedirs(staging_dir, exist_ok=True)

        target_code_path = os.path.join(staging_dir, f"{blob_slug}.py")
        target_json_path = os.path.join(staging_dir, "blob.json")

        # Copy original code into renamed destination handle
        shutil.copyfile(source_file_path, target_code_path)

        # Write clean manifest model metadata layout file
        with open(target_json_path, "w") as f:
            f.write(json.dumps(manifest.model_dump(), indent=4))

        print(f"\n🟢 Success! Staged registry package prepared inside: {staging_dir}")
        print(f"📄 Generated Manifest: {target_json_path}")
        print(f"🐍 Processed Executable: {target_code_path}")
        print("\n🚀 Next Steps to push to 'The Hub of Blobs':")
        print(f" 1. Copy the folder '{staging_dir}' into your public git registry asset tree under 'blobs/'.")
        print(" 2. Execute: git add . && git commit -m 'Release package' && git push")
        print(f" 3. Other users can now download your creation using:\n    👉 swarmhub install <your_username>/<your_repo>/{blob_slug}\n")