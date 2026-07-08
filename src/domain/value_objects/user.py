from dataclasses import dataclass

from src.domain.value_objects import IdValueObject


@dataclass(frozen=True, kw_only=True, slots=True)
class UserID(IdValueObject[int]):
    """ID пользователя."""
