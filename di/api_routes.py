from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Configuration, List, Singleton
from fastapi import APIRouter


class ApiRoutesContainer(DeclarativeContainer):
    """Контейнер с данными по обработчикам запросов API."""

    config = Configuration()

    task_router = Singleton(
        APIRouter,
        prefix="/tasks",
        tags=["tasks"],
    )
    user_router = Singleton(
        APIRouter,
        prefix="/users",
        tags=["users"],
    )
    routes = List(
        task_router,
        user_router,
    )
