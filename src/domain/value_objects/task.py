from dataclasses import dataclass
from enum import StrEnum, unique
from typing import ClassVar

from src.domain.exceptions import (
    TaskContentInvalidError,
    TaskDeadlineInvalidError,
    TaskNameInvalidError,
    TaskStatusInvalidError,
)
from src.domain.value_objects import (
    DatetimeValueObject,
    IdValueObject,
    IntValueObject,
    StringValueObject,
    ValueObject,
)


@unique
class Status(StrEnum):
    """Статусы задачи."""

    CREATE = "create"
    IN_PROGRESS = "in_progress"
    IN_REVIEW = "in_review"
    DONE = "done"
    CANCEL = "cancel"
    ON_HOLD = "on_hold"


@dataclass(frozen=True, kw_only=True, slots=True)
class TaskID(IdValueObject[int]):
    """Идентификатор задачи."""


@dataclass(frozen=True, kw_only=True, slots=True)
class TaskName(StringValueObject):
    """Название задачи.."""

    _MIN_NAME_LENGTH: ClassVar[int] = 1
    _MAX_NAME_LENGTH: ClassVar[int] = 200

    def __post_init__(self) -> None:
        if len(self.value) < self._MIN_NAME_LENGTH:
            raise TaskNameInvalidError(
                f"Task name must be at least {self._MIN_NAME_LENGTH} character(s).",
            )
        if len(self.value) > self._MAX_NAME_LENGTH:
            raise TaskNameInvalidError(
                f"Task name must not exceed {self._MAX_NAME_LENGTH} characters.",
            )


@dataclass(frozen=True, kw_only=True, slots=True)
class TaskContent(StringValueObject):
    """Описание задачи."""

    _MAX_CONTENT_LENGTH: ClassVar[int] = 500

    def __post_init__(self) -> None:
        if len(self.value) > self._MAX_CONTENT_LENGTH:
            raise TaskContentInvalidError(
                "Content length must not exceed "
                f"{self._MAX_CONTENT_LENGTH} characters.",
            )


@dataclass(frozen=True, kw_only=True, slots=True)
class TaskStatusID(ValueObject[Status]):
    """Статус задачи."""

    def __post_init__(self) -> None:
        if not isinstance(self.value, Status):
            raise TaskStatusInvalidError("Status must be a valid Status enum value.")


@dataclass(frozen=True, kw_only=True, slots=True)
class TaskDeadlineDays(IntValueObject):
    """Срок выполнения задачи в днях."""

    _MIN_DEADLINE_DAYS: ClassVar[int] = 1
    _MAX_DEADLINE_DAYS: ClassVar[int] = 30

    def __post_init__(self) -> None:
        if self.value < self._MIN_DEADLINE_DAYS or self.value > self._MAX_DEADLINE_DAYS:
            raise TaskDeadlineInvalidError(
                f"Deadline days must be between {self._MIN_DEADLINE_DAYS} "
                f"and {self._MAX_DEADLINE_DAYS}.",
            )


@dataclass(frozen=True, kw_only=True, slots=True)
class TaskCreatedAt(DatetimeValueObject):
    """Дата создания задачи."""


@dataclass(frozen=True, kw_only=True, slots=True)
class TaskUpdatedAt(DatetimeValueObject):
    """Дата обновления задачи."""


@dataclass(frozen=True, kw_only=True, slots=True)
class TaskDeletedAt(DatetimeValueObject):
    """Дата удаления задачи."""
