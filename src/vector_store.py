from langchain_huggingface import HuggingFaceEmbeddings
from .config import Config
from langchain_chroma import chroma
import os
import shutil

class VectorStore:
    def __init__(self):
        self.embeddings = HuggingFaceEmbeddings(
            model_name = Config.EMBEDDING_MODEL,
        )

    def create_vector_store(self, Document):
        if os.path.exists(Config.DB_DIR):
            shutil.rmtree(Config.DB_DIR)
        
        db = chroma.from_documents(
            documents = Document,
            embedding = self.embeddings,
            persist_directory = Config.DB_DIR
        )
        return db

    def get_vector_store(self):
        return chroma(
            persist_directory = Config.DB_DIR,
            embedding_function = self.embeddings
        )

    def get_retriever(self):
        db = self.get_vector_store()
        return db.as_retriever(
            search_type = "similarity",
            search_kwargs = {"k": Config.RETRIEVE_K}
        )


