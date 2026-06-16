from dependency_injector import containers
from dependency_injector.providers import Configuration, Container

from di.web_app import WebAppContainer
from src.infrastructure.configuration import settings


class ApplicationContainer(containers.DeclarativeContainer):
    """Основной контейнер приложения."""

    config = Configuration()
    web_app_container = Container(WebAppContainer, config=config)


application_container = ApplicationContainer()
application_container.config.from_pydantic(settings=settings)


__all__ = ("ApplicationContainer", "application_container")
