import os
import streamlit as st
from dotenv import load_dotenv

from vec_utils import text_from_pdf, build_vectorstore, load_vectorstore, query_vectorstore
from tools import calculator_tool, web_search_tool, email_sender_tool

# --- Modern LangChain & LangGraph imports ---
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import Tool
from langgraph.prebuilt import create_react_agent
from langchain_core.documents import Document

load_dotenv()

st.set_page_config(page_title="RAG Agent Demo", layout="wide")
st.title("Modern RAG + Tool Agent (LangGraph)")

OPENAI_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_KEY:
    st.error("Set OPENAI_API_KEY in your .env file")
    st.stop()

# ============ Sidebar: Index Building ============
st.sidebar.header("1) Upload docs & build index")
upload = st.sidebar.file_uploader("Upload TXT/PDF", accept_multiple_files=True)
action = st.sidebar.selectbox("Index action", ["Load", "Build", "Clear"])

if "vs" not in st.session_state:
    st.session_state.vs = None

if action == "Build":
    if upload:
        docs = []
        for f in upload:
            fname = f.name
            with open(fname, "wb") as out:
                out.write(f.read())
            if fname.endswith(".pdf"):
                text = text_from_pdf(fname)
            else:
                text = open(fname, "r", encoding="utf-8", errors="ignore").read()
            docs.append((fname, text))
        st.session_state.vs = build_vectorstore(docs)
        st.success("Index built.")
    else:
        st.info("Upload files first.")

elif action == "Load":
    vs = load_vectorstore()
    if vs:
        st.session_state.vs = vs
        st.success("Loaded index.")
    else:
        st.warning("No index found.")

elif action == "Clear":
    import shutil
    if os.path.exists("faiss_index"):
        shutil.rmtree("faiss_index")
        st.session_state.vs = None
        st.success("Index cleared.")
    else:
        st.info("Nothing to clear.")

st.sidebar.markdown("---")
st.sidebar.header("2) Tools")
st.sidebar.write("calculator, web_search, email_sender, retrieval")

# =================== TOOLS ======================

def rag_search(query: str):
    """RAG tool — fetches relevant chunks from FAISS"""
    if st.session_state.vs is None:
        return "No index found."
    docs = st.session_state.vs.similarity_search(query, k=4)
    context = "\n\n".join([d.page_content for d in docs])
    return context

tools = [
    Tool(
        name="calculator",
        func=lambda q: str(calculator_tool(q)),
        description="Evaluate math expressions."
    ),
    Tool(
        name="web_search",
        func=lambda q: str(web_search_tool(q)),
        description="Search the web."
    ),
    Tool(
        name="email_sender",
        func=lambda q: str(email_sender_tool(*q.split('|', 2))),
        description="Send email: recipient|subject|body"
    ),
    Tool(
        name="retrieval",
        func=lambda q: rag_search(q),
        description="Search uploaded documents using RAG."
    ),
]

# =================== AGENT ======================

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

agent = create_react_agent(llm, tools)

# =================== UI =========================

st.header("Ask the Agent")
query = st.text_area("Your question", height=120)
run = st.button("Run")

if run and query.strip():
    with st.spinner("Thinking..."):
        result = agent.invoke({"input": query})
    st.subheader("Agent Response")
    st.write(result["output"])

    if st.session_state.vs:
        st.markdown("---")
        st.subheader("Top RAG Chunks")
        docs = query_vectorstore(st.session_state.vs, query, k=4)
        for d, score in docs:
            st.write(f"Source: {d.metadata.get('source')} | Score: {score:.4f}")
            st.write(d.page_content[:400])
            st.markdown("---")
