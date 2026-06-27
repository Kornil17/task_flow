from http import HTTPMethod, HTTPStatus
from typing import TypedDict

from pydantic.v1 import BaseModel


class RoterConfigData(TypedDict):
    """Конфигурация данных для подключаемого роутера."""

    path: str
    endpoint: str
    methods: list[HTTPMethod]
    responses: dict[HTTPStatus, dict[str, BaseModel]]
