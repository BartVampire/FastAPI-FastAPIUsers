from fastapi import APIRouter
from .users import router as users_router
from core.config import settings
from .auth_router import router as auth_router

"""Подключаем модули и регистрируем маршруты в API V1"""

router = APIRouter(prefix=settings.api.v1.prefix)

router.include_router(
    users_router, prefix=settings.api.v1.users
)  # Регистрируем маршруты из модуля users с префиксом /api/v1/users

router.include_router(
    auth_router
)  # Регистрируем маршруты из модуля auth с префиксом /api/v1/auth

