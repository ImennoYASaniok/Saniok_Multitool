from aiohttp import web

import asyncio
import os

from handlers.handlers_menu import menu_router
from handlers.handlers_other_menu import other_menu_router
from handlers.handler_send_message import send_message_router
from bot_session import dp, bot, set_commands
from db import db_session


async def start_bot():
    dp.include_router(menu_router)
    dp.include_router(other_menu_router)
    dp.include_router(send_message_router)
    await bot.delete_webhook(drop_pending_updates=True)
    await set_commands()
    await dp.start_polling(bot)

async def handle(request):
    return web.Response(text="Bot is running!")

app = web.Application()
app.router.add_get("/", handle)

if __name__ == "__main__":
    db_file = os.path.join(
        os.path.abspath(os.path.dirname(__file__)), 'db', 'db.sqlite'
    )
    db_session.my_global_init(os.environ.get('DATABASE_URI', db_file))

    port = int(os.environ.get("PORT", 10000))

    loop = asyncio.get_event_loop()
    loop.create_task(web._run_app(app, port=port, print=None))
    loop.run_until_complete(start_bot())