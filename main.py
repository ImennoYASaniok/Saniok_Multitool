import logging
from aiohttp import web
import asyncio
import os
from decouple import config

from handlers.handlers_menu import menu_router
from handlers.handlers_other_menu import other_menu_router
from handlers.handler_send_message import send_message_router
from handlers.handler_snake import snake_router
from bot_session import dp, bot, set_commands
from consts import TYPE_TOKEN
from db.db_session import db_init

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

def include_routers():
    if menu_router.parent_router is None:
        dp.include_router(menu_router)
    if other_menu_router.parent_router is None:
        dp.include_router(other_menu_router)
    if send_message_router.parent_router is None:
        dp.include_router(send_message_router)
    if snake_router.parent_router is None:
        dp.include_router(snake_router)

async def other_actions():
    await set_commands()
    logger.info("Запуск и преднастройка бота прошла успешно")

async def start_bot(app=None):
    await db_init()
    include_routers()

    logger.info("Запускается основной бот")
    await bot.set_webhook(
        url=config('WEBHOOK_URL'),
        drop_pending_updates=True
    )
    logger.info("Webhook запущен")

    await other_actions()

async def start_extra_bot(app=None):
    await db_init()
    include_routers()

    logger.info("Запускается дополнительный бот")
    await bot.delete_webhook(drop_pending_updates=True)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

    await other_actions()


async def shutdown_bot(app):
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

async def handle_ping(request):
    return web.Response(text="OK")

if __name__ == "__main__":
    if TYPE_TOKEN == "TOKEN":
        logger.info("http порт поднимается")
        port = int(os.environ.get('PORT', 8080))
        app = web.Application()
        app.router.add_post("/webhook", handle_webhook)
        app.on_startup.append(start_bot)
        app.on_shutdown.append(shutdown_bot)
        app.router.add_get("/", handle_ping)
        web.run_app(app, host='0.0.0.0', port=port)
    elif TYPE_TOKEN == "EXTRA_TOKEN":
        logger.info("Бот работает локально на long_polling")
        asyncio.run(start_extra_bot())
    else:
        raise RuntimeError("Токен не найден")
    logger.info("Бот полностью функционирует")