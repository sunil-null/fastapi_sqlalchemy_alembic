from pydantic import BaseModel


class User(BaseModel):
    first_name: str
    last_name: str = None
    age: int
    city: str = None

    class Config:
        orm_mode = True
