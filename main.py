from fastapi import FastAPI
from database import engine, async_session
import uvicorn
from models.base import Base
from contextlib import asynccontextmanager

from router_api.router import router as router_v1


    
@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)  # Создаём таблицы при запуске
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(router=router_v1)



if __name__ == "__main__":
    uvicorn.run(
        "main:app", 
        reload=True,
        )


