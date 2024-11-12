from fastapi import APIRouter
import crud
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from database import get_database_session
from schemas import CreateReaction
router = APIRouter(
    tags=["reactions"],
    prefix="/reactions",
    )


@router.get("/")
async def get_reactions_all(session: AsyncSession = Depends(get_database_session)):
    return await crud.get_reactions_all(session)


@router.get("/{reaction_id}")
async def get_reaction_by_id(reaction_id: int, session: AsyncSession = Depends(get_database_session)):
    return await crud.get_reaction_by_id(reaction_id, session)


@router.post("/")
async def create_reaction(data_in: CreateReaction, session: AsyncSession = Depends(get_database_session)):
    return await crud.create_reaction(data_in, session)