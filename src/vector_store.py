"""
vector_store.py

Creates and returns a connection to the local Qdrant server.

Responsibilities:
- Connect to Qdrant
- Verify the server is reachable

This module does NOT:
- Generate embeddings
- Upload documents
- Create collections
"""

from qdrant_client import QdrantClient

from src.config import (
    QDRANT_HOST,
    QDRANT_PORT,
)


def get_qdrant_client() -> QdrantClient:
    """
    Create and return a connected Qdrant client.

    Returns:
        QdrantClient: Connected Qdrant client.

    Raises:
        RuntimeError: If the Qdrant server is not reachable.
    """

    try:
        client = QdrantClient(
            host=QDRANT_HOST,
            port=QDRANT_PORT,
        )

        # Verify connection
        client.get_collections()

        print("✅ Connected to Qdrant successfully.")

        return client

    except Exception as e:
        raise RuntimeError(
            f"Failed to connect to Qdrant: {e}"
        )