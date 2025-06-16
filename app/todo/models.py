from sqlalchemy import Column, Integer, Text, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import engine, Base


class TODO(Base):
    __tablename__ = "todos"
    # __table_args__ = {'extend_existing': True}

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    text: Mapped[str] = mapped_column(String)
    is_done: Mapped[bool] = mapped_column(Boolean)
