from http import HTTPMethod, HTTPStatus

from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import (
    AttributeGetter,
    Configuration,
    Dict,
    List,
    Singleton,
)
from fastapi import APIRouter

from src.presentation.dtos.models import Error, Task
from src.presentation.routers.tasks import TasksRouter


class ApiRoutesContainer(DeclarativeContainer):
    """Контейнер с данными по обработчикам запросов API."""

    config = Configuration()

    tasks_routes = Singleton(
        TasksRouter,
        _base_router=Singleton(
            APIRouter,
            prefix="/tasks",
            tags=["tasks"],
        ),
        _routes_config_data=List(
            Dict(
                path="/{task_id}",
                endpoint="get_task_by_id",
                methods=[HTTPMethod.GET],
                responses={
                    HTTPStatus.OK: {"model": Task},
                    HTTPStatus.NOT_FOUND: {"model": Error},
                    HTTPStatus.INTERNAL_SERVER_ERROR: {"model": Error},
                },
            ),
        ),
    )
    user_router = Singleton(
        APIRouter,
        prefix="/users",
        tags=["users"],
    )
    task_router = AttributeGetter(tasks_routes, "router")
    routes = List(
        task_router,
        user_router,
    )
