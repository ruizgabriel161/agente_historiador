
from abc import ABC
from langchain_core.vectorstores import VectorStore
from langchain_core.embeddings import Embeddings

class BaseVectorStore(ABC):
    """
    Classe abstrata sobre banco vetorial
    """
    def get(self, embbeding: Embeddings) -> VectorStore:
        '''
        get  Método para popular o banco de dados vetorial

        Args:
            embbeding (Embeddings): objeto embbeding

        Returns:
            VectorStore: retorna uma instancia do banco de dados
        '''        
        ...

    