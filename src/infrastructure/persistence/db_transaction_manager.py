from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from dataclasses import dataclass, field
from logging import Logger, getLogger

from asyncpg import InterfaceError

from src.application.interfaces.persistence import IsolationLevel
from src.infrastructure.persistence.db_client import PostgresDBClient


_logger = getLogger("infrastructure")


@dataclass(frozen=True, slots=True, kw_only=True)
class PostgresDBTransactionManager:
    """
    Менеджер жизненного цикла PostgreSQL-транзакции.

    Transaction Manager отвечает только за управление жизненным циклом транзакции:
    1. начинает транзакцию;
    2. передаёт transaction-scoped DB client вызывающему коду;
    3. выполняет commit при успешном завершении;
    4. выполняет rollback при исключении;
    5. в любом случае освобождает connection обратно в pool.
    """

    _db_client: PostgresDBClient
    _logger: Logger = field(init=False, default=_logger)

    @asynccontextmanager
    async def start(
        self,
        *,
        isolation_level: IsolationLevel | None = None,
        readonly: bool = False,
    ) -> AsyncGenerator[PostgresDBClient]:
        """Запускает транзакцию и возвращает DB client."""
        self._logger.info(
            "Start readonly='%s' transaction isolation_level='%s'.",
            readonly,
            isolation_level,
        )

        await self._db_client.begin(
            isolation_level=isolation_level,
            readonly=readonly,
        )

        try:
            self._logger.debug(
                "Transaction client is ready.",
            )
            yield self._db_client

            await self._db_client.commit()
            self._logger.debug(
                "Transaction successfully committed.",
            )
        except InterfaceError:
            self._logger.exception(
                "Transaction failed. Start rollback.",
            )
            await self._db_client.rollback()
        finally:
            await self._db_client.close()
            self._logger.debug(
                "DB client successfully closed.",
            )
