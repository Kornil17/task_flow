from typing import final

from pydantic import Field
from pydantic.v1 import BaseSettings


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
    # ----------------------------------------

    class Config:
        env_file = ".env"
        env_file_encoding = "utf8"


settings = Settings()
