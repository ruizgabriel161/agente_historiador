from langchain_core.documents import Document
from langchain_core.embeddings import Embeddings
from langchain_core.vectorstores import VectorStore

from app.infraestructure.chunk.chunk import TextChunker
from app.infraestructure.loaders.pdf_loader import PdfLoader
from app.infraestructure.vectorstores.base_vectorstore import BaseVectorStore

from 

class PDFIngestionService:
    def __init__(
        self,
        loader: PdfLoader,
        splitter: TextChunker,
        vectorstore: BaseVectorStore,
        embeddings: Embeddings,
    ):
        self._loader: PdfLoader = loader
        self._splitter: TextChunker = splitter
        self._vectorstore: BaseVectorStore = vectorstore
        self._embeddings: Embeddings = embeddings

    def ingest(self, pdf_path: str) -> VectorStore:
        """
        ingest Metodo responsável por ingetar no banco de dados vetorial o pdf embbedado

        Args:
            pdf_path (str): caminho do pdf

        Returns:
            VectorStore: intacia do banco de dados vetorial
        """
        documents: list[Document] = self._loader.load(pdf_path)
        chunks: list[Document] = self._splitter.split(documents)

        store = self._vectorstore.get(self._embeddings)
        store.add_documents(chunks)

        return store
