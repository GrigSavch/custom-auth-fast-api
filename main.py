from fastapi import FastAPI
from app.api import auth, mock
from app.models.base import Base

from database import engine

app = FastAPI()


@app.post("/startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.post("/setup")
async def setup_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)



app.include_router(auth.router)
app.include_router(mock.router)