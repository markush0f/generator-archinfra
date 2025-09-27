# 📚 Retrieval-Augmented Generation (RAG)

This project integrates **RAG (Retrieval-Augmented Generation)**. The goal is to combine traditional data storage with semantic search and AI-powered responses.

---

## 🔹 How RAG is Implemented

### 1. Document Storage

* Documents and their metadata (title, project, source, etc.) are stored in **PostgreSQL** using SQLModel.
* This ensures structured data, easy querying, and relational integrity.

### 2. Embedding Generation

* Each document's content is converted into **vector embeddings** using the local model **all-mpnet-base-v2** (SentenceTransformers).
* These embeddings represent the semantic meaning of the text.

### 3. Vector Index (FAISS)

* Embeddings are stored inside a **FAISS index** (IndexFlatL2).
* FAISS allows fast similarity search between vectors.
* The index and document metadata are persisted on disk so data is not lost when restarting the app.

### 4. Adding Documents

When a new document is added:

1. It is saved in PostgreSQL.
2. Its embedding is generated.
3. The embedding and document metadata are stored in FAISS.

### 5. Searching (Retrieval)

When a query is made:

1. The query is converted into an embedding.
2. FAISS retrieves the **k most similar documents**.
3. The original document content and metadata are returned along with similarity scores.

### 6. Generation (Future Integration)

* Retrieved documents are passed as **context** to a language model (e.g., via Ollama or another LLM).
* The model generates an AI-powered answer that is grounded in the retrieved information.

---

## ⚡ Benefits of This Approach

* Combines **structured storage** (Postgres) with **semantic retrieval** (FAISS).
* Ensures persistence of both documents and embeddings.
* Allows fast, intelligent search across stored information.
* Prepares the foundation for contextual AI responses with RAG.

---

👉 This setup makes the application not just a CRUD system, but an **AI-enhanced platform** capable of retrieving knowledge and generating meaningful insights.
