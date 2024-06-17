from pydantic import BaseModel

class CreatureBase(BaseModel):
    name: str
    country: str
    area: str
    description: str
    aka: str

class Creature(CreatureBase):
    class Config:
        orm_mode = True