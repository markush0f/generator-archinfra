from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.core.db import get_session
from app.domain.eag.service import EagService
from app.domain.eag.schemas import EagCreate, EagRead, EagPage

router = APIRouter(prefix="/eag", tags=["eag"])

def get_service(session: Session = Depends(get_session)) -> EagService:
    return EagService(session)

@router.get("", response_model=EagPage)
def list_eag(offset: int = 0, limit: int = 50, svc: EagService = Depends(get_service)):
    items, total = svc.list_with_total(offset=offset, limit=limit)
    return EagPage(total=total, items=items)

@router.post("", response_model=EagRead)
def create_eag(payload: EagCreate, svc: EagService = Depends(get_service)):
    return svc.create(payload)
