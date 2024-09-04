import uvicorn

from fastapi import FastAPI

import contextlib
from typing import AsyncIterator

from database.db import db_manager
from app import api
from app.config import network


@contextlib.asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    db_manager.init()
    yield
    await db_manager.close()


app = FastAPI(
    title="Test task API",
    lifespan=lifespan
)
app.include_router(
    api.router,
    prefix="/api/users",
    tags=["TestTask"]
)


if __name__ == "__main__":
    uvicorn.run(
        app=app,
        host=network.host,
        port=network.port
    )