from pydantic import ValidationError


class TaskInvalidError(ValidationError):
    """Некорректная задача (нарушены правила агрегата Task)."""


class TaskStatusInvalidError(TaskInvalidError):
    """Некорректный статус задачи."""


class TaskNameInvalidError(TaskInvalidError):
    """Некорректное название задачи."""


class TaskContentInvalidError(TaskInvalidError):
    """Некорректное описание задачи."""


class TaskDeadlineInvalidError(TaskInvalidError):
    """Некорректный срок выполнения задачи."""
