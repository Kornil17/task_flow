from dependency_injector import containers
from dependency_injector.providers import Configuration, Singleton
from fastapi import FastAPI


class WebAppContainer(containers.DeclarativeContainer):
    """Контейнер для управления веб приложением."""

    config = Configuration()
    app = Singleton(
        FastAPI,
        title=config.title,
        description=config.description,
        version=config.version,
        debug=config.debug,
    )
