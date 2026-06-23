# 🐝 SwarmHub

### The Universal Abstraction Plane and Cross-Compiler for AI Agent Frameworks

SwarmHub is an enterprise-grade cross-compiler utility, programmatic SDK, and decentralized package manager designed to completely decouple **AI Workforce Architecture** from **Framework Execution Paradigms**. Design your multi-agent routing graphs, long-running state threads, and tool allocations once using an agnostic, fluent Python API, then instantly cross-compile them natively into production-ready **LangGraph**, **CrewAI**, or **Microsoft AutoGen** codebases.

---

## 💡 The Core Philosophy: Orchestration vs. Cognition

The current AI ecosystem suffers from severe framework lock-in. Switching an active agent workforce from a State-Machine model (LangGraph) to an Actor-Model conversation layer (AutoGen) or a sequential execution track (CrewAI) typically forces an expensive, complete rewrite of state schemas, persistence adapters, and tool parameters.

SwarmHub splits the problem cleanly into two layers:
1. **The Orchestration Layer (SwarmHub Core):** Manages routing topology, thread memory context boundaries, interface constraints, and framework target translation loops at compile time.
2. **The Cognitive Layer (Local Code Blobs):** Houses your actual business rules, granular prompts, and model interactions inside completely isolated, standard Python modules (Blobs).

By separating the infrastructure (the framework) from the execution logic (your code blobs), SwarmHub gives you the flexibility to swap underlying execution paradigms instantly with zero structural rewrites.

---

## ⚡ Key Features

* **Fluent Programmatic SDK:** Design non-linear multi-agent networks using clean, chainable, human-readable Python commands supporting advanced memory layouts and capability server registries.
* **Universal State Persistence & Memory:** Track long-running conversation loops using backend-agnostic checkpointers (SQLite, In-Memory, etc.) that cross-compile cleanly into isolated native runtime saver tables (`swarmhub_checkpoints`) protecting your data boundaries.
* **Model Context Protocol (MCP) Integration:** Connect your agent workforce to unified external capability servers running over local `stdio` sub-processes or remote network transport nodes with granular, least-privilege permission scoping at the node level.
* **Serverless Package Registry:** A decentralized package manager capable of staging, linting, publishing, and distributing both individual script nodes and complete multi-agent workloads directly across public GitHub repositories.
* **Deterministic AST Cross-Compilation:** Deep Abstract Syntax Tree parsers reverse-engineer native source code parameters and rebuild them symmetrically into alternative framework compilation targets.
* **Universal Translation Mapping Plane:** Natively ingests legacy architectures and standalone assets, transforming `LangChain` pipelines into stateful `LangGraph` graphs, and unstructured `Vanilla Python` scripts into sequential `CrewAI` topologies.
* **Interactive AST Code Auto-Healer:** Pre-processing compilation layers scan and repair common syntax defects (such as unescaped nested f-string quotes or trailing bracket typos) programmatically on the fly before code strings hit the parser core.
* **Batteries-Included Agent Library:** 117 world-class agent environments automatically discovered and indexed, yielding **86 fully functional, pre-compiled production agent matrixes** shipping directly inside the distribution tree.
* **Strict State Contracts:** Dynamically compiles inline Pydantic validation guards onto the entry and exit boundaries of every agent node, neutralizing state drift or runtime context corruption.

---

## 📦 The Pristine Agent Library (Pre-Compiled Distribution Matrix)

SwarmHub ships out-of-the-box with a pre-compiled library containing **86 high-performance production agent systems**. These architectures were extracted directly from the official repositories of leading framework ecosystems and decentralized community registries, stripped of vendor lock-in, and cross-compiled across all target pipelines.

When a developer runs `git clone` on SwarmHub, they instantly inherit an optimized, ready-to-run cross-framework matrix located inside **`dist/compiled/`**:

```text
dist/compiled/
├── crewai/       # 44 Pre-Compiled Production Crews & Modernized Vanilla Python Codebases
├── langgraph/    # 13 Pre-Compiled Core Enterprise Graphs & Upgraded LangChain Pipelines
└── autogen/      # 29 Pre-Compiled Next-Gen AutoGen v0.4+ Workload Blueprints
```

