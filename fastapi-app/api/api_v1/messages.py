from typing import Annotated

from fastapi import APIRouter, Depends

from api.dependencies.authentication.fastapii_user_dispatcher import (
    current_user_route,
    current_superuser_route,
)
from core.models import User
from core.config import settings
from core.schemas.user_schema import UserRead

router = APIRouter(
    prefix=settings.api.v1.messages,
    tags=["Messages"],  # Создание маршрутизатора API с тегом "Messages"
)


@router.get("")
def get_user_messages(
    user: Annotated[
        "User", Depends(current_user_route)
    ],  # Получение текущего пользователя из зависимости
):
    return {
        "messages": ["Hello, world!", "This is a test message."],
        "user": UserRead.model_validate(user),
    }


@router.get("/secrets")
def get_superuser_messages(
    user: Annotated[
        "User", Depends(current_superuser_route)
    ],  # Получение текущего пользователя из зависимости для суперпользователей
):
    return {
        "messages": ["Hello, world!", "This is secret message."],
        "user": UserRead.model_validate(user),
    }
