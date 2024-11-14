from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends 
from database import get_database_session
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from schemas import  UserCreate
from models.user import User
from models.joke import Joke
from models.category import Category
from models.reaction import Reaction
from schemas import CategoryCreate
from schemas import JokeCreate
from fastapi import HTTPException


async def get_user_by_id(user_id: int, session: AsyncSession = Depends(get_database_session)):
    stmt = select(User).where(User.id == user_id)
    result = await session.execute(stmt)
    user = result.scalar_one_or_none()
    if user is None:
        raise HTTPException(
            status_code=404,
            detail="Пользователь не найден",
        )
    return user


async def get_all_users(session: AsyncSession = Depends(get_database_session)) -> list[User]:
    stmt = select(User).order_by(User.id)
    result = await session.execute(stmt)
    users_all = result.scalars().all()
    if users_all is None:
        raise HTTPException(
            status_code=404,
            detail="Список пользователей пустой",
        )
    return list(users_all)


async def create_user(user_in: UserCreate, session: AsyncSession = Depends(get_database_session)) -> User:
    user = User(
        username=user_in.username,
        email=user_in.email,
    )
    session.add(user)
    await session.commit()
    await session.refresh(user)
    if user is None:
        raise HTTPException(
            status_code=404,
            detail="Данный пользователь не найден",
        )
    return user

async def create_category(data_in: CategoryCreate, session: AsyncSession = Depends(get_database_session)):
    data = Category(
        name=data_in.name,
        description=data_in.description,
    )
    session.add(data)
    await session.commit()
    await session.refresh(data)
    if data is None:
        raise HTTPException(
            status_code=404,
            detail="Категория не создана",
        )
    return data
        
        
async def get_categories_all(session: AsyncSession = Depends(get_database_session)):
    stmt = select(Category).order_by(Category.id)
    result = await session.execute(stmt)
    categories_all = result.scalars().all()
    if categories_all is None:
        raise HTTPException(
            status_code=404,
            detail="Список категорий пустой",
            
        )
    return list(categories_all)     

async def get_categories_by_id(category_id: int, session: AsyncSession = Depends(get_database_session)):
    stmt = select(Category).where(Category.id == category_id)
    result = await session.execute(stmt)
    response = result.scalar_one_or_none()
    if response is None:
        raise HTTPException(
            status_code=404,
            detail="Категория не найдена",
        )
    return response


async def create_joke(data_in: JokeCreate, session: AsyncSession = Depends(get_database_session)):
    joke = Joke(
        content=data_in.content,
        user_id=data_in.user_id,
        category_id=data_in.category_id,
        
    )
    session.add(joke)
    await session.commit()
    await session.refresh(joke)
    if joke is None:
        raise HTTPException(
            status_code=404,
            detail="Шутка не создана",
        )
    return joke


async def get_jokes_all(session: AsyncSession = Depends(get_database_session)):
    stmt = select(Joke).order_by(Joke.id)
    result = await session.execute(stmt)
    response = result.scalars().all()
    if response is None:
        raise HTTPException(
            status_code=404,
            detail="Ни одной шутки не найдено",
        )
    return list(response)

async def get_jokes_by_id(joke_id: int, session: AsyncSession = Depends(get_database_session)):
    stmt = select(Joke).where(Joke.id == joke_id)
    result = await session.execute(stmt)
    response = result.scalar_one_or_none()
    if response is None:
        raise HTTPException(
            status_code=404,
            detail="Шутка не найдена",
        )
    return response


async def create_reaction(data_in: Reaction, session: AsyncSession = Depends(get_database_session)):
    reaction = Reaction(
        type=data_in.type,
        user_id=data_in.user_id,
        joke_id=data_in.joke_id,
    )
    session.add(reaction)
    await session.commit()
    await session.refresh(reaction)
    if reaction is None:
        raise HTTPException(
            status_code=404,
            detail="Реакция не создана",
        )
    return reaction


async def get_reaction_by_id(reaction_id: int, session: AsyncSession = Depends(get_database_session)):
    stmt = select(Reaction).where(Reaction.id == reaction_id)
    result = await session.execute(stmt)
    response = result.scalar_one_or_none()
    if response is None:
        raise HTTPException(
            status_code=404,
            detail="Реация отсутствует",
        )
    return response


async def get_reactions_all(session: AsyncSession = Depends(get_database_session)):
    stmt = select(Reaction).order_by(Reaction.id)
    result = await session.execute(stmt)
    response = result.scalars().all()
    if response is None:
        raise HTTPException(
            status_code=404,
            detail="Список реакций пустой",
        )
    return list(response)


async def get_user_jokes_in_category(
    user_id: int, 
    category_id: int,
    session: AsyncSession = Depends(get_database_session)
    ):
    stmt = (
        select(
            Joke.id,
            Joke.content,
            Joke.created_at,
            User.username.label("user_name"),
            Category.name.label("category_name")
        )
        .join(User, Joke.user_id == User.id)
        .join(Category, Joke.category_id == Category.id)
        .where(Joke.user_id == user_id, Joke.category_id == category_id)
        .order_by(Joke.id)
    )
    result = await session.execute(stmt)
    jokes = result.all()
    
    if not jokes:
        raise HTTPException(
            status_code=404,
            detail="У данного пользователя нет шуток в выбранной категории"
        )
    
    return [
        {
            "id": joke.id,
            "content": joke.content,
            "created_at": joke.created_at,
            "user_name": joke.user_name,
            "category_name": joke.category_name
        }
        for joke in jokes
    ]