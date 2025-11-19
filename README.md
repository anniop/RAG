🚀 Overview
-----------

This project is a **modern** Retrieval-Augmented Generation (RAG) + AI Agent system built using:

*   **Streamlit** – UI
    
*   **LangChain + LangGraph** – Agent & RAG orchestration
    
*   **OpenAI** – LLM + Embeddings
    
*   **FAISS** – Vector database
    
*   **Custom Tools** – Calculator, Web Search, Email Sender, RAG Retrieval
    

It lets users:

*   Upload **PDF / TXT documents**
    
*   Build a **FAISS vector store**
    
*   Ask questions from the documents (**RAG**)
    
*   Use an **AI Agent** that can call tools automatically
    
*   Perform external tasks (web search, calculator, email mock)
    

This is the correct approach for **2024–2025 LangChain**, since old agents (initialize\_agent, AgentType, RetrievalQA) are deprecated or removed.

📂 Project Structure
--------------------

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   project/  │── app.py  │── vec_utils.py  │── tools.py  │── requirements.txt  │── .env  │── README.md  └── faiss_index/     (auto-created)   `

📦 Requirements
---------------

Install dependencies:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   pip install -r requirements.txt   `

### Main packages used

*   streamlit
    
*   openai
    
*   langchain
    
*   langchain-openai
    
*   langchain-community
    
*   langchain-text-splitters
    
*   langgraph
    
*   faiss-cpu
    
*   pdfplumber
    

🔑 Environment Variables
------------------------

Create a file **.env**:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   OPENAI_API_KEY=your_key_here  SERPAPI_API_KEY=optional_key   `

▶️ Running the App
------------------

Activate your virtual environment:

### Windows (PowerShell)

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   .\.venv\Scripts\Activate.ps1   `

### macOS / Linux

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   source .venv/bin/activate   `

Start Streamlit:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   streamlit run app.py   `

🧩 Features
-----------

### ✔️ 1. Document Upload

Upload:

*   PDF files
    
*   TXT files
    

The app extracts text, chunks it, creates embeddings, and builds a FAISS vector index.

### ✔️ 2. RAG (Retrieval-Augmented Generation)

A custom **retrieval tool** (retrieval) lets the agent fetch relevant chunks:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   Tool(name="retrieval", func=rag_search, ...)   `

### ✔️ 3. AI Agent with Tools (LangGraph)

The project uses a modern **LangGraph ReAct Agent**:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   from langgraph.prebuilt import create_react_agent  agent = create_react_agent(llm, tools)   `

The agent can call:

Tool NameFunctionalitycalculatorSafe math evaluatorweb\_searchSerpAPI → DuckDuckGoemail\_senderMock email senderretrievalRAG over uploaded docs

🛠 Custom Tools
---------------

All custom tools are defined in **tools.py**:

*   **calculator** → evaluates expressions like "2+3\*10"
    
*   **web\_search** → internet search via SerpAPI or DuckDuckGo
    
*   **email\_sender** → mock demonstration tool
    
*   **retrieval** → searches FAISS vectorstore using user's uploaded documents
    

🧠 How the Agent Works
----------------------

The LangGraph agent follows **ReAct pattern**:

*   Looks at your input
    
*   Decides whether it needs tool assistance
    
*   Calls a tool if needed
    
*   Reasons about the tool output
    
*   Produces a final answer
    

🖥 UI Flow (Streamlit)
----------------------

1.  **Upload docs**
    
2.  Build vector index
    
3.  Ask a question or command
    
4.  Agent responds, optionally calling tools
    
5.  Retrieved chunks (RAG context) shown for transparency
    

🧪 Example Queries
------------------

Try:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   summarize the uploaded documents   `

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   search the web for latest updates on AI research   `

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   calculate 2*(32/4)+5   `

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   email_sender john@example.com|Meeting|We have a meeting at 5pm   `

🛑 Troubleshooting
------------------

### Missing imports (RetrievalQA, initialize\_agent)

These are **deprecated**.This project uses **modern LangGraph**, so no deprecated imports are required.

### FAISS errors on Windows

Make sure faiss-cpu matches your Python version.

### PDF text not extracted

Try installing:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   pip install PyPDF2   `

🏁 Final Notes
--------------

This project is fully compatible with **LangChain 2024–2025**, avoids deprecated APIs, and uses LangGraph—the correct agent framework going forward.

If you want a **more advanced version** (chat history, memory, Pinecone, auth, better UI), just ask:

➡️ _“Upgrade project to advanced version”_

Happy building! 🚀