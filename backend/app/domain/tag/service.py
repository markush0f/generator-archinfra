from typing import List
from sqlmodel import Session
from .models import Tag
from .repository import TagRepository
from .schemas import TagCreate

class TagService:
    def __init__(self, session: Session):
        self.repo = TagRepository(session)

    def list_with_total(self, offset: int, limit: int) -> tuple[list[Tag], int]:
        items_seq = self.repo.list(offset=offset, limit=limit)
        items: List[Tag] = list(items_seq)
        total = self.repo.count()
        return items, total

    def create(self, data: TagCreate) -> Tag:
        obj = Tag.model_validate(data.model_dump())
        return self.repo.create(obj)
