from contextlib import asynccontextmanager

from fastapi import FastAPI
from shared.database.async_manager import db_manager


@asynccontextmanager
async def lifespan(app: FastAPI):
    await db_manager.init_pool()
    yield
    await db_manager.close_pool()


app = FastAPI(lifespan=lifespan)
