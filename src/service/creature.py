from sqlalchemy.ext.asyncio import AsyncSession

from models.creature import Creature as CreatureModel
# from fake import creature as data
# from 


# def get_all(session: AsyncSession) -> list[Creature]

# def get_all() -> list[Creature]:
    # return data.get_all()
# 

async def get_one(db: AsyncSession, name: str)-> CreatureModel:
    return await db.get(CreatureModel, name)

# def get_one(name) -> Creature:
#     return data.get_one(name)

# def create(creature: Creature) -> Creature:
#     return data.create(creature)

# def modify(name: str, creature: Creature) -> Creature:
#     return data.modify(name, creature)

# def delete(name: str) -> None:
#     return data.delete(name)