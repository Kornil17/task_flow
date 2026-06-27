import asyncio
import logging

from src.presentation.app import Application


_logger = logging.getLogger(__name__)


async def main():
    _logger.debug("Start service.")
    application = Application()
    await application.run()


if __name__ == "__main__":
    asyncio.run(main())
