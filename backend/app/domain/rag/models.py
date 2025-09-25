from typing import Optional
from sqlmodel import SQLModel, Field

class Rag(SQLModel, table=True):
    __tablename__ = "rag"
    id: Optional[int] = Field(default=None, primary_key=True)
