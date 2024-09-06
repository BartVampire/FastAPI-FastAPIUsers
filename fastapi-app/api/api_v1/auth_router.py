from fastapi import APIRouter

from core.config import settings

router = APIRouter(
    prefix=settings.api.v1.auth,  # Префикс для маршрутов авторизации /api/v1/auth
    tags=["Auth"],  # Тег для маршрутизатора API Auth
)
