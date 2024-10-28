from .base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey, func
from datetime import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .user import User
    from .joke import Joke

class Reaction(Base):
    __tablename__ = "reactions"

    type: Mapped[str] = mapped_column(String(15))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    joke_id: Mapped[int] = mapped_column(ForeignKey("jokes.id"))
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())

    user: Mapped["User"] = relationship("User", back_populates="reactions")
    joke: Mapped["Joke"] = relationship("Joke", back_populates="reactions")
