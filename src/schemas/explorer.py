from pydantic import BaseModel

class ExplorerBase(BaseModel):
    name: str
    country: str
    description: str

# for create data
class ExplorerCreate(BaseModel):
    pass

# for return data
class Explorer(ExplorerBase):
    class Config:
        orm_mode = True