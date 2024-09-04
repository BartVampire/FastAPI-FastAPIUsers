from pydantic import BaseModel, PostgresDsn
from pydantic_settings import BaseSettings


class RunConfiguration(BaseModel):
    """
    Конфигурация запуска приложения
    """

    host: str = "0.0.0.0"
    port: int = 8000


class ApiPrefix(BaseModel):
    """
    Префикс для API
    """

    prefix: str = "/api"


class DatabaseConfig(BaseModel):
    """
    Конфигурация базы данных
    """

    url: PostgresDsn
    echo: bool = False,  # Логирование SQL-запросов в консоль
    echo_pool: bool = False,  # Выводить логирование пула соединений
    pool_size: int = 50,  # Размер количества соединений в пуле
    max_overflow: int = 10, # Количество превышения пула соединений


class Settings(BaseSettings):
    """
    Настройки приложения
    """

    run: RunConfiguration = RunConfiguration()  # Конфигурация запуска приложения
    api: ApiPrefix = ApiPrefix()  # Конфигурация префикса для API
    db: DatabaseConfig


settings = Settings()
