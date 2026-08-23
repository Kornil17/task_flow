from dataclasses import dataclass
from typing import Annotated, final

from fastapi import Body

from src.presentation.dtos.models import (
    CreateUserData,
    Error,
    User,
)
from src.presentation.routers.base import BaseRouter


@final
@dataclass(slots=True, frozen=True, kw_only=True)
class UsersRouter(BaseRouter):
    """Обработчик API запросов по пользователям."""

    async def create(
        self,
        user_data: Annotated[CreateUserData, Body()],
    ) -> User | Error:
        """Создание пользователя."""

    async def get(self, user_id: int) -> User | Error:
        """Получение пользователя."""
