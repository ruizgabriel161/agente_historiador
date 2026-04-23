
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter


class TextChunker:
    """
    Classe responsável por dividir o texto em chunks
    """
    def __init__(self, chunk_size:int = 800, chunk_overlap:int = 150):
        self._splitter: RecursiveCharacterTextSplitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )
    def split(self, docs: list[Document]) -> list[Document]:
        return self._splitter.split_documents(documents=docs)
        