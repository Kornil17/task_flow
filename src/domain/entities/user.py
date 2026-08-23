from dataclasses import dataclass

from src.domain.value_objects.user import (
    UserCreatedAt,
    UserDeletedAt,
    UserEmail,
    UserID,
    UserName,
    UserRole,
    UserSurname,
    UserUpdatedAt,
)


@dataclass(slots=True, frozen=True, kw_only=True)
class User:
    """Доменная модель пользователя."""

    id: UserID
    name: UserName
    surname: UserSurname
    role: UserRole
    email: UserEmail
    created_at: UserCreatedAt
    updated_at: UserUpdatedAt
    deleted_at: UserDeletedAt
