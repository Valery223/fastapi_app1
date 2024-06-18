from fastapi import FastAPI
from contextlib import asynccontextmanager

from api_v1 import router as router_v1
from core.models.db_helper import db_helper
from core.models.base import Base
from core.config import settings

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(router_v1, prefix=settings.api_v1_prefix)

@app.get("/")
def top():
    return "This is top"

@app.get("/echo/{thing}")
def echo(thing):
    return f"echoing {thing}"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)