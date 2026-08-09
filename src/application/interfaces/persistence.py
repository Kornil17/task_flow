from collections.abc import AsyncGenerator
from typing import Literal, Protocol

from asyncpg.pool import PoolConnectionProxy


class IDBTransactionManager:
    """Декларация контракта для менеджера управления транзакциями БД."""

    async def start(
        self,
        *,
        isolation_level: Literal[
            "read_committed",
            "read_uncommitted",
            "serializable",
            "repeatable_read",
        ]
        | None = None,
        readonly: bool = False,
    ) -> AsyncGenerator[PoolConnectionProxy]:
        """Старт транзакции."""


class IDBClient[
    ConnectionObject,
    TransactionObject,
    Params,
    QueryResponse,
    CommandResponse,
](Protocol):
    """Декларация контракта клиента БД."""

    async def begin(
        self,
        *,
        isolation_level: Literal[
            "read_committed",
            "read_uncommitted",
            "serializable",
            "repeatable_read",
        ]
        | None = None,
        readonly: bool = False,
    ) -> tuple[ConnectionObject, TransactionObject]:
        """Начало транзакции."""

    async def commit(
        self,
        transaction: TransactionObject,
    ) -> None:
        """Фиксация транзакции."""

    async def rollback(
        self,
        transaction: TransactionObject,
    ) -> None:
        """Откат транзакции."""

    async def execute_query(
        self,
        connection: ConnectionObject,
        query: str,
        params: Params | None = None,
    ) -> QueryResponse:
        """Выполняет SELECT-запрос и возвращает список строк."""

    async def execute_command(
        self,
        connection: ConnectionObject,
        query: str,
        params: Params | None = None,
    ) -> CommandResponse:
        """Выполняет INSERT/UPDATE/DELETE, возвращает количество затрагиваемых строк."""
