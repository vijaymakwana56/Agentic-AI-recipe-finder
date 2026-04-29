# Agentic Recipe AI System (RAG + Web Search + LangGraph)

A **production-ready agentic AI system** that intelligently retrieves and generates recipes using a hybrid approach:

* **Semantic Search (RAG)** via Qdrant Vector DB
* **Web Search Fallback** via Tavily
* **LLM Reasoning + Tool Calling** via LangGraph (ReAct Architecture)

This system ensures **high-quality, grounded, and context-aware recipe generation** by combining structured retrieval with real-time web knowledge.

---

# Key Features

### Agentic AI (ReAct Loop)

* Multi-step reasoning using **LangGraph**
* Dynamic **tool selection (RAG → Web fallback)**
* Iterative execution: *Think → Act → Observe → Respond*

---

### 🔍 Semantic Recipe Retrieval (RAG)

* Powered by **BAAI/bge-m3 embeddings**
* Uses **Qdrant vector database**
* Understands **intent, synonyms, and context**

  * Example: *"aubergine curry"* → retrieves *eggplant recipes*

---

### Web Search Fallback

* Integrated with **Tavily API**
* Automatically triggered when:

  * RAG returns low-quality results
  * Query requires real-time or external knowledge

---

### Clean Answer Generation

* LLM synthesizes:

  * Recipe Name
  * Ingredients
  * Step-by-step Instructions
  * Optional tips
* Avoids dumping raw retrieval output

---

# System Architecture

```text
User Query
    ↓
Agent (LLM - Groq)
    ↓
Decision (Tool?)
   ↙        ↘
RAG Tool   Final Answer
   ↓
Qdrant Search
   ↓
Tool Result
   ↓
Agent (LLM again)
   ↓
Final Response
```

---

#  Tech Stack

### AI / LLM

* Groq (LLaMA 3.3)
* LangGraph (Agent orchestration)
* LangChain (Tool integration)

### Retrieval

* Qdrant (Vector DB)
* HuggingFace Embeddings (**BAAI/bge-m3**)

### Web Search

* Tavily API

### Backend

* Python 3.10+
* Pandas, Regex

---

# Core Components

---

## 1. RAG Tool (Semantic Retrieval)

Uses Qdrant + BGE-M3 from Hugging Face to fetch the most relevant recipes.

### Functionality:

* Converts query → embedding
* Searches vector DB
* Returns top-k relevant recipes

### Example:

```python
def rag_search_recipe(query: str) -> str:
    docs = retriever.get_relevant_documents(query)
    return docs[0].page_content if docs else "NO_RESULTS"
```

---

## 2. Web Search Tool (Fallback)

Uses Tavily when RAG is insufficient.

```python
def web_search_tool(query: str) -> str:
    response = requests.post(
        "https://api.tavily.com/search",
        json={
            "api_key": os.getenv("TAVILY_API_KEY"),
            "query": query,
            "search_depth": "basic"
        }
    )
    return response.text
```

---

## 3. Agent (LangGraph Node)

Responsible for:

* Deciding which tool to call
* Generating final answer

```python
llm = ChatGroq(...).bind_tools([rag_search_recipe, web_search_tool])
```

---

## 4. Tool Execution Node

Executes tool calls and returns results to agent.

---

## 5. LangGraph Workflow

```python
START → agent
         ↓
   (tool call?)
     ↙     ↘
  tools     END
     ↓
   agent (loop)
```

---

# Semantic Recipe Search Engine (RAG Core)

## Overview

A high-performance, multilingual recipe retrieval system powered by **BAAI/bge-m3** and **Qdrant Vector Database**.

---

## Features

* Semantic search across ingredients & intent
* 1024-dimensional embeddings
* Batch processing for scalability
* Handles 6,000+ recipes efficiently

---

## Pipeline

### 1. Preprocessing

* Clean titles (`(recipe)` removal)
* Normalize whitespace
* Combine fields → single context

---

### 2. Embedding

* Model: **BAAI/bge-m3**
* Output: 1024-dim dense vectors

---

### 3. Ingestion

* Qdrant collection (COSINE similarity)
* Chunked uploads (avoid API limits)

---

### 4. Retrieval

```python
results = client.search(
    collection_name="recipe_collection",
    query_vector=query_vector,
    limit=5
)
```

---

## Evaluation Metrics

* Hit Rate @ K
* Mean Reciprocal Rank (MRR)

---

# Installation

```bash
git clone https://github.com/vijaymakwana56/Agentic-AI-recipe-finder.git
cd agentic-recipe-ai

pip install -r requirements.txt
```

---

# Environment Variables

```env
GROQ_API_KEY=your_groq_key
TAVILY_API_KEY=your_tavily_key
HF_TOKEN=your_huggingface_token
QDRANT_URL=your_qdrant_url
QDRANT_API_KEY=your_qdrant_api_key
```

---

# Run the Application

```bash
python app.py
```

---

# Example Query

```text
Input:
"How to make butter chicken?"

Output:
- Recipe Name
- Ingredients
- Steps
- Tips
```

---

# Project Structure

```text
agentic_ai/
│── src/
│   ├── nodes/
│   │   ├── agent_node.py
│   │   ├── tool_node.py
│   ├── tools/
│   │   ├── rag_search.py
│   │   ├── web_search.py
│   ├── state_graph.py
│
│── app.py
│── requirements.txt
│── README.md
```

---

# Future Improvements

*  Recipe ranking & filtering
*  Multi-modal support (images)
*  Streaming responses
*  UI (Streamlit / React)
*  Evaluation dashboard

---

#  License

MIT License

---

#  Credits

* HuggingFace (BGE-M3)
* Qdrant Vector DB
* Tavily Search API
* LangGraph / LangChain

---

#  Final Note

This project demonstrates a **real-world agentic AI system** combining:

* Retrieval-Augmented Generation (RAG)
* Tool Calling
* Multi-step Reasoning (ReAct)

Built for **production-grade AI applications** 
