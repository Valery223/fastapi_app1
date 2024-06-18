from pydantic import BaseModel, ConfigDict

class ExplorerBase(BaseModel):
    name: str
    country: str
    description: str

# for create data
class ExplorerCreate(ExplorerBase):
    pass

# for return data
class Explorer(ExplorerBase):
    model_config = ConfigDict(from_attributes=True)