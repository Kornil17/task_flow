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
    # ----------------------------------------

    class Config:
        env_file = ".env"
        env_file_encoding = "utf8"


settings = Settings()
