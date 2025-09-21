from typing import Generator
from sqlmodel import create_engine, Session
from app.core.config import DATABASE_URL

if DATABASE_URL is None:
    raise ValueError("DATABASE_URL must be set and not None.")

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    echo=False,
)


def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session
