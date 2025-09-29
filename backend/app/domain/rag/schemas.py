from typing import Optional
from datetime import datetime
from sqlmodel import SQLModel

class DocumentBase(SQLModel):
    project: str
    content: str
    source: str
    pass


class DocumentCreate(DocumentBase):
    content: str


class DocumentRead(DocumentBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
