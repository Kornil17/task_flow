class DomainError(Exception):
    """Базовый класс для всех доменных ошибок."""


class ValidationError(DomainError):
    """Базовый класс для ошибок валидации доменных значений."""


class InvalidValueError(ValidationError):
    """Некорректное значение."""


class InvalidIdError(InvalidValueError):
    """Некорректный идентификатор."""


class InvalidStringError(InvalidValueError):
    """Некорректная строка."""


class InvalidIntError(InvalidValueError):
    """Некорректное целое число."""


class InvalidDatetimeError(InvalidValueError):
    """Некорректная дата."""
