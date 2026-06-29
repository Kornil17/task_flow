import asyncio
import logging
from http import HTTPStatus
from typing import ClassVar

from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response


_logger = logging.getLogger("presentation")


class TimeoutMiddleware(BaseHTTPMiddleware):
    """Промежуточный слой ограничения времени обработки запроса."""

    _timeout: ClassVar[int]

    async def dispatch(
        self,
        request: Request,
        call_next: RequestResponseEndpoint,
    ) -> Response:
        """Ограничение времени обработки запроса."""
        try:
            async with asyncio.timeout(self._timeout):
                return await call_next(request)
        except TimeoutError:
            _logger.warning(
                "Request timed out: %s '%s' after %s",
                request.method,
                request.url.path,
                self._timeout,
            )
            return Response(
                status_code=HTTPStatus.REQUEST_TIMEOUT,
                content={"detail": "Request Timeout"},
            )
