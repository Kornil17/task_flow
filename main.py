import asyncio
import logging


_logger = logging.getLogger(__name__)


async def main():
    _logger.info("Start service.")


if __name__ == "__main__":
    asyncio.run(main())
