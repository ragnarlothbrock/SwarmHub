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

def run_cli():
    parser = argparse.ArgumentParser(
        description="🐝 SwarmHub CLI: The Universal Abstract Cross-Compiler for AI Agent Frameworks."
    )
    
    parser.add_argument(
        "--source", "-s", required=True, 
        help="Path to the legacy agent framework source file (e.g., source_graph.py)"
    )
    parser.add_argument(
        "--from-framework", "-f", choices=["langgraph", "crewai", "autogen"], default="langgraph",
        help="The source framework type to parse up from"
    )
    parser.add_argument(
        "--target", "-t", choices=["langgraph", "crewai", "autogen"], required=True,
        help="The target framework deployment codebase to emit down to"
    )
    parser.add_argument(
        "--output", "-o", required=True,
        help="The output file destination path for the compiled native asset"
    )
    parser.add_argument(
        "--inject-guardrail", action="store_true",
        help="Surgical Mutation Flag: Inject an automated data security guardrail node"
    )

    args = parser.parse_args()

    # 1. Read the input legacy code asset
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
    else:
        print("❌ Unsupported source framework.")
        sys.exit(1)

    # 3. Handle optional compilation-time structural mutations
    if args.inject_guardrail:
        print("🧬 Injecting automated 'data_guardrail_filter' node into intermediate spec...")
        # Check if the baseline model has our known stress-test configurations
        node_ids = {n.id for n in blueprint.topology.nodes}
        if "input_harvester" in node_ids and "pii_sanitizer" in node_ids:
            guardrail_step = WorkflowNode(
                id="cli_data_guardrail_filter",
                executor_type="opaque_blob",
                executor_reference="blobs/cli_guardrail.py",
                transitions=[]
            )
            blueprint = SwarmLinker.inject_node_between(
                spec=blueprint,
                source_node_id="input_harvester",
                target_node_id="pii_sanitizer",
                new_node=guardrail_step,
                adapter_condition="CLI_GUARDRAIL_PASSED"
            )
        else:
            print("⚠️ Skipping mutation: Standard 'input_harvester' -> 'pii_sanitizer' edge pattern not found.")

    # 4. Compile down into the requested target deployment framework
    print(f"🎛️ Transpiling intermediate specification down into target: '{args.target}'...")
    if args.target == "langgraph":
        emitter = LangGraphEmitter(blueprint)
    elif args.target == "crewai":
        emitter = CrewAIEmitter(blueprint)
    elif args.target == "autogen":
        emitter = AutoGenEmitter(blueprint)
    else:
        print("❌ Unsupported target emitter.")
        sys.exit(1)

    # 5. Write completed compiler asset to disk
    emitter.write_to_disk(args.output)
    print(f"🏁 Compilation complete! SwarmHub successfully generated: {args.output}\n")

if __name__ == "__main__":
    run_cli()