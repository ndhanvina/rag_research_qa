
class Config:
    PAPERS_DIR = "rag_papers"
    DB_DIR = "chromadb_rag_papers"

    EMBEDDING_MODEL =  "all-MiniLM-L6-v2"
    LLM_MODEL = "llama-3.1"
    LLM_TEMPERATURE = 0.2

    CHUNK_SIZE = 1000
    CHUNK_OVERLAP = 200
    RETRIEVE_K = 6