from fastapi import APIRouter
from schemas.category import CategoryCreate
import crud
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from database import get_database_session

router = APIRouter(
    tags=["category"],
    prefix="/category",
    )


@router.post("/")
async def create_category(data_in: CategoryCreate, session: AsyncSession = Depends(get_database_session)):
    return await crud.create_category(data_in, session)


@router.get("/{category_id}")
async def get_categories_all(category_id: int, session: AsyncSession = Depends(get_database_session)):
    return await crud.get_categories_by_id(category_id, session)


@router.get("/")
async def get_categories_all(session: AsyncSession = Depends(get_database_session)):
    return await crud.get_categories_all(session)