import asyncio
import logging

from dependency_injector.wiring import Provide, inject

from di.application import ApplicationContainer, application_container
from src.presentation.app import Application


_logger = logging.getLogger("presentation")


@inject
async def main(
    application: Application = Provide[ApplicationContainer.application],
) -> None:
    """Входная точка в приложение."""
    _logger.debug("Start service.")
    await application.run()


application_container.wire(modules=[__name__])


if __name__ == "__main__":
    asyncio.run(main())
