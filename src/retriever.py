"""
retriever.py

Creates a retriever that searches the Qdrant vector database.
"""

from langchain_qdrant import QdrantVectorStore

from src.config import COLLECTION_NAME
from src.embedding_model import get_embedding_model
from src.vector_store import get_qdrant_client


def get_retriever(k=5):
    """
    Returns a retriever that fetches the top-k
    most relevant document chunks.
    """

    embedding_model = get_embedding_model()

    client = get_qdrant_client()

    vector_store = QdrantVectorStore(
        client=client,
        collection_name=COLLECTION_NAME,
        embedding=embedding_model,
    )

    retriever = vector_store.as_retriever(
        search_kwargs={"k": k}
    )

    return retriever