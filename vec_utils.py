import os
from typing import List, Tuple

# Robust imports for text splitter, embeddings, and FAISS vectorstore
try:
    from langchain_text_splitters import RecursiveCharacterTextSplitter
except Exception:
    # fallback to older path (if present)
    try:
        from langchain.text_splitter import RecursiveCharacterTextSplitter
    except Exception:
        raise ImportError("Install langchain_text_splitters or a compatible langchain version.")

# Embeddings
try:
    from langchain_openai import OpenAIEmbeddings
except Exception:
    try:
        from langchain.embeddings import OpenAIEmbeddings
    except Exception:
        raise ImportError("Install langchain-openai or a compatible langchain embeddings package.")

# FAISS vectorstore
try:
    from langchain_community.vectorstores import FAISS
except Exception:
    try:
        from langchain.vectorstores import FAISS
    except Exception:
        raise ImportError("Install langchain-community or a compatible langchain vectorstores package.")

# PDF reading
def text_from_pdf(file_path: str) -> str:
    import pdfplumber
    text = []
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            t = page.extract_text()
            if t:
                text.append(t)
    return "\n".join(text)


# Chunking
CHUNK_SIZE = 800
CHUNK_OVERLAP = 150


def chunk_text(text: str) -> List[str]:
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        separators=["\n\n", "\n", " "],
    )
    return splitter.split_text(text)


# Build vectorstore from list of (doc_id, text)
def build_vectorstore(docs: List[Tuple[str, str]], persist_dir: str = "faiss_index"):
    os.makedirs(persist_dir, exist_ok=True)
    texts = []
    metadatas = []
    for doc_id, content in docs:
        chunks = chunk_text(content)
        for i, c in enumerate(chunks):
            texts.append(c)
            metadatas.append({"source": doc_id, "chunk": i})
    embed = OpenAIEmbeddings()
    faiss_index = FAISS.from_texts(texts, embed, metadatas=metadatas)
    faiss_index.save_local(persist_dir)
    return faiss_index


def load_vectorstore(persist_dir: str = "faiss_index"):
    if not os.path.exists(persist_dir):
        return None
    embed = OpenAIEmbeddings()
    return FAISS.load_local(persist_dir, embed)


def query_vectorstore(vs, query: str, k: int = 4):
    if vs is None:
        return []
    docs = vs.similarity_search_with_score(query, k=k)
    return docs