from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class Document(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    project: str
    content: str
    source: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
