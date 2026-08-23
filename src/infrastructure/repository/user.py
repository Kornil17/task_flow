from dataclasses import dataclass, field
from logging import Logger, getLogger
from typing import Any

from asyncpg import Record

from src.application.ports.persistence import IDBTransactionManager
from src.domain.entities.user import User
from src.domain.value_objects.user import UserID


_logger = getLogger("infrastructure")


@dataclass(slots=True, frozen=True, kw_only=True)
class UserRepository:
    """Репозиторий для работы с доменной сущностью 'Пользователь'."""

    _transaction_manager: IDBTransactionManager[
        dict[str, Any],
        list[Record],
        str,
    ]
    _table_name: str = field(default="users")
    _logger: Logger = field(default=_logger)

    async def get(self, entity_id: UserID) -> User | None:
        """Получение пользователя по уникальному ID."""
        async with self._transaction_manager.start() as _db_client:
            data = await _db_client.execute_query(
                query="""
                    SELECT *
                    FROM :table_name
                    WHERE id=:user_id
                """,
                params={"table_name": self._table_name, "user_id": entity_id},
            )

        self._logger.debug(
            "Получили данные=%s по запросу пользователя с ID=%s",
            data,
            entity_id,
        )
        if not data:
            self._logger.info("Пользователь с ID=%s отсуствует в БД.", entity_id)
            return None

        self._logger.info("Пользователь с ID=%s, получен.", entity_id)
        return User(**data[0])
