from .base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .joke import Joke

class Category(Base):
    __tablename__ = "categories"

    name: Mapped[str] = mapped_column(String(30), unique=True)
    description: Mapped[str | None] = mapped_column(String(70), nullable=False)

    jokes: Mapped[list["Joke"]] = relationship("Joke", back_populates="category")
