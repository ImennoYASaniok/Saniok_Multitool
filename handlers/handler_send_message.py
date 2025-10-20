from aiogram import Router, F
from aiogram.filters import Command, or_f
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from db.crud import get_user, create_user, create_message
from keyboards.keyboards import kb_message, KB_MENU, KB_SEND_MESSAGE, KB_MESSAGES_MENU
from bot_session import message_process_util
from bot_session import Form_Session
from handlers.handlers_other_menu import func_menu

send_message_router = Router()

@send_message_router.message(or_f(Command("messages"), F.text == str(KB_MENU["messages"])))
async def handle_menu_message(message: Message, state: FSMContext):
    await state.set_state(Form_Session.MESSAGES_MENU)
    await message.answer(message_process_util.get_message("messages_menu"), reply_markup=kb_message())


@send_message_router.message(or_f(Command("send_message"), F.text == str(KB_MESSAGES_MENU["send_message"])))
async def handle_typing_message(message: Message, state: FSMContext):
    await state.set_state(Form_Session.SENDING)
    await message.answer(message_process_util.get_message("send_message"), reply_markup=kb_message())

@send_message_router.callback_query(Form_Session.SENDING, lambda x: x.data == str(KB_SEND_MESSAGE["cancel"]["command"]))
async def handle_cancel_message(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Form_Session.MAIN_MENU)
    await callback.message.answer(message_process_util.get_message("cancel"))
    await func_menu(callback.message, state)
    await callback.answer()

@send_message_router.message(Form_Session.SENDING)
async def handle_send_message(message: Message, state: FSMContext):
    curr_user_id = str(message.from_user.id)
    user = await get_user(curr_user_id)
    if not user:
        user = await create_user(curr_user_id)

    await create_message(user.id, message.message_id, message.text)

    await state.set_state(Form_Session.MAIN_MENU)
    await message.answer(message_process_util.get_message("success_get_message"))
    await func_menu(message, state)


@send_message_router.message(or_f(Command("view_message"), F.text == str(KB_MESSAGES_MENU["view_message"])))
async def handle_view_message(message: Message, state: FSMContext):
    curr_user_id = str(message.from_user.id)
    user = await get_user(curr_user_id)
    if not user:
        user = await create_user(curr_user_id)

    await create_message(user.id, message.message_id, message.text)

    await state.set_state(Form_Session.MAIN_MENU)
    await message.answer(message_process_util.get_message("success_get_message"))
    await func_menu(message, state)