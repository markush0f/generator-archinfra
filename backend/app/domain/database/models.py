from typing import Optional, List, TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy import Column, Enum as SQLEnum
from app.types.generator_types import DatabaseTypeEnum
from app.domain.architecture.models import ArchitectureDatabaseLink, Architecture

# if TYPE_CHECKING:
#     from app.domain.architecture.models import Architecture, ArchitectureDatabaseLink


class Database(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: DatabaseTypeEnum = Field(
        sa_column=Column(
            SQLEnum(DatabaseTypeEnum), nullable=False, unique=True, index=True
        )
    )
    description: Optional[str] = Field(default=None)
    architectures: List[Architecture] = Relationship(
        back_populates="databases", link_model=ArchitectureDatabaseLink
    )
