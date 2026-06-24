import argparse
import sys
import os
import json
import shutil
from swarmhub.parsers.langgraph import LangGraphParser
from swarmhub.parsers.crewai import CrewAIParser
from swarmhub.parsers.autogen import AutoGenParser
from swarmhub.parsers.pydanticai import PydanticAIParser
from swarmhub.emitters.langgraph import LangGraphEmitter
from swarmhub.emitters.crewai import CrewAIEmitter
from swarmhub.emitters.autogen import AutoGenEmitter
from swarmhub.core.linker import SwarmLinker
from swarmhub.core.spec import WorkflowNode
from swarmhub.core.registry import RegistryEngine, PublisherEngine

def run_cli():
    parser = argparse.ArgumentParser(
        description="🐝 SwarmHub CLI: The Universal Abstract Cross-Compiler and Package Manager for AI Agents."
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Available sub-commands")
    
    # --- SUB-COMMAND 1: swarmhub compile ---
    compile_parser = subparsers.add_parser("compile", help="Cross-compile between agent framework layouts.")
    compile_parser.add_argument(
        "--source", "-s", required=True, 
        help="Path to the legacy agent framework source file (e.g., source_graph.py)"
    )
    compile_parser.add_argument(
        "--from-framework", "-f", choices=["langgraph", "crewai", "autogen", "pydanticai"], default="langgraph",
        help="The source framework type to parse up from"
    )
    compile_parser.add_argument(
        "--target", "-t", choices=["langgraph", "crewai", "autogen"], required=True,
        help="The target framework deployment codebase to emit down to"
    )
    compile_parser.add_argument(
        "--output", "-o", required=True,
        help="The output file destination path for the compiled native asset"
    )
    compile_parser.add_argument(
        "--inject-guardrail", action="store_true",
        help="Surgical Mutation Flag: Inject an automated data security guardrail node"
    )
    compile_parser.add_argument(
        "--inline", action="store_true",
        help="Optimization Flag: Inlines and absorbs isolated code blobs directly back into a single unified script asset"
    )

    # --- SUB-COMMAND 2: swarmhub install ---
    install_parser = subparsers.add_parser("install", help="Download a shared cognitive blob from a decentralized public GitHub registry repository.")
    install_parser.add_argument(
        "package_handle", type=str,
        help="The repository destination target layout string formatted as: 'owner/repository/blob_slug'"
    )

    # --- SUB-COMMAND 3: swarmhub publish ---
    publish_parser = subparsers.add_parser("publish", help="Package a local cognitive Python file into a shareable registry asset manifest.")
    publish_parser.add_argument(
        "blob_path", type=str,
        help="Path to the targeted local Python code blob file (e.g., 'blobs/fetcher.py')"
    )

    # --- SUB-COMMAND 4: swarmhub list ---
    list_parser = subparsers.add_parser("list", help="List and browse all indexed multi-agent workflows in the marketplace registry index.")
    list_parser.add_argument(
        "--framework", "-f", help="Filter indexed marketplace solutions by original codebase framework type."
    )

    # --- SUB-COMMAND 5: swarmhub unpack ---
    unpack_parser = subparsers.add_parser("unpack", help="Unpack a pre-compiled cross-framework agent portfolio asset directly into your local directory tree.")
    unpack_parser.add_argument(
        "agent_slug", type=str,
        help="The slug identifier of the target solution codebase (e.g., 'web-research-agent')"
    )
    unpack_parser.add_argument(
        "--target", "-t", choices=["langgraph", "crewai", "autogen"], required=True,
        help="The pre-compiled architecture runtime paradigm to extract from the matrix"
    )
    unpack_parser.add_argument(
        "--output", "-o", default=".",
        help="The destination workspace folder path to drop the unpacked agent codebase (defaults to current directory)"
    )

    args = parser.parse_args()

    # --- CLI UTILITY ROUTING LAYER ---
    if args.command == "install":
        try:
            RegistryEngine.install_blob(args.package_handle)
        except Exception as e:
            print(e)
            sys.exit(1)
        return

    elif args.command == "publish":
        try:
            PublisherEngine.package_blob(args.blob_path)
        except Exception as e:
            print(e)
            sys.exit(1)
        return

    elif args.command == "list":
        index_path = "dist/registry/registry_index.json"
        if not os.path.exists(index_path):
            print("❌ SwarmHub Registry Error: Ground-truth index metadata file missing at: dist/registry/registry_index.json")
            print("   Please execute the target multi-pass ingestion tooling pipelines first.")
            sys.exit(1)
            
        try:
            with open(index_path, "r", encoding="utf-8") as f:
                agents = json.load(f)
        except Exception as e:
            print(f"❌ Error loading marketplace registry index data: {e}")
            sys.exit(1)
            
        print("\n" + "=" * 105)
        print("🐝 SWARMHUB MULTI-FRAMEWORK AGENT WORKFORCE MARKETPLACE")
        print("=" * 105)
        print(f"{'AGENT SLUG (UNPACK KEY)':<32} | {'DISPLAY NAME':<40} | {'FRAMEWORK':<12} | {'INDUSTRY'}")
        print("-" * 105)
        
        match_count = 0
        for agent in agents:
            slug = agent.get("registry_handle", "").split("/")[-1]
            display_name = agent.get("display_name", "Unnamed Agent Asset")
            orig_framework = agent.get("filters", {}).get("original_framework", "Generic")
            industry = agent.get("filters", {}).get("industry", "Research & Development")
            
            if args.framework and args.framework.lower() != orig_framework.lower():
                continue
                
            print(f"{slug:<32} | {display_name:<40} | {orig_framework:<12} | {industry}")
            match_count += 1
            
        print("=" * 105)
        print(f"💎 Grand Total High-Tier Accessible Solutions Matching Query: {match_count}/{len(agents)} Agents\n")
        return

    elif args.command == "unpack":
        target_slug = args.agent_slug.lower().strip()
        target_fw = args.target.lower().strip()
        
        compiled_source_dir = os.path.join("dist", "compiled", target_fw, target_slug)
        expected_target_file = os.path.join(compiled_source_dir, f"swarmhub_{target_fw}.py")
        
        if not os.path.exists(expected_target_file):
            print(f"❌ Unpack Error: Could not locate compiled script matrix for target agent slug key [{target_slug}].")
            print(f"   Missing Target Verification Path: {expected_target_file}")
            sys.exit(1)
            
        try:
            os.makedirs(args.output, exist_ok=True)
            
            # Scaffold and unpack all matching structural portfolio resources
            for file_item in os.listdir(compiled_source_dir):
                source_item_path = os.path.join(compiled_source_dir, file_item)
                
                # Turn cross-compiled architecture scripts seamlessly into ready-to-run main entries
                if file_item == f"swarmhub_{target_fw}.py":
                    destination_item_name = "main.py"
                else:
                    destination_item_name = file_item
                    
                destination_item_path = os.path.join(args.output, destination_item_name)
                if os.path.isfile(source_item_path):
                    shutil.copy(source_item_path, destination_item_path)
                    
            print(f"\n🟢 Success! Cross-compiled agent layout assets for [{target_slug}] extracted safely.")
            print(f"📂 Workspace Target Path: {os.path.abspath(args.output)}")
            print(f"🚀 To execute this system immediately via native {args.target}, run: python3 {args.output}/main.py\n")
            
        except Exception as e:
            print(f"❌ Strategic Scaffolding Exception: Failed to unpack source bundle paths: {e}")
            sys.exit(1)
        return

    elif args.command == "compile" or (args.command is None and hasattr(args, "source")):
        source_target = args.source if hasattr(args, "source") else None
        if not source_target:
            parser.print_help()
            sys.exit(0)
            
        try:
            with open(args.source, "r") as f:
                source_code = f.read()
        except Exception as e:
            print(f"❌ Error reading source file '{args.source}': {e}")
            sys.exit(1)

        print(f"📖 Parsing legacy code via structural AST from: {args.source}...")
        if args.from_framework == "langgraph":
            blueprint = LangGraphParser(source_code, agent_name="cli-compiled-swarm").parse()
        elif args.from_framework == "crewai":
            blueprint = CrewAIParser(source_code, agent_name="cli-compiled-swarm").parse()
        elif args.from_framework == "autogen":
            blueprint = AutoGenParser(source_code, agent_name="cli-compiled-swarm").parse()
        elif args.from_framework == "pydanticai":
            blueprint = PydanticAIParser(source_code, agent_name="cli-compiled-swarm").parse()

        if args.inject_guardrail:
            print("🧬 Injecting automated 'data_guardrail_filter' node into intermediate spec...")
            node_ids = {n.id for n in blueprint.topology.nodes}
            if "input_harvester" in node_ids and "pii_sanitizer" in node_ids:
                guardrail_step = WorkflowNode(
                    id="cli_data_guardrail_filter",
                    executor_type="opaque_blob",
                    executor_reference="blobs/cli_guardrail.py"
                )
                blueprint = SwarmLinker.inject_node_between(
                    spec=blueprint, source_node_id="input_harvester",
                    target_node_id="pii_sanitizer", new_node=guardrail_step,
                    adapter_condition="CLI_GUARDRAIL_PASSED"
                )

        inline_mode = getattr(args, "inline", False)

        print(f"🎛️ Transpiling intermediate specification down into target: '{args.target}' (Inline Mode: {inline_mode})...")
        if args.target == "langgraph":
            emitter = LangGraphEmitter(blueprint, inline_blobs=inline_mode)
        elif args.target == "crewai":
            emitter = CrewAIEmitter(blueprint, inline_blobs=inline_mode)
        elif args.target == "autogen":
            emitter = AutoGenEmitter(blueprint, inline_blobs=inline_mode)

        emitter.write_to_disk(args.output)
        print(f"🏁 Compilation complete! SwarmHub successfully generated: {args.output}\n")
    else:
        parser.print_help()

if __name__ == "__main__":
    run_cli()