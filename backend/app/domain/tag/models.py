from typing import Optional
from sqlmodel import SQLModel, Field, Relationship, Column, String
from app.domain.links import ArchitectureTagLink


class Tag(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(sa_column=Column(String, nullable=False, unique=True, index=True))

    architectures: list["Architecture"] = Relationship(
        back_populates="tags",
        link_model=ArchitectureTagLink,
    )
