from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship, Column, String
from sqlalchemy.orm import Mapped
from app.domain.architecture.models import Architecture, ArchitectureTagLink


class Tag(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(sa_column=Column(String, nullable=False, unique=True, index=True))

    architectures: Mapped[List[Architecture]] = Relationship(
        back_populates="tags", link_model=ArchitectureTagLink
    )
