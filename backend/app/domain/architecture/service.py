
from typing import List, Optional, Any
from sqlmodel import Session
from .models import Architecture
from .repository import ArchitectureRepository
from .schemas import ArchitectureCreate, ArchitectureUpdate

class ArchitectureService:
    def __init__(self, session: Session):
        self.repo = ArchitectureRepository(session)

    def list_with_total(
        self, offset: int, limit: int, filters: dict[str, Any] | None = None
    ) -> tuple[list[Architecture], int]:
        items_seq = self.repo.list_with_filters(offset=offset, limit=limit, filters=filters)
        items: List[Architecture] = list(items_seq)
        total = self.repo.count()
        return items, total

    def get(self, id: int) -> Optional[Architecture]:
        return self.repo.get(id)

    def create(self, data: ArchitectureCreate) -> Architecture:
        obj = Architecture.model_validate(data.model_dump())
        return self.repo.create(obj)

    def update(self, id: int, data: ArchitectureUpdate) -> Optional[Architecture]:
        obj = self.repo.get(id)
        if not obj:
            return None
        return self.repo.update(obj, data.model_dump(exclude_unset=True))

    def delete(self, id: int) -> bool:
        obj = self.repo.get(id)
        if not obj:
            return False
        self.repo.delete(obj)
        return True
