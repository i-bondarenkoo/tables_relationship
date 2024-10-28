from .base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, func
from datetime import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .joke import Joke
    from .reaction import Reaction

class User(Base):
    __tablename__ = "users"

    username: Mapped[str] = mapped_column(String(30), unique=True)
    email: Mapped[str] = mapped_column(String(25), unique=True)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())

    jokes: Mapped[list["Joke"]] = relationship("Joke", back_populates="user")
    reactions: Mapped[list["Reaction"]] = relationship("Reaction", back_populates="user")
