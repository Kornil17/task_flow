import re
from dataclasses import dataclass
from enum import StrEnum, unique
from typing import ClassVar

from src.domain.exceptions import (
    UserEmailInvalidError,
    UserNameInvalidError,
    UserRoleInvalidError,
    UserSurnameInvalidError,
)
from src.domain.value_objects.common import (
    DatetimeValueObject,
    IdValueObject,
    StringValueObject,
    ValueObject,
)


@unique
class Role(StrEnum):
    """Роли пользователя."""

    ADMIN = "admin"
    USER = "user"
    GUEST = "guest"


@dataclass(frozen=True, kw_only=True, slots=True)
class UserID(IdValueObject[int]):
    """ID пользователя."""


@dataclass(frozen=True, kw_only=True, slots=True)
class UserName(StringValueObject):
    """Имя пользователя.."""

    _MIN_NAME_LENGTH: ClassVar[int] = 1
    _MAX_NAME_LENGTH: ClassVar[int] = 200

    def __post_init__(self) -> None:
        if len(self.value) < self._MIN_NAME_LENGTH:
            raise UserNameInvalidError(
                f"User name must be at least {self._MIN_NAME_LENGTH} character(s).",
            )
        if len(self.value) > self._MAX_NAME_LENGTH:
            raise UserNameInvalidError(
                f"User name must not exceed {self._MAX_NAME_LENGTH} characters.",
            )


@dataclass(frozen=True, kw_only=True, slots=True)
class UserSurname(StringValueObject):
    """Фамилия пользователя."""

    _MIN_SURNAME_LENGTH: ClassVar[int] = 1
    _MAX_SURNAME_LENGTH: ClassVar[int] = 200

    def __post_init__(self) -> None:
        if len(self.value) < self._MIN_SURNAME_LENGTH:
            raise UserSurnameInvalidError(
                "User surname must be at least "
                f"{self._MIN_SURNAME_LENGTH} character(s).",
            )
        if len(self.value) > self._MAX_SURNAME_LENGTH:
            raise UserSurnameInvalidError(
                f"User surname must not exceed {self._MAX_SURNAME_LENGTH} characters.",
            )


@dataclass(frozen=True, kw_only=True, slots=True)
class UserRole(ValueObject[Role]):
    """Роль пользователя."""

    def __post_init__(self) -> None:
        if not isinstance(self.value, Role):
            raise UserRoleInvalidError("Role must be a valid Role enum value.")


@dataclass(frozen=True, kw_only=True, slots=True)
class UserEmail(StringValueObject):
    """Почта пользователя."""

    _EMAIL_REGEX: ClassVar[str] = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

    def __post_init__(self) -> None:
        if not self.value:
            raise UserEmailInvalidError("Email cannot be empty.")

        if not re.fullmatch(self._EMAIL_REGEX, self.value):
            raise UserEmailInvalidError(
                f"Email '{self.value}' is invalid.",
            )


@dataclass(frozen=True, kw_only=True, slots=True)
class UserCreatedAt(DatetimeValueObject):
    """Дата создания пользователя."""


@dataclass(frozen=True, kw_only=True, slots=True)
class UserUpdatedAt(DatetimeValueObject):
    """Дата обновления пользователя."""


@dataclass(frozen=True, kw_only=True, slots=True)
class UserDeletedAt(DatetimeValueObject):
    """Дата удаления пользователя."""
