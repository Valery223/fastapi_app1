from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from schemas.creature import Creature as CreatureSchema

# import fake.creature as service
import service.creature as service
from db.db_helper import db_helper

router = APIRouter(prefix="/creature")

# @router.get("/")
# def get_all() -> list[Creature]:
#     return service.get_all()

@router.get("/{name}", response_model=CreatureSchema)
async def get_one(name, db: AsyncSession = Depends(db_helper.get_db) ) -> CreatureSchema | None:
    return await service.get_one(db, name)

# @router.post("/")
# def create(creature: Creature) -> Creature:
#     return service.create_explorer(creature)

# @router.patch("/")
# def modify(creature: Creature) -> Creature:
#     return service.modify(creature)

# @router.put("/")
# def replace(creature: Creature) -> Creature:
#     return service.replace(creature)

# @router.delete("/{name}")
# def delete(name: str):
#     return service.delete(name)