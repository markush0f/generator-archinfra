from typing import  Optional
from sqlmodel import SQLModel, Field, Relationship, Column, String
from app.types.generator_types import ArchitectureTypeEnum
from app.domain.links import ArchitectureTagLink, ArchitectureDatabaseLink


class Architecture(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(sa_column=Column(String, nullable=False, unique=True, index=True))
    type: str = Field(sa_column=Column(String, nullable=False, index=True)) 
    description: Optional[str] = None
    path: str = Field(sa_column=Column(String, nullable=False, unique=True, index=True))

    tags: list["Tag"] = Relationship(
        back_populates="architectures",
        link_model=ArchitectureTagLink,
    )

    databases: list["Database"] = Relationship(
        back_populates="architectures",
        link_model=ArchitectureDatabaseLink,
    )

    projects: list["Project"] = Relationship(
        back_populates="architecture"
    )
