from dataclasses import dataclass
from typing import final

from fastapi import APIRouter

from src.presentation.dtos.models import Error, Task
from src.presentation.routers import RoterConfigData


@final
@dataclass(slots=True, frozen=True, kw_only=True)
class TasksRouter:
    """Обработчик API запросов по задачам."""

    _base_router: APIRouter
    _routes_config_data: list[RoterConfigData]

    def __post_init__(self) -> None:
        """Регистрация обработчиков в базовый роут."""
        for router_config in self._routes_config_data:
            self._base_router.add_api_route(
                **{
                    **router_config,
                    "endpoint": getattr(self, router_config["endpoint"]),
                },
            )

    async def get_task_by_id(self, task_id: int) -> Task | Error:  # type: ignore[empty-body]
        """Получение задачи по ID."""

    async def delete_task_by_id(self, task_id: int) -> Task | Error:  # type: ignore[empty-body]
        """Удаление задачи по ID."""

    @property
    def router(self) -> APIRouter:
        """Возращаем базовый обогащенный API обработчик."""
        return self._base_router
