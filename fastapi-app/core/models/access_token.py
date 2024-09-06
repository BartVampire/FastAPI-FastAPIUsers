from typing import TYPE_CHECKING

from fastapi_users_db_sqlalchemy.access_token import (
    SQLAlchemyBaseAccessTokenTable,
    SQLAlchemyAccessTokenDatabase,
)
from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from core.models import BaseModel
from core.types.user_id_type import UserIdType

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class AccessToken(BaseModel, SQLAlchemyBaseAccessTokenTable[UserIdType]):
    """
      Модель токена доступа представляет собой токен доступа к системе.

    Атрибуты:
    -----------
    user_id : Mapped[UserIdType] - (UserIdType = Integer)
        Идентификатор пользователя, которому принадлежит токен.

    Methods:
    --------
    get_access_token_db(session: "AsyncSession") -> SQLAlchemyAccessTokenDatabase
        Создает экземпляр базы данных токенов доступа с использованием указанной сессии.
    """

    user_id: Mapped[UserIdType] = mapped_column(
        Integer, ForeignKey("users.id", ondelete="cascade"), nullable=False
    )

    @classmethod
    def get_access_token_db(cls, session: "AsyncSession"):
        return SQLAlchemyAccessTokenDatabase(session, AccessToken)