### 🧠 Automated Jupyter Notebook Sanitization
The core framework examples provided by industry maintainers live almost exclusively inside heavily polluted Jupyter Notebooks (`.ipynb`). To prevent Abstract Syntax Tree (AST) compilation crashes, SwarmHub's mass ingestion pre-processors surgically extract code lines and strip out terminal environment pollutions on the fly:
* Identifies and parses nested JSON notebook cell array metadata structures.
* Filters out shell script updating commands (`!pip install`, `!pip3`).
* Wipes out interactive notebook magic operators (`%pip`, `%conda`).
* Validates and cleans the output stream, leaving a pure Python code block ready to hit our AST translation nodes.

---

## 🏗️ Project Architecture

```text
SwarmHub/
├── swarmhub/
│   ├── core/
│   │   ├── spec.py          # Universal Agent Specification Schema Contracts
│   │   ├── builder.py       # Developer-facing Fluent Memory/MCP SDK Generator
│   │   ├── linker.py        # Graph mutation, interface collision, and link-editing
│   │   └── registry.py      # Package registry manager, validation linters, and download clients
│   ├── parsers/             # AST-driven memory, tool, and sequence reverse-engineers
│   └── emitters/            # Framework-specific native code compilers & checkpointers
├── blobs/                   # Cognitive Layer: Framework-agnostic isolated code modules
├── tools/                   # Capability Layer: External tools and background MCP service daemons
├── examples/                # Composition Layer: Declarative blueprint maps and local source documents
├── dist/                    # Production Layer: Cross-compiled executable outputs
│   ├── registry/
│   │   └── registry_index.json  # Central Ground-Truth Agent Index (117 Total Solutions)
│   └── compiled/                # Pre-Compiled Framework Distribution Library Matrix (86 Verified Assets)
│       ├── crewai/              # Translated and ready-to-run CrewAI asset instances
│       ├── langgraph/           # Translated and ready-to-run LangGraph asset instances
│       └── autogen/             # Translated and ready-to-run AutoGen asset instances
└── tests/                   # Verification Layer: Automated cross-framework validation test suite
```

---

## 🌐 The Hub of Blobs: Serverless Architecture Registry

SwarmHub features a decentralized package manager that turns GitHub into a serverless distribution network. There are no centralized registry servers or hosting fees. Workflows, bricks, and agents are hosted transparently inside public git repositories, validated automatically via Abstract Syntax Tree (AST) static analysis parsing layers on download.

The ecosystem handles distribution across two distinct structural levels:

### 1. Atomic Bricks (Single Cognitive Steps)
An **Atomic Brick** is an isolated, reusable single function block (e.g., an LLM prompt classifier, a text sanitizer, or a data format converter). 
* **The Rule:** The target file must expose a valid `def run(state):` execution entry gate accepting exactly one state dictionary parameter.
* **Publishing an Atomic Brick:** Pass the relative file path to the publishing wizard assistant:
  ```bash
  swarmhub publish blobs/my_generic_classifier.py
  ```
  The assistant verifies the code structure via AST static analysis, builds an interactive Pydantic `blob.json` data contract mapping, and stages a clean distribution folder inside `dist/registry/`.

### 2. Composite Workloads (Full Agent Swarms)
A **Composite Workload** is a turn-key multi-agent automation ecosystem (such as our Advanced Self-Correcting RAG system). It encapsulates the master workflow compilation blueprint script, the collection of underlying specialized logic blobs, and any required background terminal capability daemons.
* **Publishing a Compound Workload:** Pass the entire workspace directory handle path directly to the assistant:
  ```bash
  swarmhub publish blobs/advanced_rag/
  ```
  The assistant flags the operation as a workload assembly, recursively crawls the directory tree to construct an automated package dependency map, links the primary execution entry file (e.g., `examples/advanced_rag_swarm.py`), and stages the complete nested package directory.

### 🌐 Installing Registered Assets From the Cloud
Because the network is fully decentralized, downloading either an individual script node or an entire pre-wired multi-agent ecosystem utilizes identical coordinate layout syntax formats:

```bash
# General Syntax: swarmhub install <github_username>/<repository_name>/<asset_slug>

# Example A: Download a single community 'brick' directly into your local blobs/ folder
swarmhub install ragnarlothbrock/SwarmHub-Registry/llm-cost-optimizer

# Example B: Unpack a complete, turn-key 'workload' stack across your project directories instantly
swarmhub install martinkovacevic/SwarmHub/advanced-corrective-rag
```
When a workload is detected, SwarmHub matches the dependency registry keys, downloads the files over secure raw HTTPS channels, runs safety contract checks, and mirrors the paths perfectly into your local project root (`blobs/`, `tools/`, and `examples/`), ready for cross-compilation.

---

