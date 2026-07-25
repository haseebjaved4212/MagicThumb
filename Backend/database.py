from sqlmodel import create_engine, SQLModel, Session
from config import DATABASE_URL

DATABASE_URL = "postgresql://postgres:123456@localhost:5432/Thambnail_Gen"

engine = create_engine(DATABASE_URL, echo=False , connect_args={"check_same_thread": False})

def create_tables():
    SQLModel.metadata.create_all(engine)    

def get_session():
    with Session(engine) as session:
        yield session    