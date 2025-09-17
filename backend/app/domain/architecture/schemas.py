from __future__ import annotations
from typing import Optional, List
from sqlmodel import SQLModel

class ArchitectureBase(SQLModel):
    pass  # añade campos compartidos aquí

class ArchitectureCreate(ArchitectureBase):
    pass  # campos requeridos para crear

class ArchitectureRead(ArchitectureBase):
    id: int

class ArchitecturePage(SQLModel):
    total: int
    items: List[ArchitectureRead]