## 🔥 Showcase: Advanced Self-Correcting (Corrective) RAG Swarm

SwarmHub shines when managing complex, non-linear feedback loops that must execute across entirely different structural frameworks. This showcase highlights a self-correcting RAG network executing on local **Llama 3.2** inference engines via an embedded, disk-persisted **ChromaDB HNSW vector database** connected via standard I/O sub-process channels.

### The Non-Linear Self-Correction Workflow Pattern
1. **`document_retriever`**: Queries a persistent background vector database daemon using high-dimensional embeddings.
2. **`context_grader`**: Passes the retrieved context chunks to Llama 3.2 to run a binary evaluation. If relevant, it signals `SYNTHESIZE`. If irrelevant or mismatched, it triggers `REWRITE`.
3. **`query_rewriter`**: Runs if flagged for a rewrite. It strips out query noise, evolves the prompt keywords, loops back to step 1, and runs a second-pass precision retrieval.
4. **`synthesis_generator`**: Synthesizes the grounded final response to the user with an anti-hallucination guarantee.

### 1. The Declarative Composition Blueprint (`examples/advanced_rag_swarm.py`)

```python
import os
from swarmhub.core.builder import SwarmWorkflow
from swarmhub.emitters.langgraph import LangGraphEmitter
from swarmhub.emitters.crewai import CrewAIEmitter
from swarmhub.emitters.autogen import AutoGenEmitter

def build_and_compile_advanced_rag():
    workflow = SwarmWorkflow(name="advanced-corrective-rag-swarm")

    # Target local Ollama runtime engines using OpenAI-compatible formats
    workflow.configure_runtime(provider="openai", model="llama3.2:3b", temperature=0.1)

    # Mount a persistent relational memory layer
    workflow.configure_memory(backend="sqlite", thread_id="local-rag-session-001", connection_string="dist/advanced_rag/rag_memory_vault.db")

    # Register an external Model Context Protocol (MCP) vector service daemon
    workflow.register_mcp_server(name="vector_store_service", transport="stdio", endpoint="python", args=["tools/advanced_rag/vector_service_daemon.py"])

    # Establish the explicit type-safe global context state contract schema
    workflow.set_state_schema({
        "user_query": "str",
        "search_query": "str",
        "retrieved_chunks": "str",
        "grade_status": "str",
        "loop_counter": "int"
    })

    # Add execution nodes bound to framework-agnostic cognitive blobs
    workflow.add_step(node_id="document_retriever", executor_reference="blobs/advanced_rag/rag_retriever.py", is_entry_point=True, interfaces=["vector_store_service"])
    workflow.add_step(node_id="context_grader", executor_reference="blobs/advanced_rag/rag_grader.py")
    workflow.add_step(node_id="query_rewriter", executor_reference="blobs/advanced_rag/rag_rewriter.py")
    workflow.add_step(node_id="synthesis_generator", executor_reference="blobs/advanced_rag/rag_generator.py")

    # Wire up non-linear routing and recursive repair loops
    workflow.add_route(from_node="document_retriever", to_node="context_grader", condition_trigger="PROCEED")
    workflow.add_route(from_node="context_grader", to_node="synthesis_generator", condition_trigger="SYNTHESIZE")
    workflow.add_route(from_node="context_grader", to_node="query_rewriter", condition_trigger="REWRITE")
    workflow.add_route(from_node="query_rewriter", to_node="document_retriever", condition_trigger="RETRY")

    # Compile the blueprint and export to native framework targets
    universal_spec = workflow.build_spec()
    target_dir = "dist/advanced_rag"
    
    LangGraphEmitter(universal_spec).write_to_disk(os.path.join(target_dir, "compiled_rag_langgraph.py"))
    CrewAIEmitter(universal_spec).write_to_disk(os.path.join(target_dir, "compiled_rag_crewai.py"))
    AutoGenEmitter(universal_spec).write_to_disk(os.path.join(target_dir, "compiled_rag_autogen.py"))

if __name__ == "__main__":
    build_and_compile_advanced_rag()
```

### 2. Running and Verifying Cross-Compiled Frameworks

Because SwarmHub compiles true framework-agnostic topologies, your code blobs will execute identically with live interactive terminal prompt gates across all three major platforms.

Execute the builder script to compile your targets:
```bash
python3 examples/advanced_rag_swarm.py
```

Launch the native **LangGraph** Functional State Graph:
```bash
python3 dist/advanced_rag/compiled_rag_langgraph.py
```

