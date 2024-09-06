from typing import Annotated, TYPE_CHECKING
from fastapi import Depends
from core.models import db_helper, AccessToken

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


async def get_access_tokens_db(
    session: Annotated["AsyncSession", Depends(db_helper.session_getter)]
):
    """
    Асинхронно получает токены доступа из базы данных с использованием указанной сессии.

    Параметры:
    - session (Annotated[AsyncSession, Depends(db_helper.session_getter)]):
        Асинхронная сессия базы данных, полученная из зависимости `db_helper.session_getter`.

    Возвращает:
    - AccessToken:
        Генератор, выдающий токены доступа, полученные из базы данных.
    """

    yield AccessToken.get_access_token_db(session=session)
