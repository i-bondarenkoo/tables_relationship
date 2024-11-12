from fastapi import FastAPI
from database import engine, async_session
import uvicorn
from models.base import Base
from contextlib import asynccontextmanager

from router_api.router_user import router as router_user
from router_api.router_category import router as router_category
from router_api.router_joke import router as router_joke
from router_api.router_reaction import router as router_reaction    
@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)  # Создаём таблицы при запуске
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(router=router_user)
app.include_router(router=router_category)
app.include_router(router=router_joke)
app.include_router(router=router_reaction)



if __name__ == "__main__":
    uvicorn.run(
        "main:app", 
        reload=True,
        )


