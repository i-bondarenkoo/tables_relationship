from fastapi import APIRouter
import crud
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from schemas import UserCreate
from schemas.user import UserResponse

from database import get_database_session


router = APIRouter(
    tags=["users"],
    prefix="/users"
    )


@router.get("/{user_id}")
async def get_user_by_id(user_id: int, session: AsyncSession = Depends(get_database_session)):
    return await crud.get_user_by_id(user_id, session)


@router.get("/")
async def get_all_users(session: AsyncSession = Depends(get_database_session)) -> list[UserResponse]:
    return await crud.get_all_users(session)


@router.post("/")
async def create_user(user_in: UserCreate, session: AsyncSession = Depends(get_database_session)):
    return await crud.create_user(user_in, session)


