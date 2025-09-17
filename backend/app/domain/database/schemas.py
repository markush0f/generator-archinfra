from __future__ import annotations
from typing import Optional, List
from app.types.generator_types import DatabaseType
from sqlmodel import SQLModel

class DatabaseBase(SQLModel):
    name: DatabaseType
    description: Optional[str] = None


class DatabaseCreate(DatabaseBase):
    pass


class DatabaseRead(DatabaseBase):
    id: int

    class Config:
        from_attributes = True


class DatabasePage(SQLModel):
    total: int
    items: List[DatabaseRead]
