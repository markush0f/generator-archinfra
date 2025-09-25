from typing import Optional
from sqlmodel import SQLModel, Field


class ArchitectureTagLink(SQLModel, table=True):
    architecture_id: Optional[int] = Field(
        default=None, foreign_key="architecture.id", primary_key=True
    )
    tag_id: Optional[int] = Field(
        default=None, foreign_key="tag.id", primary_key=True
    )


class ArchitectureDatabaseLink(SQLModel, table=True):
    architecture_id: Optional[int] = Field(
        default=None, foreign_key="architecture.id", primary_key=True
    )
    database_id: Optional[int] = Field(
        default=None, foreign_key="database.id", primary_key=True
    )
