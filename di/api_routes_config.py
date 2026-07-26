from http import HTTPMethod, HTTPStatus
from typing import Annotated

from src.presentation.dtos.models import (
    Comment,
    Error,
    Task,
    User,
)
from src.presentation.routers import RouterConfigData


_MODEL_NAME: Annotated[
    str,
    """Название модели ответа на API запрос.""",
] = "models"


GET_TASK = RouterConfigData[Task, Error](
    path="/{task_id}",
    endpoint="get",
    methods=[HTTPMethod.GET],
    responses={
        HTTPStatus.OK: {_MODEL_NAME: Task},
        HTTPStatus.NOT_FOUND: {_MODEL_NAME: Error},
        HTTPStatus.INTERNAL_SERVER_ERROR: {_MODEL_NAME: Error},
    },
)


DELETE_TASK = RouterConfigData[Task, Error](
    path="/{task_id}",
    endpoint="delete",
    methods=[HTTPMethod.DELETE],
    responses={
        HTTPStatus.NOT_FOUND: {_MODEL_NAME: Error},
        HTTPStatus.INTERNAL_SERVER_ERROR: {_MODEL_NAME: Error},
    },
)


EDIT_TASK = RouterConfigData[Task, Error](
    path="/{task_id}",
    endpoint="edit",
    methods=[HTTPMethod.PATCH],
    responses={
        HTTPStatus.OK: {_MODEL_NAME: Task},
        HTTPStatus.NOT_FOUND: {_MODEL_NAME: Error},
        HTTPStatus.INTERNAL_SERVER_ERROR: {_MODEL_NAME: Error},
    },
)


CREATE_TASK = RouterConfigData[Task, Error](
    path="",
    endpoint="create",
    methods=[HTTPMethod.POST],
    responses={
        HTTPStatus.CREATED: {_MODEL_NAME: Task},
        HTTPStatus.INTERNAL_SERVER_ERROR: {_MODEL_NAME: Error},
    },
)


ASSIGN_EXECUTOR = RouterConfigData[Task, Error](
    path="/{task_id}/executor",
    endpoint="assign_executor",
    methods=[HTTPMethod.POST],
    responses={
        HTTPStatus.OK: {_MODEL_NAME: Task},
        HTTPStatus.NOT_FOUND: {_MODEL_NAME: Error},
        HTTPStatus.INTERNAL_SERVER_ERROR: {_MODEL_NAME: Error},
    },
)


UPDATE_STATUS = RouterConfigData[Task, Error](
    path="/{task_id}/status",
    endpoint="update_status",
    methods=[HTTPMethod.PATCH],
    responses={
        HTTPStatus.OK: {_MODEL_NAME: Task},
        HTTPStatus.NOT_FOUND: {_MODEL_NAME: Error},
        HTTPStatus.BAD_REQUEST: {_MODEL_NAME: Error},
    },
)


UPDATE_DEADLINE = RouterConfigData[Task, Error](
    path="/{task_id}/deadline",
    endpoint="update_deadline",
    methods=[HTTPMethod.PATCH],
    responses={
        HTTPStatus.OK: {_MODEL_NAME: Task},
        HTTPStatus.NOT_FOUND: {_MODEL_NAME: Error},
        HTTPStatus.BAD_REQUEST: {_MODEL_NAME: Error},
    },
)


ADD_COMMENTS = RouterConfigData[Comment, Error](
    path="/{task_id}/comments",
    endpoint="add_comments",
    methods=[HTTPMethod.POST],
    responses={
        HTTPStatus.CREATED: {_MODEL_NAME: Comment},
        HTTPStatus.NOT_FOUND: {_MODEL_NAME: Error},
        HTTPStatus.INTERNAL_SERVER_ERROR: {_MODEL_NAME: Error},
    },
)


GET_COMMENTS = RouterConfigData[Comment, Error](
    path="/{task_id}/comments",
    endpoint="get_comments",
    methods=[HTTPMethod.GET],
    responses={
        HTTPStatus.OK: {_MODEL_NAME: Comment},
        HTTPStatus.NOT_FOUND: {_MODEL_NAME: Error},
        HTTPStatus.INTERNAL_SERVER_ERROR: {_MODEL_NAME: Error},
    },
)


CREATE_USER = RouterConfigData[User, Error](
    path="",
    endpoint="create",
    methods=[HTTPMethod.POST],
    responses={
        HTTPStatus.CREATED: {_MODEL_NAME: User},
        HTTPStatus.INTERNAL_SERVER_ERROR: {_MODEL_NAME: Error},
    },
)


GET_USER = RouterConfigData[User, Error](
    path="/{user_id}",
    endpoint="get",
    methods=[HTTPMethod.GET],
    responses={
        HTTPStatus.CREATED: {_MODEL_NAME: User},
        HTTPStatus.NOT_FOUND: {_MODEL_NAME: User},
        HTTPStatus.INTERNAL_SERVER_ERROR: {_MODEL_NAME: Error},
    },
)
