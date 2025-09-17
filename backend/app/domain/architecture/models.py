from __future__ import annotations
from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship
from app.types.generator_types import ArchitectureType, DatabaseType


class ArchitectureTagLink(SQLModel, table=True):
    __tablename__ = "architecture_tag_link"
    architecture_id: Optional[int] = Field(
        default=None, foreign_key="architecture.id", primary_key=True
    )
    tag_id: Optional[int] = Field(
        default=None, foreign_key="tag.id", primary_key=True
    )

class ArchitectureDatabaseLink(SQLModel, table=True):
    __tablename__ = "architecture_database_link"
    architecture_id: Optional[int] = Field(
        default=None, foreign_key="architecture.id", primary_key=True
    )
    database_id: Optional[int] = Field(
        default=None, foreign_key="database.id", primary_key=True
    )

class Tag(SQLModel, table=True):
    __tablename__ = "tag"
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True, nullable=False, unique=True)

    architectures: List["Architecture"] = Relationship(
        back_populates="tags", link_model=ArchitectureTagLink
    )

class Database(SQLModel, table=True):
    __tablename__ = "database"
    id: Optional[int] = Field(default=None, primary_key=True)
    name: DatabaseType = Field(index=True, nullable=False, unique=True)
    description: Optional[str] = Field(default=None)

    architectures: List["Architecture"] = Relationship(
        back_populates="databases", link_model=ArchitectureDatabaseLink
    )

class Architecture(SQLModel, table=True):
    __tablename__ = "architecture"
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True, nullable=False, unique=True)
    type: ArchitectureType = Field(index=True, nullable=False)
    description: Optional[str] = Field(default=None)
    path: str = Field(index=True, nullable=False, unique=True)

    tags: List[Tag] = Relationship(
        back_populates="architectures", link_model=ArchitectureTagLink
    )
    databases: List[Database] = Relationship(
        back_populates="architectures", link_model=ArchitectureDatabaseLink
    )
