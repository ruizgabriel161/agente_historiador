from app.infraestructure.embeddings.base_embeddings import BaseEmbeddingService
from langchain_core.embeddings import Embeddings
from langchain_ollama import OllamaEmbeddings

class OllamaEmbbeding(BaseEmbeddingService):
    """
    Classe responsável pelo embbeding do ollma
    """
    def init_embeddings(self, model:str, url:str) -> Embeddings:
        '''
        init_embeddings init_embeddings Metodo para iniciar um objeto embedding

        Args:
            model (str): modelo de embbeding
            url (str): url que o modelo tá hospedado

        Returns:
            Embeddings: Embeddings: retorna uma instancia de embedding
        '''        
        return OllamaEmbeddings(
            model=model, base_url=url
            )