import os
import shutil
import pytest
from pydantic import ValidationError

from swarmhub.core.builder import SwarmWorkflow
from swarmhub.core.spec import UniversalAgentSpec, WorkflowNode, MemoryConfig, InterfaceConfig
from swarmhub.core.linker import SwarmLinker
from swarmhub.parsers.langgraph import LangGraphParser
from swarmhub.parsers.crewai import CrewAIParser
from swarmhub.parsers.autogen import AutoGenParser
from swarmhub.emitters.langgraph import LangGraphEmitter
from swarmhub.emitters.crewai import CrewAIEmitter
from swarmhub.emitters.autogen import AutoGenEmitter

# --- FIXTURES: SETUP & TEARDOWN RUNTIME SANDBOX ---
@pytest.fixture(scope="module", autouse=True)
def manage_sandbox_directories():
    """Dynamically sets up and tears down isolated mock test modules."""
    os.makedirs("blobs", exist_ok=True)
    os.makedirs("dist", exist_ok=True)
    
    # Inject a clean, standardized mock blob file for the execution pipelines to read
    mock_blob_content = (
        "def run(state):\n"
        "    state['context']['processed_by_blob'] = True\n"
        "    state['next_action'] = 'GOTO_PROCEED'\n"
        "    return state\n"
    )
    with open("blobs/test_blob.py", "w") as f:
        f.write(mock_blob_content)
        
    yield # Run all collected unit tests inside this envelope
    
    # Teardown: Clean up generated output after testing finishes
    if os.path.exists("dist"):
        shutil.rmtree("dist")


# --- UNIT & INTEGRATION TESTS ---

def test_fluent_sdk_and_validation_guardrails():
    """1. Validates SDK fluent design mechanics, memory checkpointers, and MCP registrations."""
    workflow = (
        SwarmWorkflow(name="pipeline-test")
        .set_state_schema({"user_id": "str", "internal_counter": "int"})
        .configure_memory(backend="sqlite", thread_id="thread-xyz-123", connection_string="test_memory.db")
        .register_mcp_server(name="secure_db", transport="stdio", endpoint="uvx", args=["mcp-server-db"])
        .add_step(
            node_id="harvester", 
            executor_reference="blobs/test_blob.py", 
            is_entry_point=True,
            interfaces=["secure_db"]
        )
        .add_step(node_id="sanitizer", executor_reference="blobs/test_blob.py")
        .add_route(from_node="harvester", to_node="sanitizer")
    )
    spec = workflow.build_spec()
    
    # Assert structural integrity definitions
    assert isinstance(spec, UniversalAgentSpec)
    assert spec.memory.storage_backend == "sqlite"
    assert spec.memory.thread_id == "thread-xyz-123"
    assert len(spec.interfaces) == 1
    assert spec.interfaces[0].name == "secure_db"
    assert spec.topology.nodes[0].interfaces == ["secure_db"]
    
    # Enforce initial pointer validation errors
    with pytest.raises(ValidationError):
        bad_flow = SwarmWorkflow(name="broken")
        bad_flow.initial_node = "ghost_identity"
        bad_flow.add_step(node_id="node_1", executor_reference="blobs/test_blob.py")
        bad_flow.build_spec()


def test_swarm_linker_interface_collision_and_permission_mutation():
    """2. Verifies linker merges interfaces, namespaces name collisions, and rewrites permissions."""
    workflow_a = (
        SwarmWorkflow(name="swarm-alpha")
        .register_mcp_server(name="shared_filesystem", transport="stdio", endpoint="node")
        .add_step(node_id="node_a", executor_reference="blobs/test_blob.py", interfaces=["shared_filesystem"], is_entry_point=True)
    )
    workflow_b = (
        SwarmWorkflow(name="swarm-beta")
        .register_mcp_server(name="shared_filesystem", transport="sse", endpoint="http://localhost")
        .add_step(node_id="node_a", executor_reference="blobs/test_blob.py", interfaces=["shared_filesystem"])
    )
    
    spec_a = workflow_a.build_spec()
    spec_b = workflow_b.build_spec()
    
    combined = SwarmLinker.combine(spec_a, spec_b, new_name="fused-swarm")
    
    # Assert nodes merged and deduplicated
    node_ids = {n.id for n in combined.topology.nodes}
    assert "node_a" in node_ids
    assert "swarm_beta_node_a" in node_ids
    
    # Assert global interfaces merged and namespaced on collision
    interface_names = {iface.name for iface in combined.interfaces}
    assert "shared_filesystem" in interface_names
    assert "swarm_beta_shared_filesystem" in interface_names
    
    # Assert node internal lease privileges permission handles updated cleanly
    beta_node = next(n for n in combined.topology.nodes if n.id == "swarm_beta_node_a")
    assert beta_node.interfaces == ["swarm_beta_shared_filesystem"]


