from http import HTTPMethod, HTTPStatus
from typing import Literal, TypedDict


class RouterConfigData[Entity, Error](TypedDict):
    """Конфигурация данных для подключаемого роутера."""

    path: str
    endpoint: str
    methods: list[HTTPMethod]
    responses: dict[
        Literal[HTTPStatus.OK]
        | Literal[HTTPStatus.CREATED]
        | Literal[HTTPStatus.NOT_FOUND]
        | Literal[HTTPStatus.INTERNAL_SERVER_ERROR]
        | Literal[HTTPStatus.BAD_REQUEST],
        dict[str, type[Entity]] | dict[str, type[Error]],
    ]
