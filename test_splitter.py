from src.document_loader import load_documents
from src.text_splitter import split_documents

# Load all PDF pages
documents = load_documents()

print(f"\nTotal Documents : {len(documents)}")

# Split into chunks
chunks = split_documents(documents)

print(f"\nTotal Chunks : {len(chunks)}")

print("\nFirst Chunk:\n")
print(chunks[0].page_content[:500])

print("\nMetadata:\n")
print(chunks[0].metadata)