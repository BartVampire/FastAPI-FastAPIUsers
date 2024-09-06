from typing import Annotated, TYPE_CHECKING
from core.authentication.user_manager import UserManager
from .users_dependencies import get_user_db
from fastapi import Depends

if TYPE_CHECKING:
    from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase


async def get_user_manager(
    user_db: Annotated["SQLAlchemyUserDatabase", Depends(get_user_db)]
):
    yield UserManager(user_db)
