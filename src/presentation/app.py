from dataclasses import dataclass
from typing import final

import uvicorn
from uvicorn._types import ASGIApplication

from src.infrastructure.configuration import settings


@final
@dataclass(slots=True, frozen=True, kw_only=True)
class Application:
    """Класс запуска приложения."""

    _web_app: ASGIApplication

    async def run(self) -> None:
        """Запуск приложения."""
        await self._run_server()

    async def _run_server(self) -> None:
        """Запуск сервера ASGI."""
        config = uvicorn.Config(
            app=self._web_app,
            host=settings.host,
            port=settings.port,
            workers=settings.instances,
            reload=settings.reload,
        )
        await uvicorn.Server(config).serve()
