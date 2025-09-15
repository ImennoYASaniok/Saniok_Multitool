from aiogram import Router, F
from aiogram.filters import Command, or_f
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from db.db_session import create_session
from keyboards.keyboards import kb_send_message
from bot_session import KB_MENU, KB_SEND_MESSAGE
from bot_session import message_process_util
from bot_session import Form_Session
from handlers.handlers_other_menu import func_menu
from db.models import Messages as Model_Messages, Users

send_message_router = Router()

@send_message_router.message(or_f(Command("send_message"), F.text == str(KB_MENU["send_message"])))
async def handle_typing_message(message: Message, state: FSMContext):
    await state.set_state(Form_Session.SENDING)
    await message.answer(message_process_util.get_message("send_message"), reply_markup=kb_send_message())

@send_message_router.message(Form_Session.SENDING, F.text == str(KB_MENU["send_message"]))
async def handle_cancel_message(message: Message, state: FSMContext):
    print("Письмо отменено")
    await state.set_state(Form_Session.MAIN_MENU)
    await message.answer(message_process_util.get_message("cancel"))
    await func_menu(message, state)

@send_message_router.message(Form_Session.SENDING)
async def handle_send_message(message: Message, state: FSMContext):
    session = create_session()
    curr_user_tg_id = message.from_user.id
    filter_user_tg_id = list(map(lambda row: row.id, filter(lambda row: curr_user_tg_id == row.id_tg, session.query(Users).all())))
    if len(filter_user_tg_id) > 0:
        id_user = filter_user_tg_id[0]
    else:
        new_user = Users(id_tg=curr_user_tg_id)
        session.add(new_user)
        session.commit()
        id_user = new_user.id
    new_message = Model_Messages(
        id_user=id_user,
        id_message = message.message_id,
        text_message = message.text
    )
    session.add(new_message)
    session.commit()

    await state.set_state(Form_Session.MAIN_MENU)
    await message.answer(message_process_util.get_message("success_get_message"))
    await func_menu(message, state)