import asyncio

from handlers.handlers_menu import start_router
from bot_session import dp, bot, set_commands

from db import db_session
import os

async def start_bot():
    dp.include_router(start_router)
    await bot.delete_webhook(drop_pending_updates=True)
    await set_commands()
    await dp.start_polling(bot)

if __name__ == "__main__":
    db_file = os.path.join(
        os.path.abspath(os.path.dirname(__file__)), 'db', 'kon.sqlite'
    )
    db_session.my_global_init(os.environ.get('DATABASE_URI', f'{db_file}'))
    asyncio.run(start_bot())