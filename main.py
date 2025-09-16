import logging

import asyncio
import os

from aiohttp import web

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

async def start_bot():
    if menu_router.parent_router is None:
        dp.include_router(menu_router)
    if other_menu_router.parent_router is None:
        dp.include_router(other_menu_router)
    if send_message_router.parent_router is None:
        dp.include_router(send_message_router)

    await bot.set_webhook(
        url=os.environ["WEBHOOK_URL"],
        drop_pending_updates=True
    )
    await set_commands()
    logger.info("Webhook запущен")

async def shutdown_bot():
    logger.info("Webhook выключается и сессия закрывается")
    await bot.delete_webhook()
    await bot.session.close()

async def handle_webhook(request: web.Request):
    try:
        data = await request.json()
        await dp.feed_webhook_update(bot, data)
        return web.Response()
    except Exception as e:
        logger.exception(f"Ошибка запуска webhook: {e}")
        return web.Response(status=500)

if __name__ == "__main__":
    db_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'db', 'db.sqlite')
    db_session.my_global_init(os.environ.get('DATABASE_URI', db_file))

    port = int(os.environ.get('PORT', 8080))
    app = web.Application()
    app.router.add_post("/webhook", handle_webhook)
    app.on_startup.append(start_bot)
    app.on_shutdown.append(shutdown_bot)
    web.run_app(app, host='0.0.0.0', port=port)