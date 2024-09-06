from fastapi import APIRouter
from api.dependencies.authentication.backend import authentication_backend
from api.dependencies.authentication.fastapii_user_dispatcher import fastapi_users
from core.config import settings
from core.schemas.user_schema import UserRead, UserCreate

router = APIRouter(
    prefix=settings.api.v1.auth,  # Префикс для маршрутов авторизации /api/v1/auth
    tags=["Auth"],  # Тег для маршрутизатора API Auth
)

# Регистрация маршрутов авторизации в FastAPI-Users /login and /logout
router.include_router(
    router=fastapi_users.get_auth_router(
        authentication_backend,
        requires_verification=True,  # Обязательное подтверждение по электронной почте
    )
)

# Регистрация маршрута создания нового пользователя в FastAPI-Users /register
router.include_router(router=fastapi_users.get_register_router(UserRead, UserCreate))

# Регистрация маршрута подтверждения аккаунта в FastAPI-Users "/verify, /request-verify-token"
router.include_router(router=fastapi_users.get_verify_router(UserRead))

# Регистрация маршрута сброса пароля в FastAPI-Users "/reset-password, /forgot-password"
router.include_router(router=fastapi_users.get_reset_password_router())
