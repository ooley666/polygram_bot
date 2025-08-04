import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.types import Update


from bot.handlers.base import router_main
from bot.handlers.event_tracking_handlers import set_bot_reference

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = os.getenv("BOT_TOKEN_TEST")

async def log_update_type(update: Update, bot: Bot):
    logger.info(f"Received update type: {update.model_dump().keys()}")


async def main():
    bot = Bot(token=TOKEN)
    set_bot_reference(bot)
    dp = Dispatcher()

    # Register global update handler for logging
    dp.update.register(log_update_type, flags={"log_only": True})

    # Register other routers/handlers here
    dp.include_router(router_main)

    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")