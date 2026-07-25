from sqlmodel import create_engine, SQLModel, Session
from config import DATABASE_URL

DATABASE_URL = "postgresql://postgres:123456@localhost:5432/Thambnail_Gen"

engine = create_engine(DATABASE_URL, echo=True)

def create_db_and_table():
    SQLModel.metadata.create_all(engine)    