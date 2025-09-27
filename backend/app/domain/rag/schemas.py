from typing import Optional
from datetime import datetime
from sqlmodel import SQLModel

class DocumentBase(SQLModel):
    project: str
    content: str
    source: str
    pass


class DocumentCreate(DocumentBase):
    project: str
    content: str
    source: Optional[str] = None


class DocumentRead(DocumentBase):
    id: int
    project: str
    content: str
    source: Optional[str] = None
    created_at: datetime

    class Config:
        from_attributes = True
