from fastapi import APIRouter, Depends
from app.domain.rag.embedding_service import EmbeddingService
from app.domain.rag.schemas import DocumentCreate
from sqlmodel import Session
from app.core.database import get_session
from app.domain.rag import models

router = APIRouter(prefix="/rag", tags=["RAG"])
service = EmbeddingService()

@router.post("/add")
def add_documents(docs: list[DocumentCreate], session: Session = Depends(get_session)):
    # guardar en Postgres
    db_docs = []
    for doc in docs:
        db_doc = models.Document(**doc.dict())
        session.add(db_doc)
        db_docs.append(db_doc.dict())
    session.commit()
    # añadir a FAISS
    added = service.add_documents(db_docs)
    return {"added": added}

@router.get("/search")
def search_docs(query: str, k: int = 5):
    return {"results": service.search(query, k)}
