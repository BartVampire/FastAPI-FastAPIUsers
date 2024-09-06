from fastapi import APIRouter
from api.dependencies.authentication.fastapii_user_dispatcher import fastapi_users
from core.schemas.user_schema import UserRead, UserUpdate

router = APIRouter(tags=["Users"])  # Создание маршрутизатора API с тегом "Users"

# Создание маршрута для получения информации о пользователе "/me"
router.include_router(
    router=fastapi_users.get_users_router(
        user_schema=UserRead,
        user_update_schema=UserUpdate,
    )
)
