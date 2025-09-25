from typing import Optional
from sqlmodel import SQLModel, Field

class Project(SQLModel, table=True):
    __tablename__ = "project"
    id: Optional[int] = Field(default=None, primary_key=True)
