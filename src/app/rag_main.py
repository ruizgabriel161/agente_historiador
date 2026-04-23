
from app.config.config_env import Settings
from app.infraestructure.chunk.chunk import TextChunker
from app.infraestructure.embeddings.service_embbeding import OllamaEmbbeding
from app.infraestructure.llm.load_llm import LoadLLM
from app.infraestructure.loaders.pdf_loader import PdfLoader
from app.infraestructure.vectorstores.base_vectorstore import BaseVectorStore
from app.infraestructure.vectorstores.chroma import ChromaVectorStore
from app.services.pdf_ingestion import PDFIngestionService
from app.services.rag_query import RAGQueryService


def main() -> None:

    settings: Settings = Settings() # carrega as variáveis de ambientw

    loader:PdfLoader = PdfLoader() # Inicia a classe para ler o pdf
    splitter:TextChunker = TextChunker(chunk_size=1000, chunk_overlap=200) # classe para dividir o pdf em chunks

    embbedings = OllamaEmbbeding().init_embeddings(
        model=settings.MODE_EMBEDDIGNS,
        url=settings.LLM_HOST
    ) # classe para criar o embbending do pdf

    vectorstore_repo: BaseVectorStore = ChromaVectorStore(
        host='localhost',
        port=8000,
        collection_name='agente_historiador'
    ) # cria uma instancia do banco de dados vetorial


    ingestion = PDFIngestionService(
        loader=loader,
        splitter=splitter,
        vectorstore=vectorstore_repo,
        embeddings=embbedings
    ) # classe para ingerir os embbending no baco de dados vetorial

    store = ingestion.ingest(r"K:\Workspace\Python\agente_historiador\docs\Monografia - Gabriel Lopes Ruiz.pdf") # adiciona o embbending do pdf

    llm = LoadLLM().init_llm() # carrega a LLM

    rag = RAGQueryService(
        llm=llm,
        vectorsstore=store,
        k=5
    ) # cria o prompt com os embbending

    while True:
        user_input:str = input('User: ')

        if user_input.lower() in ['q', 'sair','exit']:
            break
        answer = rag.ask(user_input)
        print("\nResposta:\n", answer)

if __name__ == "__main__":
    main()