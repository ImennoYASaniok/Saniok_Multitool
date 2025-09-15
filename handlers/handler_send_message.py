from aiogram import Router, F
from aiogram.filters import Command, or_f
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from keyboards.keyboards import kb_send_message
from bot_session import KB_MENU, KB_SEND_MESSAGE

from handlers.handlers_menu import start_router, message_process_util, Form_Session
from handlers.handlers_other_menu import func_menu

@start_router.message(or_f(Command("send_message"), F.text == str(KB_MENU["send_message"])))
async def handle_typing_message(message: Message, state: FSMContext):
    await state.set_state(Form_Session.SENDING)
    await message.answer(message_process_util.get_message("send_message"), reply_markup=kb_send_message())

@start_router.message(Form_Session.SENDING, F.text == str(KB_MENU["send_message"]))
async def handle_cancel_message(message: Message, state: FSMContext):
    print("Письмо отменено")
    await state.set_state(Form_Session.MAIN_MENU)
    await message.answer(message_process_util.get_message("cancel"))
    await func_menu(message, state)

@start_router.message(Form_Session.SENDING)
async def handle_send_message(message: Message, state: FSMContext):
    print(message.text)
    await state.set_state(Form_Session.MAIN_MENU)
    await message.answer(message_process_util.get_message("success_get_message"))
    await func_menu(message, state)