from http import HTTPMethod, HTTPStatus
from typing import Literal, TypedDict

from src.presentation.dtos.models import Error, Task


class RouterConfigData(TypedDict):
    """Конфигурация данных для подключаемого роутера."""

    path: str
    endpoint: str
    methods: list[HTTPMethod]
    responses: dict[
        Literal[HTTPStatus.OK, HTTPStatus.NOT_FOUND, HTTPStatus.INTERNAL_SERVER_ERROR],
        dict[str, type[Task]] | dict[str, type[Error]],
    ]
