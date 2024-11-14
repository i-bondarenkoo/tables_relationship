from fastapi import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
import crud
from database import get_database_session
from schemas import JokeCreate


router = APIRouter(
    tags=["jokes"],
    prefix="/jokes",
    )

@router.get("/{joke_id}")
async def get_jokes_by_id(joke_id: int, session: AsyncSession = Depends(get_database_session)):
    return await crud.get_jokes_by_id(joke_id, session)


@router.get("/")
async def get_jokes_all(session: AsyncSession = Depends(get_database_session)):
    return await crud.get_jokes_all(session)


@router.post("/")
async def create_joke(data_in: JokeCreate, session: AsyncSession = Depends(get_database_session)):
    return await crud.create_joke(data_in, session)


@router.get("/user/{user_id}/category/{category_id}")
async def get_user_jokes_in_category(
    user_id: int,
    category_id: int,
    session: AsyncSession = Depends(get_database_session)
):
    return await crud.get_user_jokes_in_category(user_id, category_id, session)