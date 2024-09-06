from pydantic import BaseModel, ConfigDict
from fastapi_users import schemas

from core.types.user_id_type import UserIdType


class UserRead(schemas.BaseUser[UserIdType]):
    pass


class UserCreate(schemas.BaseUserCreate):
    pass


class UserUpdate(schemas.BaseUserUpdate):
    pass
