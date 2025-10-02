# 🏗️ Generator-ArchInfra

**Generator-ArchInfra** es un proyecto que permite crear y seleccionar arquitecturas de software de forma dinámica utilizando **FastAPI**, **React/Vite**, **PostgreSQL con pgvector** y un sistema de **RAG (Retrieval Augmented Generation)** para elegir la plantilla adecuada según una consulta en lenguaje natural.

---

## 🔹 Tecnologías principales

* **Backend:** FastAPI + SQLModel + Alembic
* **Frontend:** React + TypeScript + Vite
* **Base de datos:** PostgreSQL con extensión `pgvector`
* **Embeddings:** `all-mpnet-base-v2` (modelo local) o modelos premium (ej. OpenAI Embeddings)
* **Infraestructura:** Docker + Docker Compose

---

## 🔹 Requisitos previos

1. **Python 3.11+**
2. **Docker y Docker Compose** instalados
3. **Node.js 18+** (para el frontend)
4. **Instalar dependencias**:

   ```bash
   pip install -r requirements.txt
   npm install --prefix frontend
   ```

---

## 🔹 Levantar entorno de desarrollo

### 1. Base de datos con pgvector

```bash
docker compose up -d db adminer
```

* Accede a **Adminer** en: [http://localhost:8080](http://localhost:8080)
* Usuario: `user`
* Password: `1234`
* BD: `archinfra`

---

### 2. Migraciones de la base de datos

Inicializa el esquema con Alembic:

```bash
alembic upgrade head
```

Esto creará todas las tablas (`architecture`, `architecture_embedding`, etc.).

---

### 3. Cargar seeds iniciales

Ejecuta los seeds SQL:

```bash
psql -U user -d archinfra -f seeds/seeds_architectures.sql
```

Luego genera embeddings para esas arquitecturas:

```bash
python seed_embeddings.py
```

---

### 4. Ejecutar backend (FastAPI)

```bash
uvicorn app.main:app --reload
```

API disponible en: [http://localhost:8000/docs](http://localhost:8000/docs)

---

### 5. Ejecutar frontend

```bash
cd frontend
npm run dev
```

Frontend disponible en: [http://localhost:5173](http://localhost:5173)

---

## 🔹 Endpoints principales

### Crear una arquitectura (con embedding automático)

```http
POST /architecture
{
  "name": "fastapi-backend",
  "description": "Arquitectura base para APIs con FastAPI."
}
```

### Elegir arquitectura con RAG

```http
GET /architecture/choose?query=quiero un backend con fastapi y postgres
```

📌 Respuesta:

```json
{
  "id": 1,
  "name": "fastapi-backend",
  "description": "Arquitectura base para APIs con FastAPI.",
  "similarity": 0.94
}
```

---

## 🔹 Flujo de trabajo del RAG

1. Seeds cargan arquitecturas en la tabla `architecture`.
2. Script/endpoint genera embeddings con el modelo (`all-mpnet-base-v2`) → guardados en `architecture_embedding`.
3. Usuario hace consulta → se convierte en embedding.
4. Se compara con embeddings en BD (pgvector).
5. Devuelve la arquitectura más parecida para iniciar el **scaffolding**.

---

## ✅ Conclusión

Con este entorno puedes:

* **Añadir nuevas arquitecturas dinámicamente**.
* **Generar embeddings automáticamente**.
* **Recuperar arquitecturas vía RAG** según consultas en lenguaje natural.
* Preparar scaffolding personalizado para proyectos de IA, APIs, SaaS o frontend.

---

👉 Próximo paso: configurar un despliegue en **producción** con Docker Compose (backend + frontend + Postgres en modo prod).
