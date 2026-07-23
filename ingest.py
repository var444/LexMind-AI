"""
ingest.py

Creates the complete knowledge base.

Pipeline:

PDFs
    ↓
Documents
    ↓
Chunks
    ↓
Hugging Face Embeddings
    ↓
Qdrant
"""

from qdrant_client.models import Distance, VectorParams
from langchain_qdrant import QdrantVectorStore

from src.document_loader import load_documents
from src.text_splitter import split_documents
from src.embedding_model import get_embedding_model
from src.vector_store import get_qdrant_client

from src.config import COLLECTION_NAME

# BAAI/bge-base-en-v1.5 embedding size
VECTOR_SIZE = 768


def create_collection_if_not_exists(client):
    """
    Create the Qdrant collection if it doesn't already exist.
    """

    collections = client.get_collections().collections
    existing = [c.name for c in collections]

    if COLLECTION_NAME in existing:
        print(f"Collection '{COLLECTION_NAME}' already exists.")
        return

    print(f"Creating collection '{COLLECTION_NAME}'...")

    client.create_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=VectorParams(
            size=VECTOR_SIZE,
            distance=Distance.COSINE,
        ),
    )

    print("Collection created successfully.\n")


def main():

    print("=" * 60)
    print("Connecting to Qdrant...")
    print("=" * 60)

    client = get_qdrant_client()

    print("Connected to Qdrant successfully.\n")

    create_collection_if_not_exists(client)

    # --------------------------------------------------------
    # Skip ingestion if the collection already contains vectors
    # --------------------------------------------------------
    try:
        count = client.count(
            collection_name=COLLECTION_NAME,
            exact=True
        ).count

        if count > 0:
            print("=" * 60)
            print("Knowledge Base already exists.")
            print(f"Collection contains {count} vectors.")
            print("Skipping ingestion...")
            print("=" * 60)
            return

    except Exception:
        pass

    print("=" * 60)
    print("Loading PDF documents...")
    print("=" * 60)

    documents = load_documents()

    print(f"\nLoaded {len(documents)} pages.\n")

    print("=" * 60)
    print("Splitting documents into chunks...")
    print("=" * 60)

    chunks = split_documents(documents)

    print(f"\nCreated {len(chunks)} chunks.\n")

    print("=" * 60)
    print("Loading Hugging Face Embedding Model...")
    print("=" * 60)

    embedding_model = get_embedding_model()

    print("Embedding model loaded.\n")

    print("=" * 60)
    print("Initializing Vector Store...")
    print("=" * 60)

    vector_store = QdrantVectorStore(
        client=client,
        collection_name=COLLECTION_NAME,
        embedding=embedding_model,
    )

    print("Uploading document chunks...\n")

    vector_store.add_documents(chunks)

    print("\n" + "=" * 60)
    print("Knowledge Base Created Successfully!")
    print("=" * 60)


if __name__ == "__main__":
    main()