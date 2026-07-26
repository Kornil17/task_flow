from dataclasses import dataclass

from fastapi import APIRouter
from pydantic import BaseModel

from src.presentation.routers import RouterConfigData


@dataclass(slots=True, frozen=True, kw_only=True)
class BaseRouter:
    """Обработчик API запросов по пользователям."""

    _base_router: APIRouter
    _routes_config_data: list[RouterConfigData[BaseModel, BaseModel]]

    def __post_init__(self) -> None:
        """Регистрация обработчиков в базовый роут."""
        for router_config in self._routes_config_data:
            self._base_router.add_api_route(
                **{
                    **router_config,
                    "endpoint": getattr(self, router_config["endpoint"]),
                },
            )

    @property
    def router(self) -> APIRouter:
        """Возращаем базовый обогащенный API обработчик."""
        return self._base_router
