from pydantic import BaseModel, ConfigDict, Field


class UserCreateRequest(BaseModel):
    user_id: int
    name: str
    age: int
    height: float
    date: str


class FakerRequest(BaseModel):
    count: int
