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

from src.presentation.dtos.models import Comment, Error, Task
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
                endpoint="get",
                methods=[HTTPMethod.GET],
                responses={
                    HTTPStatus.OK: {"model": Task},
                    HTTPStatus.NOT_FOUND: {"model": Error},
                    HTTPStatus.INTERNAL_SERVER_ERROR: {"model": Error},
                },
            ),
            Dict(
                path="/{task_id}",
                endpoint="delete",
                methods=[HTTPMethod.DELETE],
                responses={
                    HTTPStatus.NOT_FOUND: {"model": Error},
                    HTTPStatus.INTERNAL_SERVER_ERROR: {"model": Error},
                },
            ),
            Dict(
                path="/{task_id}",
                endpoint="edit",
                methods=[HTTPMethod.PATCH],
                responses={
                    HTTPStatus.OK: {"model": Task},
                    HTTPStatus.NOT_FOUND: {"model": Error},
                    HTTPStatus.INTERNAL_SERVER_ERROR: {"model": Error},
                },
            ),
            Dict(
                path="",
                endpoint="create",
                methods=[HTTPMethod.POST],
                responses={
                    HTTPStatus.CREATED: {"model": Task},
                    HTTPStatus.INTERNAL_SERVER_ERROR: {"model": Error},
                },
            ),
            Dict(
                path="/{task_id}/executor",
                endpoint="assign_executor",
                methods=[HTTPMethod.POST],
                responses={
                    HTTPStatus.OK: {"model": Task},
                    HTTPStatus.NOT_FOUND: {"model": Error},
                    HTTPStatus.INTERNAL_SERVER_ERROR: {"model": Error},
                },
            ),
            Dict(
                path="/{task_id}/status",
                endpoint="update_status",
                methods=[HTTPMethod.PATCH],
                responses={
                    HTTPStatus.OK: {"model": Task},
                    HTTPStatus.NOT_FOUND: {"model": Error},
                    HTTPStatus.BAD_REQUEST: {"model": Error},
                },
            ),
            Dict(
                path="/{task_id}/deadline",
                endpoint="update_deadline",
                methods=[HTTPMethod.PATCH],
                responses={
                    HTTPStatus.OK: {"model": Task},
                    HTTPStatus.NOT_FOUND: {"model": Error},
                    HTTPStatus.BAD_REQUEST: {"model": Error},
                },
            ),
            Dict(
                path="/{task_id}/comments",
                endpoint="add_comments",
                methods=[HTTPMethod.POST],
                responses={
                    HTTPStatus.CREATED: {"model": Comment},
                    HTTPStatus.NOT_FOUND: {"model": Error},
                    HTTPStatus.INTERNAL_SERVER_ERROR: {"model": Error},
                },
            ),
            Dict(
                path="/{task_id}/comments",
                endpoint="get_comments",
                methods=[HTTPMethod.GET],
                responses={
                    HTTPStatus.OK: {"model": Comment},
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
