from typing import Sequence
from sqlmodel import Session, select
from sqlalchemy import func
from .models import Architecture

class ArchitectureRepository:
    def __init__(self, session: Session):
        self.session = session

    def list(self, offset: int = 0, limit: int = 50) -> Sequence[Architecture]:
        stmt = select(Architecture).offset(offset).limit(limit)
        return self.session.exec(stmt).all()

    def count(self) -> int:
        stmt = select(func.count()).select_from(Architecture)
        return int(self.session.exec(stmt).one())

    def create(self, obj: Architecture) -> Architecture:
        self.session.add(obj)
        self.session.commit()
        self.session.refresh(obj)
        return obj
