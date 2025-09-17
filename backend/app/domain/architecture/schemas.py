from typing import List, Optional
from sqlmodel import SQLModel
from app.types.generator_types import ArchitectureType, DatabaseType


class TagBase(SQLModel):
    name: str


class TagCreate(TagBase):
    pass


class TagRead(TagBase):
    id: int

    class Config:
        from_attributes = True


class DatabaseBase(SQLModel):
    name: DatabaseType
    description: Optional[str] = None


class DatabaseCreate(DatabaseBase):
    pass


class DatabaseRead(DatabaseBase):
    id: int

    class Config:
        from_attributes = True


class ArchitectureBase(SQLModel):
    name: str
    type: ArchitectureType
    description: Optional[str] = None
    path: str


class ArchitectureCreate(ArchitectureBase):
    tag_ids: Optional[List[int]] = []
    database_ids: Optional[List[int]] = []


class ArchitectureRead(ArchitectureBase):
    id: int
    tags: List[TagRead] = []
    databases: List[DatabaseRead] = []

    class Config:
        from_attributes = True


class ArchitecturePage(SQLModel):
    total: int
    items: List[ArchitectureRead]
