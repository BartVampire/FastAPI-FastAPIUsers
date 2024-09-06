from typing import TYPE_CHECKING, Annotated
from fastapi import Depends
from core.models import db_helper, User

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


async def get_user_db(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)]
):
    """
    Получает текущего пользователя из асинхронной сессии базы данных.

    Параметры:
    session : Annotated[AsyncSession, Depends(db_helper.session_getter)]
        Асинхронная сессия базы данных, полученная через зависимость `db_helper.session_getter`.
        Эта сессия предоставляется зависимостью и автоматически закрывается после использования.

    Возвращает:
    AsyncGenerator[User, None]
        Генератор, который выдает текущего пользователя.
        Вызов `next()` на этом генераторе вернет текущего пользователя.
        После использования генератор закрывается автоматически.
    """

    yield User.get_db(session=session)
