from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.domain.architecture.service import ArchitectureService
from app.domain.architecture.schemas import ArchitectureCreate, ArchitectureRead, ArchitecturePage
from app.core.database import get_session

router = APIRouter(prefix="/architecture", tags=["architecture"])

def get_service(session: Session = Depends(get_session)) -> ArchitectureService:
    return ArchitectureService(session)

@router.get("", response_model=ArchitecturePage)
def list_architecture(offset: int = 0, limit: int = 50, svc: ArchitectureService = Depends(get_service)):
    items, total = svc.list_with_total(offset=offset, limit=limit)
    return ArchitecturePage(total=total, items=items)

@router.post("", response_model=ArchitectureRead)
def create_architecture(payload: ArchitectureCreate, svc: ArchitectureService = Depends(get_service)):
    return svc.create(payload)
