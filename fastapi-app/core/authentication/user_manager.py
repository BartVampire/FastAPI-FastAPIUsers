import logging
import uuid
from typing import Optional, TYPE_CHECKING

from fastapi import Depends, Request
from fastapi_users import BaseUserManager, IntegerIDMixin
from core.config import settings
from core.models import User
from core.types.user_id_type import UserIdType

if TYPE_CHECKING:
    from fastapi import Request

log = logging.getLogger(__name__)


class UserManager(IntegerIDMixin, BaseUserManager[User, UserIdType]):
    """
    Класс UserManager для управления операциями пользователей. Наследуется от IntegerIDMixin и BaseUserManager.
    """

    reset_password_token_secret = settings.access_token.reset_password_token_secret
    verification_token_secret = settings.access_token.verification_token_secret

    async def on_after_register(self, user: User, request: Optional["Request"] = None):
        """
        Записывает предупреждение в журнал после регистрации пользователя.

        Параметры:
        - user (User): Объект пользователя, который был зарегистрирован.
        - request (Optional[Request]): Объект запроса FastAPI. По умолчанию None.

        Возвращает:
        - None
        """
        log.warning("Пользователь зарегистрирован: %r", user.id)

    async def on_after_forgot_password(
        self, user: User, token: str, request: Optional["Request"] = None
    ):
        """
        Записывает предупреждение в журнал после того, как пользователь запросил сброс пароля.

        Параметры:
        - user (User): Объект пользователя, который запросил сброс пароля.
        - token (str): Токен сброса пароля.
        - request (Optional[Request]): Объект запроса FastAPI. По умолчанию None.

        Возвращает:
        - None
        """

        log.warning(
            "Пользователь %r забыл свой пароль. Reset token: %r", user.id, token
        )

    async def on_after_request_verify(
        self, user: User, token: str, request: Optional["Request"] = None
    ):
        """
        Записывает предупреждение в журнал после того, как пользователь запросил подтверждение по электронной почте.

        Параметры:
        - user (User): Объект пользователя, который запросил подтверждение по электронной почте.
        - token (str): Токен подтверждения.
        - request (Optional[Request]): Объект запроса FastAPI. По умолчанию None.

        Возвращает:
        - None
        """

        log.warning(
            "Запрошено подтверждение для пользователя %r. Токен подтверждения: %r",
            user.id,
            token,
        )
