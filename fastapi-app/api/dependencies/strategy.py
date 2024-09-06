from typing import TYPE_CHECKING, Annotated

from fastapi import Depends
from fastapi_users.authentication.strategy import DatabaseStrategy
from .access_token_dependencies import get_access_tokens_db
from core.config import settings

if TYPE_CHECKING:
    from core.models import AccessToken
    from fastapi_users.authentication.strategy import AccessTokenDatabase


def get_database_strategy(
    access_token_db: Annotated[
        "AccessTokenDatabase[AccessToken]", Depends(get_access_tokens_db)
    ],
) -> DatabaseStrategy:
    """
    Создаем стратегию авторизации с использованием базы данных.

    Parameters:
    access_token_db (AccessTokenDatabase["AccessToken"], Depends(get_access_tokens_db)):
        Экземпляр базы данных для хранения токенов доступа.
        Экземпляр создается с помощью зависимости `get_access_tokens_db`.

    Returns:
    DatabaseStrategy:
        Стратегия авторизации, использующая указанную базу данных для проверки токенов доступа.
        Время жизни токенов задается настройкой `settings.access_token.lifetime_seconds`.
    """
    return DatabaseStrategy(
        database=access_token_db,
        lifetime_seconds=settings.access_token.lifetime_seconds,
    )
