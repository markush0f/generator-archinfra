from __future__ import annotations
from typing import Optional, List, TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy import Column, String, Enum as SQLEnum
from app.types.generator_types import ArchitectureTypeEnum

if TYPE_CHECKING:
    from app.domain.tag.models import Tag
    from app.domain.database.models import Database

class ArchitectureTagLink(SQLModel, table=True):
    architecture_id: Optional[int] = Field(default=None, foreign_key="architecture.id", primary_key=True)
    tag_id: Optional[int] = Field(default=None, foreign_key="tag.id", primary_key=True)

class ArchitectureDatabaseLink(SQLModel, table=True):
    architecture_id: Optional[int] = Field(default=None, foreign_key="architecture.id", primary_key=True)
    database_id: Optional[int] = Field(default=None, foreign_key="database.id", primary_key=True)

class Architecture(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(sa_column=Column(String, nullable=False, unique=True, index=True))
    type: ArchitectureTypeEnum = Field(
        sa_column=Column(SQLEnum(ArchitectureTypeEnum), nullable=False, index=True)
    )
    description: Optional[str] = Field(default=None)
    path: str = Field(sa_column=Column(String, nullable=False, unique=True, index=True))

    tags: List["Tag"] = Relationship(
        back_populates="architectures",
        link_model=ArchitectureTagLink
    )
    databases: List["Database"] = Relationship(
        back_populates="architectures",
        link_model=ArchitectureDatabaseLink
    )
