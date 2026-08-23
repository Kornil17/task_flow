from typing import final

from pydantic import Field
from pydantic_settings import BaseSettings


@final
class Settings(BaseSettings):
    """Класс для получения настроек приложения."""

    # Настройки uvicorn ----------------------
    host: str = Field(
        description="Хост сервера.",
    )
    port: int = Field(
        description="Порт сервера.",
    )
    instances: int = Field(
        description="Кол-во процессов приложения.",
        ge=1,
        le=10,
    )
    reload: bool = Field(
        description="Флаг динамечской подгрузки изменений в приложение.",
        default=False,
    )
    # ----------------------------------------
    # Настройки web_api ----------------------
    title: str = Field(
        description="Заголовок приложения",
        default="Task Flow",
    )
    description: str = Field(
        description="Описание приложения",
        default="Сервис для управления задачами.",
    )
    version: str = Field(
        description="Версия приложения.",
        default="0.1.0",
    )
    debug: bool = Field(
        description="Режим дебага приложения",
        default=False,
    )
    request_timeout: float = Field(
        description="Таймаут на выполнение запроса.",
        gt=0,
        lt=60,
        default=30.0,
    )
    # ----------------------------------------
    # Настройки БД ----------------------
    db_host: str = Field(
        description="Хост для подключения к БД.",
    )
    db_port: int = Field(
        description="Порт для подключения к БД.",
    )
    db_name: str = Field(
        description="Название подключаемой БД.",
        default="task_flow",
    )
    db_user: str = Field(
        description="Имя пользователя для подключения к БД.",
    )
    db_password: str = Field(
        description="Пароль пользователя для подключения к БД.",
    )
    db_min_pool_size: int = Field(
        description="Минимальное кол-во коннектов к БД в пуле.",
    )
    db_max_pool_size: int = Field(
        description="Максимальное кол-во коннектов к БД в пуле.",
    )
    db_max_connection_life_time: float = Field(
        description="Максимальное время жизни неиспользуемого "
        "открытого подключения(s).",
        gt=30.0,
        default=300.0,
    )
    # ----------------------------------------

    class Config:
        env_file = ".env"
        env_file_encoding = "utf8"


settings = Settings()
