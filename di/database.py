from asyncpg import create_pool
from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Configuration, Resource


class DBContainer(DeclarativeContainer):
    """Контейнер для создания и управления ресурсами БД."""

    config = Configuration()
    db_pool = Resource(
        create_pool,
        dsn=f"postgres://{config.db_user}:{config.db_password}@{config.db_host}:{config.db_port}/{config.db_name}",
        min_size=config.db_min_pool_size,
        max_size=config.db_max_pool_size,
        max_inactive_connection_lifetime=config.db_max_connection_life_time,
    )
