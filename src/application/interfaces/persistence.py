from enum import StrEnum, unique
from typing import Any, Protocol


@unique
class IsolationLevel(StrEnum):
    """Уровни изоляции транзакций."""

    READ_COMMITTED = "READ COMMITTED"
    REPEATABLE_READ = "REPEATABLE READ"
    SERIALIZABLE = "SERIALIZABLE"
    READ_UNCOMMITTED = "READ UNCOMMITTED"


class IDBClient[TransactionObject, Params](Protocol):
    """Декларация контракта клиента БД."""

    async def begin(
        self,
        *,
        isolation_level: IsolationLevel | None = None,
        read_only: bool = False,
        timeout_ms: int | None = None,
    ) -> TransactionObject:
        """Начало транзакции."""

    async def commit(self) -> None:
        """Фиксация транзакции."""

    async def rollback(self) -> None:
        """Откат транзакции."""

    async def execute_query(
        self,
        connection: TransactionObject,
        query: str,
        params: Params | None = None,
    ) -> list[dict[str, Any]]:
        """Выполняет SELECT-запрос и возвращает список строк."""

    async def execute_command(
        self,
        connection: TransactionObject,
        query: str,
        params: Params | None = None,
    ) -> int:
        """Выполняет INSERT/UPDATE/DELETE, возвращает количество затрагиваемых строк."""
