from src.document_loader import load_documents

documents = load_documents()

print("=" * 50)
print(f"Total Pages Loaded: {len(documents)}")
print("=" * 50)

# Print first document preview
print("\nFirst Document Preview:\n")
print(documents[0].page_content[:500])

print("\nMetadata:\n")
print(documents[0].metadata)