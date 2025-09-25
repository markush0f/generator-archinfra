from typing import List
from sqlmodel import Session
from .models import Rag
from .repository import RagRepository
from .schemas import RagCreate

class RagService:
    def __init__(self, session: Session):
        self.repo = RagRepository(session)

    def list_with_total(self, offset: int, limit: int) -> tuple[list[Rag], int]:
        items_seq = self.repo.list(offset=offset, limit=limit)
        items: List[Rag] = list(items_seq)
        total = self.repo.count()
        return items, total

    def create(self, data: RagCreate) -> Rag:
        obj = Rag.model_validate(data.model_dump())
        return self.repo.create(obj)
