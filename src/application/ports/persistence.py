from contextlib import AbstractAsyncContextManager
from typing import Literal, Protocol


IsolationLevel = Literal[
    "read_committed",
    "read_uncommitted",
    "serializable",
    "repeatable_read",
]


class IDBClient[
    Params,
    QueryResponse,
    CommandResponse,
](Protocol):
    """Декларация контракта клиента БД."""

    async def begin(
        self,
        *,
        isolation_level: IsolationLevel | None = None,
        readonly: bool = False,
    ) -> None:
        """Начало транзакции."""

    async def commit(self) -> None:
        """Фиксирует текущую транзакцию."""

    async def rollback(self) -> None:
        """Откатывает текущую транзакцию."""

    async def execute_query(
        self,
        query: str,
        params: Params | None = None,
    ) -> QueryResponse:
        """Выполняет SELECT-запрос и возвращает список строк."""

    async def execute_command(
        self,
        query: str,
        params: Params | None = None,
    ) -> CommandResponse:
        """Выполняет INSERT/UPDATE/DELETE, возвращает количество затрагиваемых строк."""


class IDBTransactionManager[
    Params,
    QueryResponse,
    CommandResponse,
]:
    """Декларация контракта для менеджера управления транзакциями БД."""

    def start(
        self,
        *,
        isolation_level: IsolationLevel | None = None,
        readonly: bool = False,
    ) -> AbstractAsyncContextManager[
        IDBClient[
            Params,
            QueryResponse,
            CommandResponse,
        ],
    ]:
        """Старт транзакции."""
