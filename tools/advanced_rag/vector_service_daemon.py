import os
import sys
import json
import urllib.request
from pypdf import PdfReader
import chromadb

# --- 1. CONFIGURATION PARAMETERS ---
DOCUMENTS_DIR = "examples/documents"
CHROMA_DB_DIR = "dist/chroma_vector_vault"  # Persistent local database path
COLLECTION_NAME = "advanced_rag_collection"
OLLAMA_EMBED_URL = "http://localhost:11434/api/embed"
EMBEDDING_MODEL = "nomic-embed-text"
CHUNK_SIZE = 600
CHUNK_OVERLAP = 120
TOP_K = 2

# --- 2. INFERENCE CALLS TO OLLAMA ---
def get_embedding(text_string):
    """Dispatches a POST request to Ollama to generate a text embedding vector."""
    payload = {
        "model": EMBEDDING_MODEL,
        "input": text_string
    }
    req = urllib.request.Request(
        OLLAMA_EMBED_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST"
    )
    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            res_data = json.loads(response.read().decode("utf-8"))
            return res_data["embeddings"][0]
    except Exception as e:
        sys.stderr.write(f"❌ Error fetching embedding from Ollama: {e}\n")
        return [0.0] * 768

# --- 3. PERSISTENT INGESTION & SUB-SAMPLING LOOP ---
def initialize_persistent_vector_store():
    """Initializes a local file-backed vector database and processes unindexed PDFs."""
    os.makedirs(DOCUMENTS_DIR, exist_ok=True)
    os.makedirs(os.path.dirname(CHROMA_DB_DIR), exist_ok=True)
    
    # Instantiate Chroma's local file-backed disk client (Zero server setup required)
    chroma_client = chromadb.PersistentClient(path=CHROMA_DB_DIR)
    
    # Fetch or create the isolated vector collection database space
    collection = chroma_client.get_or_create_collection(name=COLLECTION_NAME)
    
    # Optimization Gate: Check if data is already stored on disk
    existing_count = collection.count()
    pdf_files = [f for f in os.listdir(DOCUMENTS_DIR) if f.endswith(".pdf")]
    
    if existing_count > 0 and not pdf_files:
        sys.stderr.write(f"💾 Persistent Vault Located. Running with {existing_count} pre-indexed database vectors.\n")
        return collection

    if not pdf_files:
        sys.stderr.write(f"📁 Empty document repository at '{DOCUMENTS_DIR}'. Drop your source PDFs here!\n")
        return collection

    # If new PDFs are detected, parse and add them to the persistent store
    sys.stderr.write(f"📚 Detected active document collection files. Commencing persistent disk indexing...\n")
    
    global_chunk_counter = existing_count
    for filename in pdf_files:
        filepath = os.path.join(DOCUMENTS_DIR, filename)
        try:
            reader = PdfReader(filepath)
            full_text = ""
            for page in reader.pages:
                text = page.extract_text()
                if text:
                    full_text += text + " "
            
            # Slide character window down the parsed text block
            start = 0
            file_chunks = []
            while start < len(full_text):
                end = start + CHUNK_SIZE
                chunk = full_text[start:end].strip()
                if len(chunk) > 30:
                    file_chunks.append(chunk)
                start += (CHUNK_SIZE - CHUNK_OVERLAP)
                
            sys.stderr.write(f"   Parsing '{filename}': Extracted {len(file_chunks)} sliding blocks.\n")
            
            # Pack chunks and pre-computed vectors straight into ChromaDB storage layers
            for idx, chunk in enumerate(file_chunks):
                global_chunk_counter += 1
                sys.stderr.write(f"   ↳ Progress: Vectorizing element {idx+1}/{len(file_chunks)}...\r")
                
                # Fetch embedding via Ollama acceleration
                vector = get_embedding(chunk)
                
                # Persist directly to disk files
                collection.add(
                    ids=[f"id_chunk_{global_chunk_counter}"],
                    embeddings=[vector],
                    metadatas=[{"source": filename}],
                    documents=[chunk]
                )
            sys.stderr.write("\n")
            # Archive the file to ensure it doesn't get processed next reboot pass
            os.rename(filepath, os.path.join(DOCUMENTS_DIR, f".processed_{filename}"))
            
        except Exception as e:
            sys.stderr.write(f"❌ Failed processing document index '{filename}': {e}\n")
            
    sys.stderr.write(f"✅ Disk Storage Synchronized. Total stored vectors: {collection.count()}\n")
    return collection

# --- 4. PERSISTENT SUB-PROCESS INTERFACE LINK ---
def main():
    # Stand up our indexed connection collection
    collection = initialize_persistent_vector_store()
    
    sys.stderr.write("🔌 SwarmHub MCP Protocol Server Alive: Awaiting incoming standard IO queries...\n")
    sys.stderr.flush()

    while True:
        try:
            line = sys.stdin.readline()
            if not line:
                break
                
            request = json.loads(line.strip())
            query_text = request.get("query", "")
            
            if not query_text:
                print(json.dumps({"error": "Empty search parameters provided."}))
                sys.stdout.flush()
                continue
                
            # 1. Transform active query text into an embedding float vector
            query_vector = get_embedding(query_text)
            
            # 2. Query ChromaDB's local file-backed HNSW index
            # This completely bypasses brute force array loops
            search_results = collection.query(
                query_embeddings=[query_vector],
                n_results=TOP_K
            )
            
            # 3. Restructure query matching results into unified return lines
            retrieved_strings = []
            if search_results and "documents" in search_results and search_results["documents"]:
                documents_list = search_results["documents"][0]
                metadatas_list = search_results["metadatas"][0]
                distances_list = search_results["distances"][0] if "distances" in search_results else [0.0] * len(documents_list)
                
                for doc_text, meta, distance in zip(documents_list, metadatas_list, distances_list):
                    source_name = meta.get("source", "Unknown")
                    # Note: Chroma distance tracks vector divergence; lower values indicate higher semantic proximity
                    retrieved_strings.append(f"[Source: {source_name} | Divergence: {distance:.4f}]: {doc_text}")
            
            response_payload = {
                "status": "SUCCESS",
                "results": " || ".join(retrieved_strings) if retrieved_strings else "No contextual data hits found."
            }
            
            print(json.dumps(response_payload))
            sys.stdout.flush()
            
        except Exception as err:
            sys.stderr.write(f"❌ Persistent Daemon encountered loop anomaly: {err}\n")
            sys.stderr.flush()
            print(json.dumps({"status": "ERROR", "results": "Fallback database loop tracking fault."}))
            sys.stdout.flush()

if __name__ == "__main__":
    main()