import os
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

PDF_DIR = BASE_DIR / "data"  / "pdfs"

GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError(
        "GOOGLE_API_KEY not found. Please set it your .env file"
    )
LLM_MODEL = "gemini-2.5-flash"
EMBEDDING_MODEL = "models/gemini-embedding-001"

QDRANT_HOST = "localhost"
QDRANT_PORT = 6333
COLLECTION_NAME = "legal_contracts"

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200
TOP_K = 5