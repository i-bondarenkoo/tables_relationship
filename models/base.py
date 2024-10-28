from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

# Базовый класс для всех моделей
class Base(DeclarativeBase):
    __abstract__ = True
    id: Mapped[int] = mapped_column(primary_key=True)
