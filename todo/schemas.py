from pydantic import BaseModel

class TodoSchamas(BaseModel):
    id : int
    text : str
    is_done : bool

    class Config:
        orm_model =True