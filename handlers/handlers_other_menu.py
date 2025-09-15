from aiogram import Router, F
from aiogram.filters import Command, or_f
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from keyboards.keyboards import kb_other_menu
from bot_session import KB_MENU, KB_OTHER_MENU
from bot_session import message_process_util
from bot_session import Form_Session
from handlers.handlers_menu import func_menu

other_menu_router = Router()

@other_menu_router.message(Form_Session.MAIN_MENU, or_f(Command("other_menu"), F.text == str(KB_MENU["other"])))
async def handle_menu_other(message: Message, state: FSMContext):
    await state.set_state(Form_Session.OTHER_MENU)
    await message.answer(message_process_util.get_message("other_menu"), reply_markup=kb_other_menu())

@other_menu_router.message(Form_Session.OTHER_MENU, F.text == str(KB_OTHER_MENU["back"]))
async def handle_menu_other_back(message: Message, state: FSMContext):
    await func_menu(message, state)

@other_menu_router.message(or_f(Command("snake"), F.text == str(KB_OTHER_MENU["snake"])))
async def handle_snake(message: Message):
    await message.answer(message_process_util.get_message("in_develop"), reply_markup=kb_other_menu())

@other_menu_router.message(or_f(Command("music"), F.text == str(KB_OTHER_MENU["music"])))
async def handle_snake(message: Message):
    await message.answer(message_process_util.get_message("in_develop"), reply_markup=kb_other_menu())