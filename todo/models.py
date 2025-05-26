from sqlalchemy import Column, Integer, Text, String, Boolean
from database import engine, Base


class TODO(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True)
    text = Column(String)
    is_done = Column(Boolean)


Base.metadata.create_all(engine)
