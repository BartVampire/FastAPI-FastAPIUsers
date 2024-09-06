from typing import TYPE_CHECKING

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from sqlalchemy.orm import Mapped, mapped_column
from .base_model import BaseModel
from .mixins.id_int_pk import IdIntPrimaryKeyMixin

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession

class User(BaseModel, IdIntPrimaryKeyMixin, SQLAlchemyBaseUserTable[int]):
    """
    Модель пользователя представляет собой пользователя системы.
    Attributes:
    username: Mapped[str] = mapped_column(unique=True)
        Имя пользователя (уникальное поле)

    Methods:
    get_db(cls, session: "AsyncSession") -> SQLAlchemyUserDatabase
        Возвращает экземпляр SQLAlchemyUserDatabase, инициализированный сессией и текущей моделью пользователя.
    """

    username: Mapped[str] = mapped_column(
        unique=True
    )  # Имя пользователя (уникальное поле)

    @classmethod
    def get_db(cls, session: "AsyncSession"):
        return SQLAlchemyUserDatabase(session, User)
