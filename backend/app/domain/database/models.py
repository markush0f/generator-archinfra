from typing import Optional, List, TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship
from app.types.generator_types import DatabaseType

if TYPE_CHECKING:
    from app.domain.architecture.models import Architecture, ArchitectureDatabaseLink


class Database(SQLModel, table=True):
    __tablename__ = "database"
    id: Optional[int] = Field(default=None, primary_key=True)
    name: DatabaseType = Field(index=True, nullable=False, unique=True)
    description: Optional[str] = None

    architectures: List["Architecture"] = Relationship(
        back_populates="databases", link_model="ArchitectureDatabaseLink"
    )
