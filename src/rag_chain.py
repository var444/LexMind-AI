from langchain_core.prompts import ChatPromptTemplate

from src.retriever import get_retriever
from src.llm import get_llm


prompt = ChatPromptTemplate.from_template(
    """
You are an AI Legal Assistant.

Answer the user's question ONLY from the provided context.

If the answer is not present in the context, say:
"I couldn't find that information in the uploaded documents."

Context:
{context}

Question:
{question}

Answer:
"""
)


def ask_question(question):

    retriever = get_retriever()

    docs = retriever.invoke(question)

    context = "\n\n".join(
        doc.page_content for doc in docs
    )

    llm = get_llm()

    formatted_prompt = prompt.format(
        context=context,
        question=question,
    )

    response = llm.invoke(formatted_prompt)

    return {
    "answer": response.content,
    "sources": docs
}