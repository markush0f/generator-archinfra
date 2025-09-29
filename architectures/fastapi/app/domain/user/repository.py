from typing import Sequence
from sqlmodel import Session, select
from sqlmodel import func
from .models import User

class UserRepository:
    def __init__(self, session: Session):
        self.session = session

    def list(self, offset: int = 0, limit: int = 50) -> Sequence[User]:
        stmt = select(User).offset(offset).limit(limit)
        return self.session.exec(stmt).all()

    def count(self) -> int:
        stmt = select(func.count()).select_from(User)
        return int(self.session.exec(stmt).one())

    def create(self, obj: User) -> User:
        self.session.add(obj)
        self.session.commit()
        self.session.refresh(obj)
        return obj
