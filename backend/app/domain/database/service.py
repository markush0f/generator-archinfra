from typing import List
from sqlmodel import Session
from .models import Database
from .repository import DatabaseRepository
from .schemas import DatabaseCreate

class DatabaseService:
    def __init__(self, session: Session):
        self.repo = DatabaseRepository(session)

    def list_with_total(self, offset: int, limit: int) -> tuple[list[Database], int]:
        items_seq = self.repo.list(offset=offset, limit=limit)
        items: List[Database] = list(items_seq)
        total = self.repo.count()
        return items, total

    def create(self, data: DatabaseCreate) -> Database:
        obj = Database.model_validate(data.model_dump())
        return self.repo.create(obj)
    