from pydantic import ValidationError


class CommentInvalidError(ValidationError):
    """Некорректный комментарий (нарушены правила агрегата Comment)."""


class CommentContentInvalidError(CommentInvalidError):
    """Некорректное описание комментария."""
