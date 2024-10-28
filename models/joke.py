from .base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey, func
from datetime import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .user import User
    from .category import Category
    from .reaction import Reaction

class Joke(Base):
    __tablename__ = "jokes"

    content: Mapped[str] = mapped_column(String(250))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())

    user: Mapped["User"] = relationship("User", back_populates="jokes")
    category: Mapped["Category"] = relationship("Category", back_populates="jokes")
    reactions: Mapped[list["Reaction"]] = relationship("Reaction", back_populates="joke")
