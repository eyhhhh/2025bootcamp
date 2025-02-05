from sqlmodel import (Field, SQLModel,Session, create_engine, select)

db_url = 'sqlite:///blog.db'
db_engine = create_engine(db_url, connect_args={"check_same_thread": False})

def get_db_session():
  with Session(db_engine) as session:
    yield session
  
def create_db():
  SQLModel.metadata.create_all(db_engine)

