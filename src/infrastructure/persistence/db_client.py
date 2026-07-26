from dataclasses import dataclass
from typing import Any

from asyncpg import Pool
from asyncpg.pool import PoolConnectionProxy
from asyncpg.transaction import Transaction

from src.application.interfaces.persistence import IsolationLevel


@dataclass(frozen=True, slots=True, kw_only=True)
class PostgresDBClient:
    """Клиент для работы с БД PostgresSQL."""

    _pool_clients: Pool

    async def begin(
        self,
        *,
        isolation_level: IsolationLevel | None = None,
        read_only: bool = False,
        timeout_ms: int | None = None,
    ) -> tuple[PoolConnectionProxy, Transaction]:
        """Начало транзакции."""
        async with self._pool_clients.acquire() as connection:
            return connection, await connection.begin(  # type: ignore[attr-defined]
                isolation=isolation_level,
                read_only=read_only,
                timeout=timeout_ms,
            )

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
