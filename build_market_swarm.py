from swarmhub.core.builder import SwarmWorkflow
from swarmhub.emitters.langgraph import LangGraphEmitter
from swarmhub.emitters.crewai import CrewAIEmitter
from swarmhub.emitters.autogen import AutoGenEmitter

print("🛠️  Constructing Production Market Research & Copywriting Swarm...")

workflow = (
    SwarmWorkflow(name="market-intelligence-swarm")
    .configure_runtime(provider="openai", model="gpt-4o", temperature=0.1)
    
    # 1. Enforce a rigorous global context data contract schema layout
    .set_state_schema({
        "target_topic": "str",
        "raw_metrics": "str",
        "final_copy": "str"
    })
    
    # 2. Register our execution steps and assign their localized code blobs
    .add_step(
        node_id="data_fetcher", 
        executor_reference="blobs/fetcher.py", 
        is_entry_point=True, 
        tools=["database_query"]
    )
    .add_step(
        node_id="data_writer", 
        executor_reference="blobs/writer.py", 
        tools=["web_search"]
    )
    
    # 3. Establish directional execution channels between the actors
    .add_route(from_node="data_fetcher", to_node="data_writer", condition_trigger="PROCEED")
)

# Build our finalized spec blueprint contract object
blueprint = workflow.build_spec()

print("🎛️  Compiling across all three upgraded runtime emitters...")
LangGraphEmitter(blueprint).write_to_disk("dist/market_langgraph.py")
CrewAIEmitter(blueprint).write_to_disk("dist/market_crew.py")
AutoGenEmitter(blueprint).write_to_disk("dist/market_autogen.py")

print("\n🎉 Architecture compilation pass completely successful!")