from pydantic import ValidationError


class UserInvalidError(ValidationError):
    """Некорректный пользователь (нарушены правила агрегата User)."""


class UserNameInvalidError(UserInvalidError):
    """Некорректное имя пользователя."""


class UserEmailInvalidError(UserNameInvalidError):
    """Некорректная почта пользователя."""


class UserRoleInvalidError(UserNameInvalidError):
    """Некорректная роль пользователя."""


class UserSurnameInvalidError(UserNameInvalidError):
    """Некорректная фамилия пользователя."""
