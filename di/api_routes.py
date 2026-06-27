from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import (
    AttributeGetter,
    Configuration,
    Dict,
    List,
    Singleton,
)
from fastapi import APIRouter

from di.api_routes_config import (
    ADD_COMMENTS,
    ASSIGN_EXECUTOR,
    CREATE_TASK,
    CREATE_USER,
    DELETE_TASK,
    EDIT_TASK,
    GET_COMMENTS,
    GET_TASK,
    GET_USER,
    UPDATE_DEADLINE,
    UPDATE_STATUS,
)
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
            Dict(GET_TASK),
            Dict(DELETE_TASK),
            Dict(EDIT_TASK),
            Dict(CREATE_TASK),
            Dict(ASSIGN_EXECUTOR),
            Dict(UPDATE_STATUS),
            Dict(UPDATE_DEADLINE),
            Dict(ADD_COMMENTS),
            Dict(GET_COMMENTS),
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
            Dict(CREATE_USER),
            Dict(GET_USER),
        ),
    )
    user_router = AttributeGetter(user_routes, "router")
    task_router = AttributeGetter(tasks_routes, "router")
    routes = List(
        task_router,
        user_router,
    )
