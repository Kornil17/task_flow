from dependency_injector import containers
from dependency_injector.providers import Configuration, Container, Singleton

from di.api_routes import ApiRoutesContainer
from di.middlewares import MiddlewareContainer
from di.web_app import WebAppContainer
from src.infrastructure.configuration import settings
from src.presentation.app import Application


class ApplicationContainer(containers.DeclarativeContainer):
    """Основной контейнер приложения."""

    config = Configuration()
    web_app_container = Container(WebAppContainer, config=config)
    api_routes_container = Container(ApiRoutesContainer, config=config)
    api_middlewares_container = Container(MiddlewareContainer, config=config)
    application = Singleton(
        Application,
        _web_app=web_app_container.app,
        _api_routes=api_routes_container.routes,
        _api_middlewares=api_middlewares_container.middlewares,
    )


application_container = ApplicationContainer()
application_container.config.from_pydantic(settings=settings)


__all__ = ("ApplicationContainer", "application_container")
