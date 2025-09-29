from typing import Optional, List
from sqlmodel import SQLModel

class TagBase(SQLModel):
    name: str

class TagCreate(TagBase):
    pass


class TagRead(TagBase):
    id: int

    class Config:
        from_attributes = True

class TagPage(SQLModel):
    total: int
    items: List[TagRead]