def test_cross_framework_emitters_write_pass():
    """3. Tests that emitters compile schemas with complex memory and interface metrics successfully."""
    workflow = (
        SwarmWorkflow(name="multi-compile-target")
        .configure_memory(backend="sqlite", thread_id="tx-999")
        .register_mcp_server(name="file_server", transport="stdio", endpoint="python")
        .add_step(node_id="node_1", executor_reference="blobs/test_blob.py", interfaces=["file_server"])
    )
    spec = workflow.build_spec()
    
    lg_path = "dist/test_lg.py"
    cr_path = "dist/test_cr.py"
    ag_path = "dist/test_ag.py"
    
    LangGraphEmitter(spec).write_to_disk(lg_path)
    CrewAIEmitter(spec).write_to_disk(cr_path)
    AutoGenEmitter(spec).write_to_disk(ag_path)
    
    assert os.path.exists(lg_path)
    assert os.path.exists(cr_path)
    assert os.path.exists(ag_path)


def test_langgraph_ast_parser_memory_and_tools_roundtrip():
    """4. Asserts abstract recovery of database checkpointers, threads, and code bodies from LangGraph source."""
    workflow = (
        SwarmWorkflow(name="lg-roundtrip")
        .configure_memory(backend="sqlite", thread_id="checkpoint-session-777", connection_string="prod_data.db")
        .add_step(node_id="step_a", executor_reference="blobs/test_blob.py", is_entry_point=True)
    )
    spec = workflow.build_spec()
    generated_code = LangGraphEmitter(spec).emit()
    
    parsed_spec = LangGraphParser(generated_code).parse()
    
    # Assert structural recovery of memory architectures
    assert parsed_spec.memory.storage_backend == "sqlite"
    assert parsed_spec.memory.thread_id == "checkpoint-session-777"
    assert parsed_spec.memory.connection_string == "prod_data.db"
    
    node_ids = {n.id for n in parsed_spec.topology.nodes}
    assert "step_a" in node_ids


def test_crewai_and_autogen_lossless_metadata_rehydration():
    """5. Validates memory layout structures and interface vectors re-hydrate via JSON source maps."""
    workflow = (
        SwarmWorkflow(name="lossless-relay")
        .configure_memory(backend="sqlite", thread_id="session-omega")
        .register_mcp_server(name="cloud_vector_db", transport="sse", endpoint="https://api.vector")
        .add_step(node_id="secure_step", executor_reference="blobs/test_blob.py", interfaces=["cloud_vector_db"])
    )
    spec = workflow.build_spec()
    
    # Test CrewAI Pass
    crew_code = CrewAIEmitter(spec).emit()
    recovered_crew_spec = CrewAIParser(crew_code).parse()
    assert recovered_crew_spec.memory.storage_backend == "sqlite"
    assert recovered_crew_spec.memory.thread_id == "session-omega"
    assert len(recovered_crew_spec.interfaces) == 1
    assert recovered_crew_spec.interfaces[0].name == "cloud_vector_db"
    
    # Test AutoGen Pass
    autogen_code = AutoGenEmitter(spec).emit()
    recovered_ag_spec = AutoGenParser(autogen_code).parse()
    assert recovered_ag_spec.memory.storage_backend == "sqlite"
    assert recovered_ag_spec.memory.thread_id == "session-omega"
    assert recovered_ag_spec.topology.nodes[0].interfaces == ["cloud_vector_db"]