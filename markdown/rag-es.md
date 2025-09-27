# 📚 Retrieval-Augmented Generation (RAG)

Este proyecto integra **RAG (Generación Aumentada con Recuperación)** . El objetivo es combinar el almacenamiento tradicional de datos con la búsqueda semántica y respuestas potenciadas por IA.

---

## 🔹 Cómo está implementado el RAG

### 1. Almacenamiento de documentos

* Los documentos y sus metadatos (título, proyecto, fuente, etc.) se guardan en **PostgreSQL** usando SQLModel.
* Esto asegura datos estructurados, consultas fáciles y relaciones consistentes.

### 2. Generación de embeddings

* El contenido de cada documento se convierte en **vectores de embeddings** usando el modelo local **all-mpnet-base-v2** (SentenceTransformers).
* Estos embeddings representan el significado semántico del texto.

### 3. Índice vectorial (FAISS)

* Los embeddings se almacenan en un **índice FAISS** (IndexFlatL2).
* FAISS permite realizar búsquedas rápidas de similitud entre vectores.
* El índice y la metadata de los documentos se guardan en disco para no perder datos al reiniciar la aplicación.

### 4. Añadir documentos

Cuando se añade un documento nuevo:

1. Se guarda en PostgreSQL.
2. Se genera su embedding.
3. El embedding y la metadata del documento se guardan en FAISS.

### 5. Búsqueda (Recuperación)

Cuando se hace una consulta:

1. La consulta se convierte en un embedding.
2. FAISS recupera los **k documentos más similares**.
3. El contenido original del documento y su metadata se devuelven junto con las puntuaciones de similitud.

### 6. Generación (Integración futura)

* Los documentos recuperados se pasan como **contexto** a un modelo de lenguaje (ej. Ollama u otro LLM).
* El modelo genera una respuesta con IA fundamentada en la información recuperada.

---

## ⚡ Beneficios de este enfoque

* Combina **almacenamiento estructurado** (Postgres) con **recuperación semántica** (FAISS).
* Asegura persistencia tanto de documentos como de embeddings.
* Permite una búsqueda rápida e inteligente sobre la información almacenada.
* Sienta la base para respuestas contextuales con RAG.

---

👉 Este sistema convierte la aplicación en algo más que un CRUD: una **plataforma mejorada con IA** capaz de recuperar conocimiento y generar información valiosa.
