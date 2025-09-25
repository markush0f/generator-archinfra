from typing import List
from sqlmodel import Session
from .models import Project
from .repository import ProjectRepository
from .schemas import ProjectCreate

class ProjectService:
    def __init__(self, session: Session):
        self.repo = ProjectRepository(session)

    def list_with_total(self, offset: int, limit: int) -> tuple[list[Project], int]:
        items_seq = self.repo.list(offset=offset, limit=limit)
        items: List[Project] = list(items_seq)
        total = self.repo.count()
        return items, total

    def create(self, data: ProjectCreate) -> Project:
        obj = Project.model_validate(data.model_dump())
        return self.repo.create(obj)
