from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Configuration, List

from src.presentation.middlewares import (
    ExceptionMiddleware,
    TimeoutMiddleware,
    TimeProcessingMiddleware,
)


class MiddlewareContainer(DeclarativeContainer):
    """Контейнер для хранения данных о промежуточных слоях API."""

    config = Configuration()
    # от порядка регистрации зависит порядок отработки
    middlewares = List(
        ExceptionMiddleware,
        TimeoutMiddleware,
        TimeProcessingMiddleware,
    )
