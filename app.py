import streamlit as st
from src.rag_chain import ask_question

# ---------------- Page Config ---------------- #
st.set_page_config(
    page_title="LexMind AI",
    page_icon="⚖️",
    layout="wide"
)

# ---------------- Session State ---------------- #
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------- Sidebar ---------------- #
with st.sidebar:
    st.title("⚖️ LexMind AI")
    st.caption("Legal RAG Assistant")

    st.divider()

    st.subheader("📊 Project Information")

    st.metric("📄 Documents", "510")
    st.metric("🤖 Model", "Gemini 2.5 Flash")
    st.metric("🗄️ Vector DB", "Qdrant")
    st.metric("🧩 Chunks", "37,179")

    st.divider()

    if st.button("🗑 Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

# ---------------- Header ---------------- #
st.title("⚖️ LexMind AI")
st.caption("AI-Powered Legal Contract Assistant")

st.markdown("""
Ask questions about your uploaded legal contracts using **Retrieval-Augmented Generation (RAG)**.

**Tech Stack:** Streamlit • LangChain • Google Gemini • Qdrant
""")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("📄 Documents", "510")

with col2:
    st.metric("🧩 Chunks", "37,179")

with col3:
    st.metric("🤖 Model", "Gemini 2.5 Flash")

st.divider()

# ---------------- Welcome ---------------- #
if not st.session_state.messages:
    st.success("""
👋 **Welcome to LexMind AI**

Ask anything about your legal contracts.

### Example Questions
- What is the termination clause?
- Summarize this agreement.
- What are the payment terms?
- Who are the parties involved?
""")

# ---------------- Display Previous Messages ---------------- #
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

        if message["role"] == "assistant" and message.get("sources"):

            with st.expander("📂 Retrieved Sources"):

                for doc in message["sources"]:

                    filename = doc.metadata.get(
                        "source", "Unknown"
                    ).split("/")[-1].split("\\")[-1]

                    page = doc.metadata.get("page", "N/A")

                    st.markdown(f"### 📄 {filename}")
                    st.caption(f"Page: {page}")

                    preview = doc.page_content.strip()

                    if len(preview) > 300:
                        preview = preview[:300] + "..."

                    st.text(preview)

                    st.divider()

# ---------------- Chat Input ---------------- #
question = st.chat_input("💬 Ask a legal question...")

if question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):

        with st.spinner("🔍 Searching legal documents..."):

            try:
                result = ask_question(question)

                answer = result.get(
                    "answer",
                    "No answer generated."
                )

                sources = result.get(
                    "sources",
                    []
                )

            except Exception as e:
                answer = f"❌ Error: {e}"
                sources = []

        st.markdown(answer)

        st.caption(
            f"📚 Retrieved {len(sources)} relevant document(s)."
        )

        if sources:

            with st.expander("📂 Retrieved Sources"):

                for doc in sources:

                    filename = doc.metadata.get(
                        "source", "Unknown"
                    ).split("/")[-1].split("\\")[-1]

                    page = doc.metadata.get("page", "N/A")

                    st.markdown(f"### 📄 {filename}")
                    st.caption(f"Page: {page}")

                    preview = doc.page_content.strip()

                    if len(preview) > 300:
                        preview = preview[:300] + "..."

                    st.text(preview)

                    st.divider()

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer,
                "sources": sources
            }
        )

# ---------------- Footer ---------------- #
st.divider()

st.caption(
    "⚖️ LexMind AI | Built with Streamlit • LangChain • Google Gemini • Qdrant"
)