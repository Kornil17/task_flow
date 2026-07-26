from enum import StrEnum, unique
from typing import Protocol


@unique
class IsolationLevel(StrEnum):
    """Уровни изоляции транзакций."""

    READ_COMMITTED = "READ COMMITTED"
    REPEATABLE_READ = "REPEATABLE READ"
    SERIALIZABLE = "SERIALIZABLE"
    READ_UNCOMMITTED = "READ UNCOMMITTED"


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
        isolation_level: IsolationLevel | None = None,
        read_only: bool = False,
        timeout_ms: int | None = None,
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
