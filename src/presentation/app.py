import logging
from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import final

import uvicorn
from fastapi import APIRouter, FastAPI
from starlette.middleware.base import BaseHTTPMiddleware

from src.infrastructure.configuration import settings


_logger = logging.getLogger("root")


@final
@dataclass(slots=True, frozen=True, kw_only=True)
class Application:
    """Класс запуска приложения."""

    _web_app: FastAPI
    _api_routes: Iterable[APIRouter]
    _api_middlewares: Iterable[type[BaseHTTPMiddleware]]
    _logger: logging.Logger = field(default=_logger)

    async def run(self) -> None:
        """Запуск приложения."""
        self._logger.debug("Start registration app routes.")
        await self._registration_api_routes()
        self._logger.debug("Start registration app middlewares.")
        await self._registration_api_middlewares()
        self._logger.debug("Start configuration ASGI server.")
        await self._run_server()

    async def _registration_api_routes(self) -> None:
        """Регистрация обработчиков API запросов."""
        for api_router in self._api_routes:
            self._web_app.include_router(api_router)
            self._logger.debug("Add APIRoute '%s'", api_router)

    async def _registration_api_middlewares(self) -> None:
        """Регистрация промежуточнчых слоев API."""
        for middleware in self._api_middlewares:
            self._web_app.add_middleware(middleware)
            self._logger.debug("Add middleware '%s'", middleware)

    async def _run_server(self) -> None:
        """Запуск сервера ASGI."""
        config = uvicorn.Config(
            app=self._web_app,
            host=settings.host,
            port=settings.port,
            workers=settings.instances,
            reload=settings.reload,
        )
        self._logger.debug("Start ASGI with config '%s'", config)
        await uvicorn.Server(config).serve()
