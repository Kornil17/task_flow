from dataclasses import dataclass
from typing import Any, Literal

from asyncpg import Pool
from asyncpg.pool import PoolConnectionProxy
from asyncpg.transaction import Transaction


@dataclass(frozen=True, slots=True, kw_only=True)
class PostgresDBClient:
    """Клиент для работы с БД PostgresSQL."""

    _pool_clients: Pool

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
    ) -> tuple[PoolConnectionProxy, Transaction]:
        """Начало транзакции."""
        connection = await self._pool_clients.acquire()

        tx = connection.transaction(
            isolation=isolation_level,
            readonly=readonly,
        )

        await tx.start()

        return connection, tx

    async def commit(
        self,
        transaction: Transaction,
    ) -> None:
        """Фиксация транзакции."""
        await transaction.commit()

    async def rollback(
        self,
        transaction: Transaction,
    ) -> None:
        """Откат транзакции."""
        await transaction.rollback()

    async def execute_query(
        self,
        connection: PoolConnectionProxy,
        query: str,
        params: dict[str, Any] | None = None,
    ) -> list[dict[str, Any]]:
        """Выполняет SELECT-запрос и возвращает список строк."""
        params = params or {}
        return await connection.fetch(  # type: ignore[no-any-return]
            query=query,
            **params,
        )

    async def execute_command(
        self,
        connection: PoolConnectionProxy,
        query: str,
        params: dict[str, Any] | None = None,
    ) -> str:
        """Выполняет INSERT/UPDATE/DELETE, возвращает количество затрагиваемых строк."""
        params = params or {}
        return await connection.execute(
            query=query,
            **params,
        )
