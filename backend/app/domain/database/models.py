# app/domain/database/models.py
from typing import Optional
from sqlmodel import SQLModel, Field, Relationship, Column, Enum as SQLEnum
from app.types.generator_types import DatabaseTypeEnum
from app.domain.links import ArchitectureDatabaseLink
from app.domain.project.models import (
    ProjectDatabaseLink,
)  # 👈 importar el link correcto


class Database(SQLModel, table=True):
    __tablename__ = "database"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: DatabaseTypeEnum = Field(
        sa_column=Column(
            SQLEnum(DatabaseTypeEnum), nullable=False, unique=True, index=True
        )
    )
    description: Optional[str] = None

    architectures: list["Architecture"] = Relationship(
        back_populates="databases",
        link_model=ArchitectureDatabaseLink,
    )

    projects: list["Project"] = Relationship(
        back_populates="databases", link_model=ProjectDatabaseLink
    )
