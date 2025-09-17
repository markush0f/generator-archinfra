from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.core.db import get_session
from app.domain.tag.service import TagService
from app.domain.tag.schemas import TagCreate, TagRead, TagPage

router = APIRouter(prefix="/tag", tags=["tag"])

def get_service(session: Session = Depends(get_session)) -> TagService:
    return TagService(session)

@router.get("", response_model=TagPage)
def list_tag(offset: int = 0, limit: int = 50, svc: TagService = Depends(get_service)):
    items, total = svc.list_with_total(offset=offset, limit=limit)
    return TagPage(total=total, items=items)

@router.post("", response_model=TagRead)
def create_tag(payload: TagCreate, svc: TagService = Depends(get_service)):
    return svc.create(payload)
