from typing import override

from chromadb import HttpClient
from chromadb.api import ClientAPI
from chromadb.config import Settings
from langchain_chroma import Chroma
from langchain_core.embeddings import Embeddings
from langchain_core.vectorstores import VectorStore

from app.infraestructure.vectorstores.base_vectorstore import BaseVectorStore


class ChromaVectorStore(BaseVectorStore):
    def __init__(self, host: str, port: int, collection_name: str):
        self.host = host
        self.port = port
        self.collection_name = collection_name
        self._client = self._set_client()

    def _set_client(self) -> ClientAPI:
        return HttpClient(
            host=self.host,
            port=self.port,
            settings=Settings()
        ) 

    @override
    def get(self, embeddings: Embeddings) -> VectorStore:
        return Chroma(
            client=self._client,
            collection_name=self.collection_name,
            embedding_function=embeddings,

        )
        