from sqlmodel import SQLModel, create_engine, Session
import os

DB_FILE = os.getenv("SQLITE_FILE", "{{db_name}}.db")
DATABASE_URL = f"sqlite:///{DB_FILE}"

engine = create_engine(DATABASE_URL, echo=True)

def init_db():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
