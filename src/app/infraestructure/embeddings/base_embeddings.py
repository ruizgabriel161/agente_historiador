
from abc import ABC, abstractmethod
from langchain_core.embeddings import Embeddings

class BaseEmbeddingService(ABC):
    """
    Classe abstrata para iniciar o serviço de embbeding
    """
    @abstractmethod
    def init_embeddings(self, model:str, url:str) -> Embeddings:
        ...