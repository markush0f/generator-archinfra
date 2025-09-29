# app/domain/project/models.py
from typing import Optional, List
from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship


class ProjectDatabaseLink(SQLModel, table=True):
    __tablename__ = "project_database_link"
    project_id: Optional[int] = Field(
        default=None, foreign_key="project.id", primary_key=True
    )
    database_id: Optional[int] = Field(
        default=None, foreign_key="database.id", primary_key=True
    )


class ProjectTagLink(SQLModel, table=True):
    __tablename__ = "project_tag_link"
    project_id: Optional[int] = Field(
        default=None, foreign_key="project.id", primary_key=True
    )
    tag_id: Optional[int] = Field(default=None, foreign_key="tag.id", primary_key=True)


class Project(SQLModel, table=True):
    __tablename__ = "project"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True, nullable=False)
    description: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    updated_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)

    architecture_id: Optional[int] = Field(default=None, foreign_key="architecture.id")
    architecture: Optional["Architecture"] = Relationship(back_populates="projects")

    databases: List["Database"] = Relationship(
        back_populates="projects", link_model=ProjectDatabaseLink
    )

    tags: List["Tag"] = Relationship(
        back_populates="projects", link_model=ProjectTagLink
    )
