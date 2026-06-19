import argparse
import sys
from swarmhub.parsers.langgraph import LangGraphParser
from swarmhub.parsers.crewai import CrewAIParser
from swarmhub.parsers.autogen import AutoGenParser
from swarmhub.emitters.langgraph import LangGraphEmitter
from swarmhub.emitters.crewai import CrewAIEmitter
from swarmhub.emitters.autogen import AutoGenEmitter
from swarmhub.core.linker import SwarmLinker
from swarmhub.core.spec import WorkflowNode
from swarmhub.core.registry import RegistryEngine, PublisherEngine # Imported Publisher

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
        "--from-framework", "-f", choices=["langgraph", "crewai", "autogen"], default="langgraph",
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

    args = parser.parse_args()

    # Routing logic based on typed sub-commands
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