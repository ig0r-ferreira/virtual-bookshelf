from sqlalchemy import Float, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Book(Base):
    __tablename__ = 'book'
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True)
    author: Mapped[str] = mapped_column(String(250))
    rating: Mapped[float] = mapped_column(Float(precision=1))
