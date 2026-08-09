from dataclasses import dataclass, field
from logging import Logger, getLogger
from typing import Any, Literal

from asyncpg import Pool
from asyncpg.pool import PoolConnectionProxy
from asyncpg.transaction import Transaction


_logger = getLogger("infrastructure")


@dataclass(frozen=True, slots=True, kw_only=True)
class PostgresDBClient:
    """Клиент для работы с БД PostgresSQL."""

    _pool_clients: Pool
    _logger: Logger = field(default=_logger)

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
        self._logger.debug(
            "Start readonly='%s' transaction isolation_level='%s'.",
            readonly,
            isolation_level,
        )
        connection = await self._pool_clients.acquire()

        tx = connection.transaction(
            isolation=isolation_level,
            readonly=readonly,
        )

        self._logger.debug(
            "Transaction id=%s is started.",
            tx._id,
        )
        await tx.start()

        return connection, tx

    async def commit(
        self,
        transaction: Transaction,
    ) -> None:
        """Фиксация транзакции."""
        self._logger.debug(
            "Start commit transaction id=%s",
            transaction._id,
        )
        await transaction.commit()

    async def rollback(
        self,
        transaction: Transaction,
    ) -> None:
        """Откат транзакции."""
        self._logger.debug(
            "Start rollback transaction id=%s",
            transaction._id,
        )
        await transaction.rollback()

    async def execute_query(
        self,
        connection: PoolConnectionProxy,
        query: str,
        params: dict[str, Any] | None = None,
    ) -> list[dict[str, Any]]:
        """Выполняет SELECT-запрос и возвращает список строк."""
        self._logger.debug(
            "Execute query='%s' with params='%s' by connection=%s",
            query,
            params,
            str(connection),
        )
        params = params or {}
        query_resp = await connection.fetch(
            query=query,
            **params,
        )
        self._logger.debug(
            "Executed query='%s' with params='%s' got resp='%s'.",
            query,
            params,
            query_resp,
        )
        return query_resp  # type: ignore[no-any-return]

    async def execute_command(
        self,
        connection: PoolConnectionProxy,
        query: str,
        params: dict[str, Any] | None = None,
    ) -> str:
        """Выполняет INSERT/UPDATE/DELETE, возвращает количество затрагиваемых строк."""
        self._logger.debug(
            "Execute query='%s' with params='%s' by connection=%s",
            query,
            params,
            str(connection),
        )
        params = params or {}
        query_resp = await connection.execute(
            query=query,
            **params,
        )
        self._logger.debug(
            "Executed query='%s' with params='%s' got resp='%s'.",
            query,
            params,
            query_resp,
        )
        return query_resp
