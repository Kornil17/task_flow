from dataclasses import dataclass

from src.domain.value_objects.comment import (
    CommentContent,
    CommentCreatedAt,
    CommentDeletedAt,
    CommentID,
    CommentUpdatedAt,
)
from src.domain.value_objects.task import TaskID
from src.domain.value_objects.user import UserID


@dataclass(slots=True, frozen=True, kw_only=True)
class Comment:
    """Доменная модель комментария."""

    id: CommentID
    content: CommentContent
    user_id: UserID
    task_id: TaskID
    created_at: CommentCreatedAt
    updated_at: CommentUpdatedAt
    deleted_at: CommentDeletedAt
