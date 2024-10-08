from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from database.orm_manager import orm_manager

from app.schemas.request_schemas import (
    UserCreateRequest,
    FakerRequest
)
from app.schemas.response_schemas import (
    UserResponse,
    APIUserResponse,
    APIUserListResponse
)

from faker import Faker
import random
from misc.utils import str_to_timestamp


router = APIRouter()


@router.get("/")
async def get_hello_world() -> JSONResponse:
    return JSONResponse(
        content={
            "status": "ok",
            "data": "Hello world!"
        },
    )


@router.get("/get_user/{user_id}/", response_model=APIUserResponse)
async def get_user(user_id: int) -> JSONResponse:
    user = await orm_manager.get_user(user_id=user_id)
    if not user:
        return JSONResponse(
            content={"status": "error", "message": "User not found"},
            status_code=status.HTTP_404_NOT_FOUND,
        )
    response_model = UserResponse.model_validate(user)
    return JSONResponse(
        content={
            "status": "ok",
            "data": response_model.model_dump(),
        }
    )


@router.get("/users/", response_model=APIUserListResponse)
async def get_users() -> JSONResponse:
    users = await orm_manager.get_users()
    response_data = [
        UserResponse.model_validate(user).model_dump() for user in users
    ]
    return JSONResponse(
        content={
            "status": "ok",
            "data": response_data,
        }
    )


@router.post("/user/", response_model=APIUserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(user_data: UserCreateRequest) -> JSONResponse:
    user_candidate = await orm_manager.create_user(
        user_id=user_data.user_id,
        name=user_data.name,
        age=user_data.age,
        height=user_data.height,
        date=user_data.date
    )
    response_model = UserResponse.model_validate(user_candidate)
    return JSONResponse(
        content={
            "status": "ok",
            "data": response_model.model_dump(),
        },
        status_code=status.HTTP_201_CREATED,
    )
