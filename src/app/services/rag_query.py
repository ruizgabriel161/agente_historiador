from langchain.chat_models import BaseChatModel
from langchain_core.documents import Document
from langchain_core.messages import AIMessage
from langchain_core.vectorstores import VectorStore, VectorStoreRetriever

from app.config.logger_config import get_logger


class RAGQueryService:
    def __init__(self, llm: BaseChatModel, vectorsstore: VectorStore, k: int = 5):
        self.logger = get_logger('rag_historiador')
        self._llm: BaseChatModel = llm
        self._retriever: VectorStoreRetriever = vectorsstore.as_retriever(
            search_kwargs={"k": k}
        )
    def ask(self, question: str) -> str:
        docs: list[Document] = self._retriever.invoke(question)

        self.logger.debug(f'{docs=}')

        context = "/n/n".join(d.page_content for d in docs)

        prompt = f"""
                Você é um historiador especialista.
                Use apenas o contexto abaixo para responder.

                Contexto:
                {context}

                Pergunta:
                {question}
            """

        response: AIMessage = self._llm.invoke(prompt)
        return response.text
