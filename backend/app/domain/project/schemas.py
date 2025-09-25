from typing import Optional, List
from sqlmodel import SQLModel

class ProjectBase(SQLModel):
    pass  # añade campos compartidos aquí

class ProjectCreate(ProjectBase):
    pass  # campos requeridos para crear

class ProjectRead(ProjectBase):
    id: int

class ProjectPage(SQLModel):
    total: int
    items: List[ProjectRead]
