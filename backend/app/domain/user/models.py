from typing import Optional
from sqlmodel import SQLModel, Field

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(index=True, nullable=False)
    email: str = Field(index=True, nullable=False, unique=True)
    is_active: bool = Field(default=True)
    created_at: Optional[str] = Field(default=None)
