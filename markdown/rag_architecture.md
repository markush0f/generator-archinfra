# 🚀 Flujo de RAG para elegir arquitectura

## 1. Base de conocimiento (BD)

* **Tabla `architecture`**: lista de arquitecturas disponibles.
* **Tabla `architecture_embedding`**: vector numérico (embedding) de cada arquitectura.

Ejemplo:

```sql
architecture
-------------
1 | fastapi   | Backend con FastAPI y PostgreSQL
2 | react     | Frontend con React, Vite y Tailwind
3 | fullstack | React + FastAPI + Docker + PostgreSQL
```

---

## 2. Preparar embeddings

* Se genera un embedding para cada arquitectura usando `all-mpnet-base-v2`.
* Se guarda en Postgres (extensión **pgvector**).

```python
text = "Backend con FastAPI y PostgreSQL"
embedding = model.encode(text)  # vector de 768 dimensiones
guardar_en_pgvector(arch_id=1, embedding=embedding)
```

---

## 3. Consulta del usuario

Ejemplo:

```
"Quiero una aplicación con backend en FastAPI y una base de datos PostgreSQL"
```

---

## 4. Procesamiento de la consulta

* Se convierte el texto en embedding con el mismo modelo.

```python
query = "Quiero un backend con FastAPI y Postgres"
query_vec = model.encode(query)
```

---

## 5. Comparación en la BD

Se busca el embedding más similar con **pgvector**:

```sql
SELECT a.id, a.name, a.description,
       1 - (e.embedding <=> %s) AS similarity
FROM architecture a
JOIN architecture_embedding e ON e.architecture_id = a.id
ORDER BY similarity DESC
LIMIT 1;
```

👉 El más parecido se devuelve con su score de similitud.

---

## 6. Selección de arquitectura

Ejemplo de resultado:

```
id = 1
name = fastapi
similarity = 0.92
```

La arquitectura correcta es **FastAPI**.

---

## 7. Ejecución del scaffolding

Con la arquitectura elegida se lanza el generador correspondiente:

```python
run_scaffolding("fastapi")
```

Este crea automáticamente:

* `models.py`
* `repository.py`
* `service.py`
* `router.py`

---

## 🔄 Resumen del flujo

1. **Definir arquitecturas** → se guardan en BD.
2. **Generar embeddings** → modelo local `all-mpnet-base-v2` + pgvector.
3. **Consulta del usuario** → texto en lenguaje natural.
4. **Embedding de consulta** → vector numérico.
5. **Comparación en BD** → similitud coseno.
6. **Selección** → arquitectura más cercana.
7. **Scaffolding** → se genera el código automáticamente.
