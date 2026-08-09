from collections.abc import Callable
from functools import wraps
from inspect import iscoroutinefunction
from logging import getLogger
from time import perf_counter
from typing import Any


_logger = getLogger("infrastructure")


def measure_time(
    func: Callable[..., Any],
) -> Callable[..., Any]:
    """Декоратор для измерения времени выполнения функций."""
    if iscoroutinefunction(func):

        @wraps(func)
        async def async_wrapper(
            *args: Any,
            **kwargs: Any,
        ) -> Any:
            """Выполняет асинхронную функцию с измерением времени."""
            start = perf_counter()
            try:
                return await func(*args, **kwargs)
            finally:
                _logger.debug(
                    "[PERF] function='%s' elapsed=%.6fs",
                    func.__qualname__,
                    perf_counter() - start,
                )

        return async_wrapper

    @wraps(func)
    def sync_wrapper(
        *args: Any,
        **kwargs: Any,
    ) -> Any:
        """Выполняет синхронную функцию с измерением времени."""
        start = perf_counter()
        try:
            return func(*args, **kwargs)
        finally:
            elapsed = perf_counter() - start
            _logger.debug(
                "[PERF] function='%s' elapsed=%.6fs",
                func.__qualname__,
                elapsed,
            )

    return sync_wrapper
