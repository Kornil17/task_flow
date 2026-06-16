from typing import final

import uvicorn
from dependency_injector.wiring import Provide, inject
from uvicorn._types import ASGIApplication

from di.application import ApplicationContainer, application_container
from src.infrastructure.configuration import settings


@final
class Application:
    """Класс запуска приложения."""

    @inject
    async def run(
        self,
        web_app: ASGIApplication = Provide[ApplicationContainer.web_app_container.app],
    ) -> None:
        config = uvicorn.Config(
            app=web_app,
            host=settings.host,
            port=settings.port,
            workers=settings.instances,
            reload=settings.reload,
        )
        await uvicorn.Server(config).serve()


application_container.wire(modules=[__name__])
