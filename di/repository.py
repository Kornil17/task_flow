from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Configuration, DependenciesContainer

from src.infrastructure.repository.user import UserRepository


class RepositoryContainer(DeclarativeContainer):
    """Контейнер для создания репозиториев работы с доменными моделями."""

    config = Configuration()
    database = DependenciesContainer()

    user_repo = UserRepository(
        _transaction_manager=database.db_transaction_manager,
    )
