from langchain_ollama import ChatOllama
from.config import Config


Class RagEngine:
    def __init__(self, retriever):
        self.retriever = retriever
        self.llm = ChatOllama(
            model = Config.LLM_MODEL,
            temperature = Config.LLM_TEMPERATURE
        )

    def _format_docs(self, docs):
        