from typing import Optional, List
from sqlmodel import SQLModel

class RagBase(SQLModel):
    pass  # añade campos compartidos aquí

class RagCreate(RagBase):
    pass  # campos requeridos para crear

class RagRead(RagBase):
    id: int

class RagPage(SQLModel):
    total: int
    items: List[RagRead]
