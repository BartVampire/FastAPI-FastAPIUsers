from fastapi_users import FastAPIUsers
from core.models import User
from core.types.user_id_type import UserIdType
from .user_manager_dependencies import get_user_manager
from .backend import authentication_backend

"""
Инициализирует экземпляр FastAPIUsers с моделями User и UserIdType.

Эта функция инициализирует экземпляр FastAPIUsers с указанным менеджером пользователей и провайдерами аутентификации.

Параметры:
- get_user_manager: Функция, возвращающая экземпляр UserManager. Эта функция должна быть определена в модуле user_manager_dependencies.
- authentication_backends: Список провайдеров аутентификации. В этом случае он содержит только один провайдер, определенный в модуле backend.

Возвращает:
- fastapi_users: Экземпляр FastAPIUsers[User, UserIdType], инициализированный с указанным менеджером пользователей и провайдерами аутентификации.
"""

fastapi_users = FastAPIUsers[User, UserIdType](
    get_user_manager,
    [authentication_backend],
)

current_user_route = fastapi_users.current_user(active=True)
current_superuser_route = fastapi_users.current_user(active=True, superuser=True)
