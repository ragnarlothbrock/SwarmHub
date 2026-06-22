import os
from swarmhub.core.builder import SwarmWorkflow
from swarmhub.emitters.langgraph import LangGraphEmitter
from swarmhub.emitters.crewai import CrewAIEmitter
from swarmhub.emitters.autogen import AutoGenEmitter

def build_and_compile_advanced_rag():
    print("🐝 SwarmHub Orchestration Engine: Assembling Advanced RAG Blueprint...")

    # 1. Initialize the workflow canvas
    workflow = SwarmWorkflow(name="advanced-corrective-rag-swarm")

    # 2. Configure the cognitive runtime to target our local Ollama server engine
    # Both our emitters and blobs will hit this model context target
    workflow.configure_runtime(
        provider="openai",  # Tells the downstream framework to use an OpenAI-compatible API format
        model="llama3.2:3b",
        temperature=0.1
    )

    # 3. Mount an Abstract Persistent Memory Layer Checkpointer
    # Isolated inside the advanced_rag folder to keep database artifacts organized
    workflow.configure_memory(
        backend="sqlite",
        thread_id="local-rag-session-001",
        connection_string="dist/advanced_rag/rag_memory_vault.db"
    )

    # 4. Register a Global External Model Context Protocol (MCP) Server
    # ✅ FIXED: Corrected path alignment from tools/ to tools/advanced_rag/
    workflow.register_mcp_server(
        name="vector_store_service",
        transport="stdio",
        endpoint="python",
        args=["tools/advanced_rag/vector_service_daemon.py"]
    )

    # 5. Define a Strict, Type-Safe Global Context State Contract Schema
    # This prevents smaller local models (1B-3B) from introducing data typos across transitions
    workflow.set_state_schema({
        "user_query": "str",         # The static user payload question
        "search_query": "str",       # The dynamically optimized query variant
        "retrieved_chunks": "str",   # Accumulator string holding context data hits
        "grade_status": "str",       # Multi-branch routing decision flag ("RELEVANT" / "IRRELEVANT")
        "loop_counter": "int"        # Loop breaker circuit mechanism to stop hallucinations
    })

    # 6. Append Workflow Execution Hops Tied to Organized Namespace Subdirectories
    # We restrict the vector server access exclusively to the retriever via the interfaces tag
    workflow.add_step(
        node_id="document_retriever",
        executor_reference="blobs/advanced_rag/rag_retriever.py",
        is_entry_point=True,
        interfaces=["vector_store_service"]
    )
    
    workflow.add_step(
        node_id="context_grader",
        executor_reference="blobs/advanced_rag/rag_grader.py"
    )
    
    workflow.add_step(
        node_id="query_rewriter",
        executor_reference="blobs/advanced_rag/rag_rewriter.py"
    )
    
    workflow.add_step(
        node_id="synthesis_generator",
        executor_reference="blobs/advanced_rag/rag_generator.py"
    )

    # 7. Wire Up Non-Linear Feedback Loops & Adaptive Conditional Transitions
    # Step A: Retriever always pipes straight into the grader
    workflow.add_route(from_node="document_retriever", to_node="context_grader", condition_trigger="PROCEED")

    # Step B: Grader reads model scoring and forks the orchestration highway path
    workflow.add_route(from_node="context_grader", to_node="synthesis_generator", condition_trigger="SYNTHESIZE")
    workflow.add_route(from_node="context_grader", to_node="query_rewriter", condition_trigger="REWRITE")

    # Step C: Rewriter updates search conditions and routes back to retriever to try again
    workflow.add_route(from_node="query_rewriter", to_node="document_retriever", condition_trigger="RETRY")

    # 8. Compile the Universal Agent Contract Spec Blueprint
    universal_spec = workflow.build_spec()
    print("✨ Specification built successfully! Data structural boundaries validated.")

    # 9. Cross-Compile to All Target Frameworks on the Fly
    print("\n🖥️  Cross-Compiling Multi-Target Deployment Architectures...")
    
    # ✅ UPDATED: Shifted execution targeting parameters directly into dist/advanced_rag/
    target_dir = "dist/advanced_rag"
    os.makedirs(target_dir, exist_ok=True)

    # Compile Target A: Native LangGraph State Machine
    lg_out = os.path.join(target_dir, "compiled_rag_langgraph.py")
    LangGraphEmitter(universal_spec).write_to_disk(lg_out)

    # Compile Target B: Sequential Task-Driven CrewAI Workforce
    cr_out = os.path.join(target_dir, "compiled_rag_crewai.py")
    CrewAIEmitter(universal_spec).write_to_disk(cr_out)

    # Compile Target C: Conversational Participant AutoGen Chatroom Manager
    ag_out = os.path.join(target_dir, "compiled_rag_autogen.py")
    AutoGenEmitter(universal_spec).write_to_disk(ag_out)

    print(f"\n🏁 Compilation Complete! All target frameworks staged inside the {target_dir}/ directory.")

if __name__ == "__main__":
    build_and_compile_advanced_rag()