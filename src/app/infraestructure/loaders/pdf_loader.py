from typing import override

from langchain_community.document_loaders import PyMuPDFLoader
from langchain_core.documents import Document

from app.infraestructure.loaders.base_loader import BaseLoader


class PdfLoader(BaseLoader):
    """
    Classe responsável por ler o documento
    """

    @override
    def load(self, path: str) -> list[Document]:
        '''
        load Método responsável por carregar o PDF

        Args:
            path (str): caminho do arquivo

        Returns:
            List[Document]: retorna uma lista de documento
        '''        

        return PyMuPDFLoader(file_path=path).load()
