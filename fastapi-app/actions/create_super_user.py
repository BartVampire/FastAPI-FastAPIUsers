import asyncio
import contextlib
from email.policy import default

from api.dependencies.authentication.user_manager_dependencies import get_user_manager
from api.dependencies.authentication.users_dependencies import get_user_db
from core.authentication.user_manager import UserManager
from core.models import db_helper
from core.schemas.user_schema import UserCreate

get_users_db_context = contextlib.asynccontextmanager(get_user_db)
get_user_manager_context = contextlib.asynccontextmanager(get_user_manager)


default_username = "LordBart"
default_email = "admin@example.com"
default_password = "password"
default_is_active = True
default_is_superuser = True
default_is_verified = True


async def create_user(user_manager: UserManager, user_create: UserCreate):
    user = await user_manager.create(
        user_create,
        safe=False,
    )
    return user


async def create_superuser(
    username: str = default_username,
    email: str = default_email,
    password: str = default_password,
    is_active: bool = default_is_active,
    is_superuser: bool = default_is_superuser,
    is_verified: bool = default_is_verified,
):
    user_create = UserCreate(
        username=username,
        email=email,
        password=password,
        is_active=is_active,
        is_superuser=is_superuser,
        is_verified=is_verified,
    )

    async with db_helper.session_factory() as session:
        async with get_users_db_context(session) as user_db:
            async with get_user_manager_context(user_db) as user_manager:
                return await create_user(user_manager, user_create)


if __name__ == "__main__":
    asyncio.run(create_superuser())
