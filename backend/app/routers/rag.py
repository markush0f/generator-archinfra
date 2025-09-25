from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.core.db import get_session
from app.domain.rag.service import RagService
from app.domain.rag.schemas import RagCreate, RagRead, RagPage

router = APIRouter(prefix="/rag", tags=["rag"])

def get_service(session: Session = Depends(get_session)) -> RagService:
    return RagService(session)

@router.get("", response_model=RagPage)
def list_rag(offset: int = 0, limit: int = 50, svc: RagService = Depends(get_service)):
    items, total = svc.list_with_total(offset=offset, limit=limit)
    return RagPage(total=total, items=items)

@router.post("", response_model=RagRead)
def create_rag(payload: RagCreate, svc: RagService = Depends(get_service)):
    return svc.create(payload)
