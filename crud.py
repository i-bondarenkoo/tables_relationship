from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends 
from database import get_database_session
from sqlalchemy import select
from schemas import  UserCreate
from models.user import User

async def get_user_by_id(user_id: int, session: AsyncSession = Depends(get_database_session)):
    stmt = select(User).where(User.id == user_id)
    result = await session.execute(stmt)
    user = result.scalar_one_or_none()
    return user


async def get_all_users(session: AsyncSession = Depends(get_database_session)) -> list[User]:
    stmt = select(User).order_by(User.id)
    result = await session.execute(stmt)
    users_all = result.scalars().all()
    return list(users_all)


async def create_user(user_in: UserCreate, session: AsyncSession = Depends(get_database_session)) -> User:
    user = User(
        username=user_in.username,
        email=user_in.email,
    )
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user
        