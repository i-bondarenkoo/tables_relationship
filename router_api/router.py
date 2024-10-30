from fastapi import APIRouter
import crud
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from schemas import UserCreate
from database import get_database_session
router = APIRouter()


@router.get("/users/{user_id}/")
async def get_user_by_id(user_id: int, session: AsyncSession = Depends(get_database_session)):
    return await crud.get_user_by_id(user_id, session)


@router.post("/users/")
async def create_user(user_in: UserCreate, session: AsyncSession = Depends(get_database_session)):
    return await crud.create_user(user_in, session)