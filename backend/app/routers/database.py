from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.domain.database.service import DatabaseService
from app.domain.database.schemas import DatabaseCreate, DatabaseRead, DatabasePage
from app.core.database import get_session

router = APIRouter(prefix="/database", tags=["database"])

def get_service(session: Session = Depends(get_session)) -> DatabaseService:
    return DatabaseService(session)

@router.get("", response_model=DatabasePage)
def list_database(offset: int = 0, limit: int = 50, svc: DatabaseService = Depends(get_service)):
    items, total = svc.list_with_total(offset=offset, limit=limit)
    return DatabasePage(total=total, items=items)

@router.post("", response_model=DatabaseRead)
def create_database(payload: DatabaseCreate, svc: DatabaseService = Depends(get_service)):
    return svc.create(payload)
