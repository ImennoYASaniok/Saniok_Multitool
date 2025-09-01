from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from message_process import MessageProcess

message_process_util = MessageProcess()

start_router = Router()

@start_router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(message_process_util.get_message("/start").format(message.from_user.first_name))