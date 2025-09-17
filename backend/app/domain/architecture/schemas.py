from typing import List, Optional
from app.domain.database.schemas import DatabaseRead
from app.domain.tag.schemas import TagRead
from sqlmodel import SQLModel
from app.types.generator_types import ArchitectureType

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
