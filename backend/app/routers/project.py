from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.core.db import get_session
from app.domain.project.service import ProjectService
from app.domain.project.schemas import ProjectCreate, ProjectRead, ProjectPage

router = APIRouter(prefix="/project", tags=["project"])

def get_service(session: Session = Depends(get_session)) -> ProjectService:
    return ProjectService(session)

@router.get("", response_model=ProjectPage)
def list_project(offset: int = 0, limit: int = 50, svc: ProjectService = Depends(get_service)):
    items, total = svc.list_with_total(offset=offset, limit=limit)
    return ProjectPage(total=total, items=items)

@router.post("", response_model=ProjectRead)
def create_project(payload: ProjectCreate, svc: ProjectService = Depends(get_service)):
    return svc.create(payload)
