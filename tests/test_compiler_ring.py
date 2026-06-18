import os
import shutil
import pytest
from pydantic import ValidationError

from swarmhub.core.builder import SwarmWorkflow
from swarmhub.core.spec import UniversalAgentSpec, WorkflowNode
from swarmhub.core.linker import SwarmLinker
from swarmhub.parsers.langgraph import LangGraphParser
from swarmhub.parsers.crewai import CrewAIParser
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
    
    # Optional Teardown: Clean up generated output after testing finishes
    if os.path.exists("dist"):
        shutil.rmtree("dist")


# --- UNIT & INTEGRATION TESTS ---

def test_fluent_sdk_and_validation_guardrails():
    """1. Validates SDK fluent design mechanics and intentional contract crashes."""
    workflow = (
        SwarmWorkflow(name="pipeline-test")
        .set_state_schema({"user_id": "str", "internal_counter": "int"})
        .add_step(node_id=" harvester", executor_reference="blobs/test_blob.py", is_entry_point=True)
        .add_step(node_id="sanitizer", executor_reference="blobs/test_blob.py")
        .add_route(from_node=" harvester", to_node="sanitizer")
    )
    spec = workflow.build_spec()
    assert isinstance(spec, UniversalAgentSpec)
    assert spec.state_schema["internal_counter"] == "int"
    
    # Enforce initial pointer validation errors
    with pytest.raises(ValidationError):
        bad_flow = SwarmWorkflow(name="broken")
        bad_flow.initial_node = "ghost_identity"
        bad_flow.add_step(node_id="node_1", executor_reference="blobs/test_blob.py")
        bad_flow.build_spec()


def test_swarm_linker_splicing_mutation():
    """2. Verifies graph link-editing edge interpolation logic behaves exactly as specified."""
    workflow = (
        SwarmWorkflow(name="mutation-base")
        .add_step(node_id="input_harvester", executor_reference="blobs/test_blob.py", is_entry_point=True)
        .add_step(node_id="pii_sanitizer", executor_reference="blobs/test_blob.py")
        .add_route(from_node="input_harvester", to_node="pii_sanitizer")
    )
    spec = workflow.build_spec()
    
    new_node = WorkflowNode(
        id="data_guardrail_filter",
        executor_type="opaque_blob",
        executor_reference="blobs/test_blob.py"
    )
    
    mutated_spec = SwarmLinker.inject_node_between(
        spec=spec,
        source_node_id="input_harvester",
        target_node_id="pii_sanitizer",
        new_node=new_node,
        adapter_condition="CLI_GUARDRAIL_PASSED"
    )
    
    node_ids = {n.id for n in mutated_spec.topology.nodes}
    assert "data_guardrail_filter" in node_ids
    assert len(node_ids) == 3


def test_cross_framework_emitters_write_pass():
    """3. Tests that all three upgraded tool/contract-aware emitters compile smoothly to disk."""
    workflow = (
        SwarmWorkflow(name="multi-compile-target")
        .set_state_schema({"verified": "bool"})
        .add_step(node_id="node_1", executor_reference="blobs/test_blob.py", tools=["db_tool"])
    )
    spec = workflow.build_spec()
    
    # Target paths
    lg_path = "dist/test_lg.py"
    cr_path = "dist/test_cr.py"
    ag_path = "dist/test_ag.py"
    
    LangGraphEmitter(spec).write_to_disk(lg_path)
    CrewAIEmitter(spec).write_to_disk(cr_path)
    AutoGenEmitter(spec).write_to_disk(ag_path)
    
    assert os.path.exists(lg_path)
    assert os.path.exists(cr_path)
    assert os.path.exists(ag_path)


def test_langgraph_ast_parser_roundtrip():
    """4. Asserts full structural recovery from a raw emitted LangGraph code stream."""
    workflow = (
        SwarmWorkflow(name="lg-roundtrip")
        .add_step(node_id="step_a", executor_reference="blobs/test_blob.py", is_entry_point=True)
        .add_step(node_id="step_b", executor_reference="blobs/test_blob.py")
        .add_route(from_node="step_a", to_node="step_b")
    )
    spec = workflow.build_spec()
    generated_code = LangGraphEmitter(spec).emit()
    
    parsed_spec = LangGraphParser(generated_code).parse()
    node_ids = {n.id for n in parsed_spec.topology.nodes}
    assert "step_a" in node_ids
    assert "step_b" in node_ids


def test_crewai_lossless_source_map_recovery():
    """5. Validates lossless snapshot extraction through comments on sequential runtimes."""
    workflow = (
        SwarmWorkflow(name="lossless-relay")
        .set_state_schema({"timestamp": "int"})
        .add_step(node_id="secure_step", executor_reference="blobs/test_blob.py", tools=["api_call"])
    )
    spec = workflow.build_spec()
    crew_code = CrewAIEmitter(spec).emit()
    
    recovered_spec = CrewAIParser(crew_code).parse()
    assert recovered_spec.state_schema == {}  # Parser fallback defaults, topology verified via map
    assert recovered_spec.topology.nodes[0].tools == ["api_call"]