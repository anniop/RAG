Here is the **raw source code** of the `README.md` file — exactly as Markdown text.
Just copy-paste into a file named **README.md**.

---

# ✅ **README.md (Source Code)**

*(Copy everything below into README.md)*

```markdown
# 📘 Streamlit RAG + Tools Agent (LangGraph Version)

## 🚀 Overview  
This project is a **modern** Retrieval-Augmented Generation (RAG) + AI Agent system built using:

- **Streamlit** – UI  
- **LangChain + LangGraph** – Agent & RAG orchestration  
- **OpenAI** – LLM + Embeddings  
- **FAISS** – Vector database  
- **Custom Tools** – Calculator, Web Search, Email Sender, RAG Retrieval  

It lets users:

- Upload **PDF / TXT documents**
- Build a **FAISS vector store**
- Ask questions from the documents (**RAG**)  
- Use an **AI Agent** that can call tools automatically  
- Perform external tasks (web search, calculator, email mock)  

This is the correct approach for **2024–2025 LangChain**, since old agents (`initialize_agent`, `AgentType`, `RetrievalQA`) are deprecated or removed.

---

## 📂 Project Structure
```

project/
│── app.py
│── vec_utils.py
│── tools.py
│── requirements.txt
│── .env
│── README.md
└── faiss_index/     (auto-created)

````

---

## 📦 Requirements

Install dependencies:

```bash
pip install -r requirements.txt
````

### Main packages used

* streamlit
* openai
* langchain
* langchain-openai
* langchain-community
* langchain-text-splitters
* langgraph
* faiss-cpu
* pdfplumber

---

## 🔑 Environment Variables

Create `.env`:

```
OPENAI_API_KEY=your_key
SERPAPI_API_KEY=optional
```

---

## ▶️ Running the App

### Windows (PowerShell)

```powershell
.\.venv\Scripts\Activate.ps1
```

### macOS / Linux

```bash
source .venv/bin/activate
```

Start Streamlit:

```bash
streamlit run app.py
```

---

## 🧩 Features

### ✔️ 1. Document Upload

Upload:

* PDF files
* TXT files

The app extracts text, chunks it, creates embeddings, and builds a FAISS vector index.

---

### ✔️ 2. Retrieval-Augmented Generation (RAG)

A custom **retrieval tool** allows the agent to fetch relevant chunks:

```python
Tool(name="retrieval", func=rag_search, ...)
```

---

### ✔️ 3. AI Agent with Tools (LangGraph)

Uses a **modern LangGraph ReAct agent**:

```python
from langgraph.prebuilt import create_react_agent
agent = create_react_agent(llm, tools)
```

The agent can use:

| Tool Name    | Functionality                   |
| ------------ | ------------------------------- |
| calculator   | Safe math evaluator             |
| web_search   | SerpAPI → DuckDuckGo            |
| email_sender | Mock email sender               |
| retrieval    | Search uploaded docs with FAISS |

---

## 🛠 Custom Tools

Defined in **tools.py**:

* **calculator** – evaluates math expressions
* **web_search** – searches the web
* **email_sender** – mock email tool
* **retrieval** – RAG search in FAISS

---

## 🧠 How the Agent Works

The agent follows **ReAct reasoning**:

1. Looks at user question
2. Decides if a tool is needed
3. Calls tools
4. Thinks again
5. Produces final answer

---

## 🖥 UI Flow (Streamlit)

1. Upload documents
2. Build vector index
3. Type a question or command
4. Agent responds (may call tools)
5. RAG chunks shown for transparency

---

## 🧪 Example Queries

```
summarize the uploaded documents
```

```
calculate 2*(32/4)+9
```

```
search the web for latest news on AI startups
```

```
email_sender john@example.com|Meeting|Let's meet at 6 PM today
```

---

## 🛑 Troubleshooting

### ❌ Missing imports (RetrievalQA, initialize_agent)

These are **deprecated** in modern LangChain.
This project uses **LangGraph** instead (recommended by LangChain authors).

### ❌ FAISS errors on Windows

Install compatible version:

```bash
pip install faiss-cpu
```

---

## 🏁 Final Notes

This project is fully compatible with the **latest LangChain + LangGraph (2024–2025)**.

If you want an **advanced version** with:

* Chat history
* Memory
* Pinecone / Chroma
* Authentication
* Cleaner UI

Just ask:
👉 **“Upgrade this project to advanced version”**

```

---

If you want, I can also generate:
✅ `LICENSE`  
✅ `.gitignore`  
✅ GitHub-ready folder structure  
Just tell me!
```
