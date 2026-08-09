from asyncpg import create_pool
from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Configuration, Resource, Singleton

from src.infrastructure.persistence.db_client import PostgresDBClient
from src.infrastructure.persistence.db_transaction_manager import (
    PostgresDBTransactionManager,
)


class DBContainer(DeclarativeContainer):
    """Контейнер для создания и управления ресурсами БД."""

    config = Configuration()
    db_pool = Resource(
        create_pool,
        user=config.db_user,
        password=config.db_password,
        host=config.db_host,
        port=config.db_port,
        database=config.db_name,
        min_size=config.db_min_pool_size,
        max_size=config.db_max_pool_size,
    )
    db_client = Singleton(
        PostgresDBClient,
        _pool_clients=db_pool,
    )
    db_transaction_manager = Singleton(
        PostgresDBTransactionManager,
        _db_client=db_client,
    )
