import asyncio
import logging
from http import HTTPStatus
from typing import ClassVar

from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response

from src.infrastructure.configuration import settings


_logger = logging.getLogger("presentation")


class TimeoutMiddleware(BaseHTTPMiddleware):
    """Промежуточный слой ограничения времени обработки запроса."""

    _request_timeout: ClassVar[float] = settings.request_timeout

    async def dispatch(
        self,
        request: Request,
        call_next: RequestResponseEndpoint,
    ) -> Response:
        """Ограничение времени обработки запроса."""
        try:
            async with asyncio.timeout(self._request_timeout):
                return await call_next(request)
        except TimeoutError:
            _logger.warning(
                "Request timed out: %s '%s' after %s",
                request.method,
                request.url.path,
                self._request_timeout,
            )
            return Response(
                status_code=HTTPStatus.REQUEST_TIMEOUT,
                content={"detail": "Request Timeout"},
            )
