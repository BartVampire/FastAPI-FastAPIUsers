from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy.orm import Mapped, mapped_column
from .base_model import BaseModel
from .mixins.id_int_pk import IdIntPrimaryKeyMixin


class User(BaseModel, IdIntPrimaryKeyMixin, SQLAlchemyBaseUserTable[int]):
    """
    Модель пользователя представляет собой пользователя системы.
    """

    username: Mapped[str] = mapped_column(
        unique=True
    )  # Имя пользователя (уникальное поле)
