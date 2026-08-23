from dataclasses import dataclass

from src.domain.value_objects.task import (
    TaskContent,
    TaskCreatedAt,
    TaskDeadlineDays,
    TaskDeletedAt,
    TaskID,
    TaskName,
    TaskStatusID,
    TaskUpdatedAt,
)
from src.domain.value_objects.user import UserID


@dataclass(slots=True, frozen=True, kw_only=True)
class Task:
    """Доменная модель задачи."""

    id: TaskID
    name: TaskName
    content: TaskContent
    status_id: TaskStatusID
    deadline_days: TaskDeadlineDays
    create_user_id: UserID
    executor_user_id: UserID
    created_at: TaskCreatedAt
    updated_at: TaskUpdatedAt
    deleted_at: TaskDeletedAt
