from sqlmodel import create_engine, SQLModel

DATABASE_URL = "sqlite:///./users.db"
engine = create_engine(DATABASE_URL, echo=True)

def init_db():
    SQLModel.metadata.create_all(engine)
