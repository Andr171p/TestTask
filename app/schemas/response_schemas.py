from typing import Literal

from pydantic import BaseModel, ConfigDict


class UserResponse(BaseModel):
    id: int
    user_id: int
    name: str
    age: int
    height: float
    date: float

    model_config = ConfigDict(from_attributes=True)


class APIUserResponse(BaseModel):
    status: Literal['ok'] = 'ok'
    data: UserResponse


class APIUserListResponse(BaseModel):
    status: Literal['ok'] = 'ok'
    data: list[UserResponse]
