from typing import List
from sqlmodel import Session
from .models import Architecture
from .repository import ArchitectureRepository
from .schemas import ArchitectureCreate

class ArchitectureService:
    def __init__(self, session: Session):
        self.repo = ArchitectureRepository(session)

    def list_with_total(self, offset: int, limit: int) -> tuple[list[Architecture], int]:
        items_seq = self.repo.list(offset=offset, limit=limit)
        items: List[Architecture] = list(items_seq)
        total = self.repo.count()
        return items, total

    def create(self, data: ArchitectureCreate) -> Architecture:
        # CORREGIDO: convertir schema a dict
        obj = Architecture.model_validate(data.model_dump())
        return self.repo.create(obj)
