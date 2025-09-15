import logging
from aiohttp import web

import asyncio
import os

from handlers.handlers_menu import menu_router
from handlers.handlers_other_menu import other_menu_router
from handlers.handler_send_message import send_message_router
from bot_session import dp, bot, set_commands
from db import db_session

LOG_FILE = "server.log"
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

def handle_async_exception(loop, context):
    msg = context.get("exception", context["message"])
    logger.exception(f"Необработанное исключение в asyncio: {msg}")

async def start_bot():
    if menu_router.parent_router is None:
        dp.include_router(menu_router)
    if other_menu_router.parent_router is None:
        dp.include_router(other_menu_router)
    if send_message_router.parent_router is None:
        dp.include_router(send_message_router)
    await bot.delete_webhook(drop_pending_updates=True)
    await set_commands()
    try:
        await dp.start_polling(bot, skip_updates=True)
    except Exception as e:
        print("Ошибка бота:", e)

async def handle(request):
    return web.Response(text="Bot is running!")

if __name__ == "__main__":
    db_file = os.path.join(
        os.path.abspath(os.path.dirname(__file__)), 'db', 'db.sqlite'
    )
    db_session.my_global_init(os.environ.get('DATABASE_URI', db_file))

    port = int(os.environ.get("PORT", 10000))
    app = web.Application()
    app.router.add_get("/", handle)

    loop = asyncio.get_event_loop()
    loop.set_exception_handler(handle_async_exception)
    loop.create_task(web._run_app(app, port=port, print=None))
    try:
        loop.run_until_complete(start_bot())
    except Exception:
        logger.exception("Главный цикл сервера упал:")