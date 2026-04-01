# 🤖 AI Research Agent

🚀 A powerful **AI-powered research assistant** built using modern LLM tools.
It can search the web 🌐, fetch research papers 📄, and generate intelligent answers 🧠 in real-time.

🔗 **Live Demo:**
👉 https://research-aiagent-bphlwappxh98zzjzxdqu7xm.streamlit.app/

---

## ✨ Features

* 🔍 Web search with real-time results
* 📄 Research paper retrieval from arXiv
* 🧠 Advanced reasoning using Groq LLM
* 🔁 Tool-using agent (LangGraph loop)
* ⚡ Fast and optimized responses
* 💬 Smooth chat UI with Streamlit

---

## 🧰 Tech Stack & Tools

### 🔗 LangChain

<img src="https://raw.githubusercontent.com/langchain-ai/langchain/master/docs/static/img/logo.png" width="120"/>

* Framework for building LLM applications
* Handles prompts, tools, and integrations
* Acts as the backbone connecting LLM + tools

---

### 🔄 LangGraph

<img src="https://miro.medium.com/v2/resize:fit:600/1*4VnZyYtYb1N4v8p4Yqk7Xg.png" width="120"/>

* Used to create **agent workflows (graphs)**
* Enables looping between LLM and tools
* Makes the agent decision-making structured

---

### ⚡ Groq (LLM)

<img src="https://groq.com/wp-content/uploads/2024/03/logo.svg" width="120"/>

* Ultra-fast inference engine for LLMs
* Runs models like **Llama3 / Qwen**
* Provides low-latency responses ⚡

---

### 🔍 Tavily Search

<img src="https://avatars.githubusercontent.com/u/139521400?s=200&v=4" width="120"/>

* Real-time web search API
* Optimized for LLM agents
* Fetches up-to-date information from the internet

---

### 📄 arXiv

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/ArXiv_logo_2022.svg/512px-ArXiv_logo_2022.svg.png" width="120"/>

* Access to **research papers** (ML, AI, etc.)
* Used for academic and technical queries
* Custom tool avoids rate-limit issues

---

### 🎨 Streamlit

<img src="https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png" width="120"/>

* Builds interactive web UI easily
* Provides chat interface for the agent
* Enables quick deployment

---

### 🚀 FastAPI

<img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" width="120"/>

* Backend API framework
* Used for production deployment
* High performance and async support

---

## 🏗️ Project Structure

```
agent_project/
│
├── app/
│   ├── config.py
│   ├── state.py
│   ├── tools.py
│   ├── nodes.py
│   ├── graph.py
│   └── utils.py
│
├── main.py
├── api.py
├── ui.py
├── requirements.txt
└── .env
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repo

```
git clone https://github.com/your-username/research-ai-agent.git
cd research-ai-agent
```

---

### 2️⃣ Create Virtual Environment

```
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

### 4️⃣ Add API Keys

Create `.env` file:

```
GROQ_API_KEY=your_key
TAVILY_API_KEY=your_key
```

---

## ▶️ Run the Project

### 💬 Streamlit UI

```
streamlit run ui.py
```

### 🖥️ CLI

```
python main.py
```

### 🌐 FastAPI

```
uvicorn api:app --reload
```

---

## 🧠 How It Works

```
User Query
   ↓
LLM (Groq)
   ↓
LangGraph decides → Tool needed?
   ↓
Tavily / arXiv
   ↓
LLM refines answer
   ↓
Final Output
```

---

## 🚀 Deployment

Deployed on Streamlit Cloud:
👉 https://research-aiagent-bphlwappxh98zzjzxdqu7xm.streamlit.app/

---

## 📌 Future Improvements

* 🧠 Add memory (chat history)
* 📚 RAG with vector database
* ⚡ Streaming responses
* 🤖 Multi-agent system

---

## 👨‍💻 Author

**Anmol Rajpoot**
🎓 IIIT Bhopal
💡 AI/ML | GenAI | LLMs

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
