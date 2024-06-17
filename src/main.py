from fastapi import FastAPI
from contextlib import asynccontextmanager

from api_v1 import explorer, creature
from db.db_helper import db_helper
from db.base import Base

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(explorer.router)
app.include_router(creature.router)

@app.get("/")
def top():
    return "This is top"

@app.get("/echo/{thing}")
def echo(thing):
    return f"echoing {thing}"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)