from dataclasses import dataclass
from datetime import datetime

from src.domain.exceptions import (
    InvalidDatetimeError,
    InvalidIdError,
    InvalidIntError,
    InvalidStringError,
)


@dataclass(slots=True, frozen=True, kw_only=True)
class ValueObject[T]:
    """Базовый класс для реализации VO."""

    value: T

    def __str__(self) -> str:
        return str(self.value)


@dataclass(frozen=True, kw_only=True, slots=True)
class IdValueObject[T](ValueObject[T]):
    def __post_init__(self) -> None:
        if not isinstance(self.value, int):
            raise InvalidIntError("Value must be an integer.")
        if self.value <= 0:
            raise InvalidIdError("ID must be greater than 0.")


@dataclass(frozen=True, kw_only=True, slots=True)
class StringValueObject(ValueObject[str]):
    def __post_init__(self) -> None:
        if not isinstance(self.value, str):
            raise InvalidStringError("Value must be a string.")

        if len(self.value) == 0:
            raise InvalidStringError("String must not be empty.")


@dataclass(frozen=True, kw_only=True, slots=True)
class IntValueObject(ValueObject[int]):
    def __post_init__(self) -> None:
        if not isinstance(self.value, int):
            raise InvalidIntError("Value must be an integer.")


@dataclass(frozen=True, kw_only=True, slots=True)
class DatetimeValueObject(ValueObject[datetime]):
    def __post_init__(self) -> None:
        if not isinstance(self.value, datetime):
            raise InvalidDatetimeError("Value must be a datetime.")

        if self.value.tzinfo is None:
            raise InvalidDatetimeError("DateTime must be timezone-aware.")
