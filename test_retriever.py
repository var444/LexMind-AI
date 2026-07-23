from src.retriever import get_retriever

retriever = get_retriever()

query = "What is the termination clause?"

docs = retriever.invoke(query)

print("=" * 80)

for i, doc in enumerate(docs, start=1):
    print(f"\nResult {i}")
    print("-" * 80)
    print(doc.page_content[:1000])
    print()