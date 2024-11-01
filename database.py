from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

DATABASE_URL = "sqlite+aiosqlite:///./jokes.db"

engine = create_async_engine(
    url=DATABASE_URL,
    echo=True,
)

# Создаём сессию для выполнения операций с базой данных
async_session = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
    autoflush=False,
    autocommit=False,
)

#создать функцию-зависимость, которая будет автоматически открывать и закрывать сессию при каждом запросе
async def get_database_session():
    async with async_session() as session:
        yield session
