from typing import List
from langchain_community.document_loaders import DirectoryLoader, PyMuPDFLoader
from .config import Config

class DocumentProcessor:
    @staticmethod
    def load_documents() -> List[Document]:
        loaders = DirectoryLoader(
            str(Config.PAPERS_DIR),
            glob = "*.pdf",
            loader_cls = PyMuPDFLoader,
            show_progress = True
        )

        docs = loaders.load()
        return docs

    @staticmethod
    def chunk_documents(docs: List[Document]) -> List[Document]:
        splitter = RecursiveCharacterTextSplitter(
            chunk_size = Config.CHUNK_SIZE,
            chunk_overlap = Config.CHUNK_OVERLAP,
            separators = ["/n/n", "/n"," ", ""]
        )
        