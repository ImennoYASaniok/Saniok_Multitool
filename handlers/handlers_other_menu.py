from aiogram import Router, F
from aiogram.filters import Command, or_f
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from keyboards.keyboards import kb_main
from bot_session import KB_MENU, KB_OTHER_MENU

from handlers.handlers_menu import start_router, message_process_util, Form_Session

async def func_menu(message: Message, state: FSMContext):
    await state.set_state(Form_Session.MAIN_MENU)
    await message.answer(message_process_util.get_message("menu"), reply_markup=kb_main(message.from_user.id))

@start_router.message(Form_Session.OTHER_MENU, or_f(Command("other_menu"), F.text == str(KB_MENU["other"])))
async def handle_menu_other(message: Message, state: FSMContext):
    await state.set_state(Form_Session.OTHER_MENU)
    await message.answer(message_process_util.get_message("other_menu"), reply_markup=kb_main(message.from_user.id))

@start_router.message(Form_Session.OTHER_MENU, F.text == str(KB_OTHER_MENU["back"]))
async def handle_menu_other_back(message: Message, state: FSMContext):
    await func_menu(message, state)

@start_router.message(or_f(Command("snake"), F.text == str(KB_OTHER_MENU["snake"])))
async def handle_snake(message: Message):
    await message.answer(message_process_util.get_message("in_develop"))