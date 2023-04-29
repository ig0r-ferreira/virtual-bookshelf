from decimal import Decimal

from sqlalchemy import Numeric, String
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    MappedAsDataclass,
    mapped_column,
)


class Base(DeclarativeBase, MappedAsDataclass):
    pass


class Book(Base):
    __tablename__ = 'book'
    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    title: Mapped[str] = mapped_column(String(250), unique=True)
    author: Mapped[str] = mapped_column(String(250))
    rating: Mapped[Decimal] = mapped_column(Numeric(precision=3, scale=1))
