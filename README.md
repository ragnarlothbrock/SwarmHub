# 🐝 SwarmHub

### The Universal Abstraction Plane and Cross-Compiler for AI Agent Frameworks

SwarmHub is an enterprise-grade cross-compiler utility and programmatic SDK designed to completely decouple **AI Workforce Architecture** from **Framework Execution Paradigms**. Design your multi-agent routing graphs, data schemas, and tool allocations once using an agnostic, fluent Python API, then instantly cross-compile them natively into production-ready **LangGraph**, **CrewAI**, or **Microsoft AutoGen** codebases.

---

## 💡 The Core Philosophy: Orchestration vs. Cognition

The current AI ecosystem suffers from severe framework lock-in. Switching an active agent workforce from a State-Machine model (LangGraph) to an Actor-Model conversation layer (AutoGen) or a sequential execution track (CrewAI) typically forces an expensive, complete rewrite of state schemas, transition maps, and tool parameters.

SwarmHub splits the problem cleanly into two layers:
1. **The Orchestration Layer (SwarmHub Core):** Manages routing topology, state constraints, and framework target translation loops at compile time.
2. **The Cognitive Layer (Local Code Blobs):** Houses your actual business rules, granular prompts, and model interactions inside completely isolated, standard Python modules.

By separating the infrastructure (the framework) from the execution logic (your code blobs), SwarmHub gives you the flexibility to swap underlying execution paradigms instantly with zero structural rewrites.

---

## ⚡ Key Features

* **Fluent Programmatic SDK:** Design non-linear multi-agent networks using clean, chainable, human-readable Python commands.
* **Deterministic AST Cross-Compilation:** Deep Abstract Syntax Tree parsers reverse-engineer native source assets and rebuild them into alternative runtime targets.
* **Strict State Contracts:** Dynamically compiles inline Pydantic validation guards onto the entry and exit boundaries of every agent node, neutralizing state drift or runtime corruption.
* **Lossless Round-Trip Metadata Relays:** Embeds serialized topological maps inside comments to cleanly pass graph data across linear and non-linear framework frameworks.
* **Local Sandboxed Verification Engine:** Run and test full business logic pipelines offline for free without spending real LLM API tokens during dev iterations.

---

## 🏗️ Project Architecture

SwarmHub/
├── swarmhub/
│   ├── core/
│   │   ├── spec.py       # Universal Agent Specification Contract Schema
│   │   ├── builder.py    # Developer-facing Fluent SDK Generator
│   │   └── linker.py     # Graph mutation and edge splicing link-editor
│   ├── parsers/          # AST-driven framework reverse-engineers
│   ├── emitters/         # Framework-specific native code compilers
│   └── cli.py            # Global Command Line interface console
├── blobs/                # Business logic & local prompts (Agent Executables)
├── tools/                # Centralized, reusable backend endpoints and utilities
└── tests/                # Automated validation test suite


## 🚀 Quick Start Guide

1. Installation
Mount SwarmHub globally to your laptop terminal shell in editable development mode:
Bash
pip install -e .


2. Programmatically Generate a Swarm Blueprint
Create a script (e.g., run_sdk_triage.py) to build a guardrailed, tool-aware agent workstream using the agnostic fluent API:

Python
from swarmhub.core.builder import SwarmWorkflow
from swarmhub.emitters.langgraph import LangGraphEmitter

# Define a strict workflow contract model
agent_system = (
    SwarmWorkflow(name="corporate-triage-swarm")
    .configure_runtime(provider="openai", model="gpt-4o", temperature=0.0)
    
    # Enforce an explicit type-safe global context state contract
    .set_state_schema({
        "customer_id": "str",
        "account_balance": "float",
        "ticket_priority": "int"
    })
    
    # Register execution steps and assign tool dependencies
    .add_step("classifier", "blobs/triage.py", is_entry_point=True, tools=["db_lookup"])
    .add_step("processor", "blobs/refund.py")
    
    # Establish directional routing edges
    .add_route(from_node="classifier", to_node="processor", condition_trigger="PROCEED")
)

# Compile down into a clean, standalone production code file
blueprint = agent_system.build_spec()
LangGraphEmitter(blueprint).write_to_disk("dist/production_langgraph.py")
Run the script to build your baseline deployment file:

Bash
python3 run_sdk_triage.py
3. Cross-Compile Frameworks on the Fly via CLI
Now that the baseline file is written, you can pass it straight to your global terminal command tool to generate alternative architecture outputs without modifying a single line of your source logic:

Bash
# Cross-compile the generated LangGraph file straight down into native CrewAI code
swarmhub --source dist/production_langgraph.py --from-framework langgraph --target crewai --output dist/crew_workforce.py

# Transpile that same logic layout directly into a Microsoft AutoGen Chatroom environment
swarmhub --source dist/production_langgraph.py --target autogen --output dist/autogen_chatroom.py
🔒 Automated Contract Guardrails
SwarmHub protects long-running state tracking parameters by appending an isolated SharedContextContract(BaseModel) model into the execution wrapper loops of every target framework. When nodes run:

On Entry: Catches initialization glitches or structural errors introduced by external API payload handoffs before they penetrate the node's brain.

On Exit: Catches logical errors or data key typos made inside custom code blobs before they propagate downstream and break the workflow.

🧪 Running the Compiler Test Suite
To ensure absolute system stability, verify the codebase locally against the full cross-compilation test rig:

Bash
pytest -v


## 📄 License

Distributed under the Apache License 2.0. See the `LICENSE` file for details.



