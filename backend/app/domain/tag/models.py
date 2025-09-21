from typing import TYPE_CHECKING, Optional, List
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from app.domain.architecture.models import Architecture, ArchitectureTagLink


class Tag(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True, nullable=False, unique=True)
    architectures: List["Architecture"] = Relationship(
        back_populates="tags", link_model="ArchitectureTagLink"
    )
