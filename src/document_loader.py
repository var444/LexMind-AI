from typing import List   # also called type hinting, this tells reader that function returns a list od doc objects
import logging # we use logging for easier debugging,better production
from langchain_core.documents import Document #important class of langchain
from langchain_community.document_loaders import PyPDFLoader # thos class reads pdfs
from src.config import PDF_DIR # thats wahy we built config.py first

#Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def load_documents() -> List[Document]:
    """
    Load all PDF documents from the dataset.

    Returns:
        List[Document]: List of LangChain Document objects.
    """

    documents: List[Document] = []

    pdf_files = list(PDF_DIR.rglob("*.pdf"))

    logger.info(f"Found {len(pdf_files)} PDF files.")

    if not pdf_files:
        raise FileNotFoundError(
            f"No PDF files found in {PDF_DIR}"
        )

    for pdf_path in pdf_files:
        try:
            loader = PyPDFLoader(str(pdf_path))
            docs = loader.load()
            documents.extend(docs)

        except Exception as e:
            logger.error(f"Error loading {pdf_path.name}: {e}")

    logger.info(f"Loaded {len(documents)} pages.")

    return documents
     
    






    pdf_files = list(PDF_DIR.rglob("*.pdf")) # rglob= search recursivly through all sub folder
    logger.info(f"Found {len(pdf_files)} PDF files.")

    for pdf_path in pdf_files:
        try:
            loader = PyPDFLoader(str(pdf_path)) #create a loader for one pdf
            docs = loader.load()  #this reads the pdf 
            documents.extend(docs)
        
        except Exception as e:
            logger.error(f"Error loading {pdf_path.name}: {e}")

    logger.info(f"Loaded {len(documents)} pages.")

    return documents