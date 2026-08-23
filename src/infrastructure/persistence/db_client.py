from dataclasses import dataclass, field
from logging import Logger, getLogger
from typing import Any

from asyncpg import Pool, Record
from asyncpg.pool import PoolConnectionProxy
from asyncpg.transaction import Transaction

from src.application.interfaces.persistence import IsolationLevel


_logger = getLogger("infrastructure")


@dataclass(slots=True, kw_only=True)
class PostgresDBClient:
    """
    Клиент для работы с БД PostgresSQL.

    Клиент является transaction-scoped: перед выполнением запросов
    необходимо вызвать 'begin', который получает connection из pool
    и сохраняет его внутри клиента.
    """

    _pool_clients: Pool
    _logger: Logger = field(init=False, default=_logger)
    _connection: PoolConnectionProxy | None = field(
        init=False,
        default=None,
    )
    _transaction: Transaction | None = field(
        init=False,
        default=None,
    )

    async def begin(
        self,
        *,
        isolation_level: IsolationLevel | None = None,
        readonly: bool = False,
    ) -> None:
        """Начало транзакции."""
        if self._connection is not None or self._transaction is not None:
            raise RuntimeError("Transaction is already started.")

        self._logger.debug(
            "Start readonly='%s' transaction isolation_level='%s'.",
            readonly,
            isolation_level,
        )

        self._connection = await self._pool_clients.acquire()
        self._transaction = self._connection.transaction(
            isolation=isolation_level,
            readonly=readonly,
        )
        await self._transaction.start()

        self._logger.debug(
            "Transaction started: transaction_id=%s, "
            "transaction_state='%s', connection=%s.",
            self._transaction._id,
            self._transaction._state,
            id(self._connection),
        )

    async def commit(self) -> None:
        """Фиксирует текущую транзакцию."""
        if self._transaction is None:
            raise RuntimeError("Transaction is not started.")

        self._logger.debug(
            "Start commit transaction_id=%s, transaction_state='%s'.",
            self._transaction._id,
            self._transaction._state,
        )

        await self._transaction.commit()

        self._logger.debug(
            "Transaction committed: transaction_id=%s, transaction_state='%s'.",
            self._transaction._id,
            self._transaction._state,
        )

    async def rollback(self) -> None:
        """Откатывает текущую транзакцию."""
        if self._transaction is None:
            raise RuntimeError("Transaction is not started.")

        self._logger.debug(
            "Start rollback transaction_id='%s', transaction_state='%s'.",
            self._transaction._id,
            self._transaction._state,
        )

        await self._transaction.rollback()

        self._logger.debug(
            "Transaction rolled back: transaction_id='%s', transaction_state='%s'.",
            self._transaction._id,
            self._transaction._state,
        )

    async def execute_query(
        self,
        query: str,
        params: dict[str, Any] | None = None,
    ) -> list[Record]:
        """Выполняет SELECT-запрос и возвращает список строк."""
        if not self._connection:
            raise RuntimeError(
                "Cannot execute query outside of transaction.",
            )
        self._logger.debug(
            "Execute query='%s' with params='%s' by connection=%s",
            query,
            params,
            id(self._connection),
        )
        params = params or {}
        query_resp = await self._connection.fetch(
            query=query,
            **params,
        )
        self._logger.debug(
            "Executed query='%s' with params='%s' got resp='%s'.",
            query,
            params,
            [dict(record) for record in query_resp],
        )
        return query_resp  # type: ignore[no-any-return]

    async def execute_command(
        self,
        query: str,
        params: dict[str, Any] | None = None,
    ) -> str:
        """Выполняет INSERT/UPDATE/DELETE, возвращает количество затрагиваемых строк."""
        if not self._connection:
            raise RuntimeError(
                "Cannot execute query outside of transaction.",
            )
        self._logger.debug(
            "Execute query='%s' with params='%s' by connection=%s",
            query,
            params,
            id(self._connection),
        )
        params = params or {}
        query_resp = await self._connection.execute(
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

    async def close(self) -> None:
        """Освобождает connection обратно в connection pool."""
        if self._connection is None:
            self._transaction = None
            return

        self._logger.debug(
            "Release connection='%s' back to pool.",
            id(self._connection),
        )

        try:
            await self._pool_clients.release(self._connection)
        finally:
            self._connection = None
            self._transaction = None

        self._logger.debug("Connection released.")