Launch the native **CrewAI** Task-Driven State Machine Runner:
```bash
python3 dist/advanced_rag/compiled_rag_crewai.py
```

Launch the native **AutoGen** Conversational Participant State Machine Runner:
```bash
python3 dist/advanced_rag/compiled_rag_autogen.py
```

---

## 🚀 Quick Start Guide

### 1. Installation

Mount SwarmHub globally to your laptop terminal shell in editable development mode:

```bash
pip install -e .
```

### 2. Programmatically Generate a Persistent, Tool-Aware Swarm

Create a script (e.g., `run_sdk_triage.py`) to build a guardrailed, persistent agent workstream bound to a local Model Context Protocol capability server using the agnostic fluent API:

```python
from swarmhub.core.builder import SwarmWorkflow
from swarmhub.emitters.langgraph import LangGraphEmitter

# Initialize an advanced, tool-aware workflow configuration
agent_system = (
    SwarmWorkflow(name="corporate-triage-swarm")
    .configure_runtime(provider="openai", model="gpt-4o", temperature=0.0)
    
    # 💾 Configure Abstract State Persistence Checkpointing
    .configure_memory(backend="sqlite", thread_id="session-tx-777", connection_string="swarmhub_memory.db")
    
    # 🔌 Register Global External MCP Capability Servers
    .register_mcp_server(name="secure_db", transport="stdio", endpoint="uvx", args=["mcp-server-db"])
    
    # 📝 Enforce an explicit type-safe global context state contract
    .set_state_schema({
        "customer_id": "str",
        "account_balance": "float",
        "ticket_priority": "int"
    })
    
    # 🔒 Register nodes with local tool hooks and granular MCP interface privileges
    .add_step("classifier", "blobs/triage.py", is_entry_point=True, tools=["db_lookup"], interfaces=["secure_db"])
    .add_step("processor", "blobs/refund.py")
    
    # Establish directional routing edges
    .add_route(from_node="classifier", to_node="processor", condition_trigger="PROCEED")
)

# Compile down into a clean, standalone production code file
blueprint = agent_system.build_spec()
LangGraphEmitter(blueprint).write_to_disk("dist/production_langgraph.py")
```

Run the script to build your baseline deployment file:

```bash
python3 run_sdk_triage.py
```

---

## 💻 Command Line Interface (CLI) Engine

SwarmHub features a fully decentralized CLI console tool managing both agent cross-compilers and structural repository assets.

### Cross-Framework Transpilation

Convert your generated specification script directly into alternative orchestration patterns on the fly without changing a single line of your source logic modules:

```bash
# Cross-compile a LangGraph system down into a native, persistent CrewAI code architecture
swarmhub compile --source dist/production_langgraph.py --from-framework langgraph --target crewai --output dist/crew_workforce.py

# Transpile that same structural architecture layout directly into an AutoGen Chatroom
swarmhub compile --source dist/production_langgraph.py --target autogen --output dist/autogen_chatroom.py

# Optimization Flag: Inline external code blobs back into a single unified deployment asset file
swarmhub compile --source dist/production_langgraph.py --target langgraph --output dist/unified_script.py --inline
```

### Decentralized Package Management (The Hub of Blobs)

Pull down verified community cognitive logic assets or complex composite workload architectures from the public git cloud instantly:

```bash
# Install an atomic function brick asset straight into your local directory tracks
swarmhub install ragnarlothbrock/SwarmHub-Registry/llm-cost-optimizer

# Install a full turn-key multi-agent workload stack (including code, tools, and configurations)
swarmhub install martinkovacevic/SwarmHub/advanced-corrective-rag

# Package a local file or directory using the automated packaging manifest assistant wizard
swarmhub publish blobs/advanced_rag/
```

---

## 🔒 Automated Contract Guardrails

SwarmHub protects transaction contexts and long-running parameters by appending an isolated `SharedContextContract(BaseModel)` validation engine straight into the wrapper routing structures of every target framework. When nodes run:

* **On Entry:** Catches serialization glitches or external structural mutations before data penetrates the node's execution context.
* **On Exit:** Catches logical drift, type contradictions, or key typos made inside custom code blobs before they can pollute downstream nodes or persistence databases.

---

## 🧪 Running the Compiler Test Suite

To verify the cross-framework translation compilers, linker mergers, and memory rehydration passes locally, run the automated test suite engine:

```bash
pytest -v tests/test_compiler_ring.py
```

---

## 📄 License

Distributed under the Apache License 2.0. See the `LICENSE` file for details.