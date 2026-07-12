from typing import Protocol


class IEntityRepository[Entity, EntityID](Protocol):
    """Декларация контракта слоя репозитория."""

    async def get(self, entity_id: EntityID) -> Entity | None:
        """Получение сущности по ID."""

    async def save(self, entity: Entity) -> None:
        """Сохранение сущности."""


class IUserRepository[User, UserID](IEntityRepository[User, UserID]):
    """Декларация контракта слоя репозитория для сущности 'Пользователь'."""
