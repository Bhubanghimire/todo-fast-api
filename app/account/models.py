from typing import Optional
from sqlalchemy import Column, Integer, Text, String, Boolean, ForeignKey, LargeBinary
from sqlalchemy.orm import mapped_column, Mapped, relationship

from app.core.database import engine, Base


class Address(Base):
    __tablename__ = "address"
    id: Mapped[int] = mapped_column(primary_key=True)
    email_address: Mapped[str] = mapped_column(String)
    user_id: Mapped[int] = mapped_column(ForeignKey("user_account.id"))
    user: Mapped["User"] = relationship(back_populates="addresses")


class User(Base):
    __tablename__ = "user_account"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=True)
    profile: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String,unique=True)
    password: Mapped[str] = mapped_column(LargeBinary)


