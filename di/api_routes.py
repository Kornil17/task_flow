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

from src.presentation.dtos.models import (
    Comment,
    Error,
    Task,
    User,
)
from src.presentation.routers.constants import MODEL_NAME
from src.presentation.routers.tasks import TasksRouter
from src.presentation.routers.users import UsersRouter


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
                    HTTPStatus.OK: {MODEL_NAME: Task},
                    HTTPStatus.NOT_FOUND: {MODEL_NAME: Error},
                    HTTPStatus.INTERNAL_SERVER_ERROR: {MODEL_NAME: Error},
                },
            ),
            Dict(
                path="/{task_id}",
                endpoint="delete",
                methods=[HTTPMethod.DELETE],
                responses={
                    HTTPStatus.NOT_FOUND: {MODEL_NAME: Error},
                    HTTPStatus.INTERNAL_SERVER_ERROR: {MODEL_NAME: Error},
                },
            ),
            Dict(
                path="/{task_id}",
                endpoint="edit",
                methods=[HTTPMethod.PATCH],
                responses={
                    HTTPStatus.OK: {MODEL_NAME: Task},
                    HTTPStatus.NOT_FOUND: {MODEL_NAME: Error},
                    HTTPStatus.INTERNAL_SERVER_ERROR: {MODEL_NAME: Error},
                },
            ),
            Dict(
                path="",
                endpoint="create",
                methods=[HTTPMethod.POST],
                responses={
                    HTTPStatus.CREATED: {MODEL_NAME: Task},
                    HTTPStatus.INTERNAL_SERVER_ERROR: {MODEL_NAME: Error},
                },
            ),
            Dict(
                path="/{task_id}/executor",
                endpoint="assign_executor",
                methods=[HTTPMethod.POST],
                responses={
                    HTTPStatus.OK: {MODEL_NAME: Task},
                    HTTPStatus.NOT_FOUND: {MODEL_NAME: Error},
                    HTTPStatus.INTERNAL_SERVER_ERROR: {MODEL_NAME: Error},
                },
            ),
            Dict(
                path="/{task_id}/status",
                endpoint="update_status",
                methods=[HTTPMethod.PATCH],
                responses={
                    HTTPStatus.OK: {MODEL_NAME: Task},
                    HTTPStatus.NOT_FOUND: {MODEL_NAME: Error},
                    HTTPStatus.BAD_REQUEST: {MODEL_NAME: Error},
                },
            ),
            Dict(
                path="/{task_id}/deadline",
                endpoint="update_deadline",
                methods=[HTTPMethod.PATCH],
                responses={
                    HTTPStatus.OK: {MODEL_NAME: Task},
                    HTTPStatus.NOT_FOUND: {MODEL_NAME: Error},
                    HTTPStatus.BAD_REQUEST: {MODEL_NAME: Error},
                },
            ),
            Dict(
                path="/{task_id}/comments",
                endpoint="add_comments",
                methods=[HTTPMethod.POST],
                responses={
                    HTTPStatus.CREATED: {MODEL_NAME: Comment},
                    HTTPStatus.NOT_FOUND: {MODEL_NAME: Error},
                    HTTPStatus.INTERNAL_SERVER_ERROR: {MODEL_NAME: Error},
                },
            ),
            Dict(
                path="/{task_id}/comments",
                endpoint="get_comments",
                methods=[HTTPMethod.GET],
                responses={
                    HTTPStatus.OK: {MODEL_NAME: Comment},
                    HTTPStatus.NOT_FOUND: {MODEL_NAME: Error},
                    HTTPStatus.INTERNAL_SERVER_ERROR: {MODEL_NAME: Error},
                },
            ),
        ),
    )
    user_routes = Singleton(
        UsersRouter,
        _base_router=Singleton(
            APIRouter,
            prefix="/users",
            tags=["users"],
        ),
        _routes_config_data=List(
            Dict(
                path="",
                endpoint="create",
                methods=[HTTPMethod.POST],
                responses={
                    HTTPStatus.CREATED: {MODEL_NAME: User},
                    HTTPStatus.INTERNAL_SERVER_ERROR: {MODEL_NAME: Error},
                },
            ),
            Dict(
                path="/{user_id}",
                endpoint="get",
                methods=[HTTPMethod.GET],
                responses={
                    HTTPStatus.CREATED: {MODEL_NAME: User},
                    HTTPStatus.NOT_FOUND: {MODEL_NAME: User},
                    HTTPStatus.INTERNAL_SERVER_ERROR: {MODEL_NAME: Error},
                },
            ),
        ),
    )
    user_router = AttributeGetter(user_routes, "router")
    task_router = AttributeGetter(tasks_routes, "router")
    routes = List(
        task_router,
        user_router,
    )
