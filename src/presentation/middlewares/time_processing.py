import logging
from time import perf_counter

from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response


_logger = logging.getLogger("presentation")


class TimeProcessingMiddleware(BaseHTTPMiddleware):
    """Промежуточный слой логирования времени обработки запроса."""

    async def dispatch(
        self,
        request: Request,
        call_next: RequestResponseEndpoint,
    ) -> Response:
        """Логирование времени обработки запроса."""
        start_time = perf_counter()
        response = await call_next(request)
        duration = perf_counter() - start_time

        _logger.debug(
            "Request processed: %s '%s' -> %s in %.2fs",
            request.method,
            request.url.path,
            response.status_code,
            duration,
        )
        return response
