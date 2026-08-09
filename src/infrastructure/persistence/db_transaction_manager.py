from collections.abc import AsyncGenerator
from dataclasses import dataclass, field
from logging import Logger, getLogger
from typing import Literal

from asyncpg import InterfaceError
from asyncpg.pool import PoolConnectionProxy

from src.infrastructure.persistence.db_client import PostgresDBClient


_logger = getLogger("infrastructure")


@dataclass(frozen=True, slots=True, kw_only=True)
class PostgresDBTransactionManager:
    """Менеджер для управления транзакциями в PostgresSQL."""

    _db_client: PostgresDBClient
    _logger: Logger = field(default=_logger)

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
        """Начало транзакции."""
        self._logger.info(
            "Start readonly='%s' transaction isolation_level='%s'.",
            readonly,
            isolation_level,
        )
        connection, transaction = await self._db_client.begin(
            isolation_level=isolation_level,
            readonly=readonly,
        )
        self._logger.debug(
            "Got connection='%s' and transaction='%s'.",
            str(connection),
            transaction._id,
        )
        async with transaction:
            try:
                yield connection
                await connection.commit(transaction)
                self._logger.debug("Transaction state='%s'.", transaction._state)
            except InterfaceError:
                self._logger.exception(
                    "Executed transaction='%s' is failed.",
                    transaction._id,
                )
                await connection.rollback(transaction)
                self._logger.debug("Transaction state='%s'.", transaction._state)
