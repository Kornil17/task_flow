from dataclasses import dataclass
from typing import ClassVar

from src.domain.exceptions import CommentContentInvalidError
from src.domain.value_objects.common import (
    DatetimeValueObject,
    IdValueObject,
    StringValueObject,
)


@dataclass(frozen=True, kw_only=True, slots=True)
class CommentID(IdValueObject[int]):
    """Идентификатор комментария."""


@dataclass(frozen=True, kw_only=True, slots=True)
class CommentContent(StringValueObject):
    """Содержимое комментария."""

    _MIN_CONTENT_LENGTH: ClassVar[int] = 1
    _MAX_CONTENT_LENGTH: ClassVar[int] = 2000

    def __post_init__(self) -> None:
        if len(self.value) < self._MIN_CONTENT_LENGTH:
            raise CommentContentInvalidError(
                "Comment content must be at least "
                f"{self._MIN_CONTENT_LENGTH} character(s).",
            )
        if len(self.value) > self._MAX_CONTENT_LENGTH:
            raise CommentContentInvalidError(
                "Comment content must not exceed "
                f"{self._MAX_CONTENT_LENGTH} characters.",
            )


@dataclass(frozen=True, kw_only=True, slots=True)
class CommentCreatedAt(DatetimeValueObject):
    """Дата создания комментария."""


@dataclass(frozen=True, kw_only=True, slots=True)
class CommentUpdatedAt(DatetimeValueObject):
    """Дата обновления комментария."""


@dataclass(frozen=True, kw_only=True, slots=True)
class CommentDeletedAt(DatetimeValueObject):
    """Дата удаления комментария."""
