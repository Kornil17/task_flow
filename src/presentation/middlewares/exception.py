import logging
from http import HTTPStatus

from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response


_logger = logging.getLogger("presentation")


class ExceptionMiddleware(BaseHTTPMiddleware):
    """Промежуточный слой отлавливания непредвиденных ошибок при обработке запроса."""

    async def dispatch(
        self,
        request: Request,
        call_next: RequestResponseEndpoint,
    ) -> Response:
        """Отлавливание непредвиденных ошибок при обработке запроса."""
        try:
            return await call_next(request)
        except Exception:
            _logger.exception(
                "Unhandled error: %s %s",
                request.method,
                request.url.path,
            )
            return Response(
                status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
                content={"detail": "Internal Server Error"},
            )
