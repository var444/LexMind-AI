from src.rag_chain import ask_question

question = "What is the termination clause?"

answer = ask_question(question)

print("=" * 80)
print("Question:")
print(question)
print("=" * 80)
print("Answer:")
print(answer)