from aiogram import F, Router
from aiogram.filters import CommandStart, Command, or_f
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from keyboards.keyboards import kb_menu, KB_MENU
from consts import MESSAGE_INFO, MESSAGE_CONTACTS
from bot_session import bot
from bot_session import message_process_util
from bot_session import Form_Session

import asyncio

menu_router = Router()

async def func_menu(message: Message, state: FSMContext):
    await state.set_state(Form_Session.MAIN_MENU)
    await message.answer(message_process_util.get_message("menu"), reply_markup=kb_menu(message.from_user.id))

@menu_router.message(CommandStart())
async def handle_start(message: Message, state: FSMContext):
    await message.answer(message_process_util.get_message("hello").format(message.from_user.first_name))
    await func_menu(message, state)

@menu_router.message(or_f(Command("info"), F.text == str(KB_MENU["info"])))
async def handle_info(message: Message):
    await message.answer(MESSAGE_INFO, reply_markup=kb_menu(message.from_user.id))

@menu_router.message(or_f(Command("contacts"), F.text == str(KB_MENU["contacts"])))
async def handle_contacts(message: Message):
    await message.answer(MESSAGE_CONTACTS, reply_markup=kb_menu(message.from_user.id))

@menu_router.message(or_f(Command("clear"), F.text == str(KB_MENU["clear"])))
async def handle_clear(message: Message, state: FSMContext):
    chat_id = message.chat.id
    curr_message_id = message.message_id
    count_message = 0

    load_message_text = message_process_util.get_message("load_clear") + " "
    load_message = await message.answer(load_message_text)
    animation_load_message = asyncio.create_task(load_clear(load_message, chat_id, load_message_text))
    for i in range(1, 200):
        try:
            await bot.delete_message(chat_id, curr_message_id)
            count_message += 1
        except:
            pass
        curr_message_id = curr_message_id - 1
    if animation_load_message:
        animation_load_message.cancel()

    await load_message.delete()
    await message.answer(message_process_util.get_message("clear").format(count_message))
    await func_menu(message, state)

async def load_clear(load_message, chat_id, load_message_text):
    try:
        ind_load_animation = 0
        load_animation = ["*", "**", "***"]
        for i in range(1, 200):
            await asyncio.sleep(1)
            try:
                await bot.edit_message_text(
                    chat_id=chat_id,
                    message_id=load_message.message_id,
                    text=load_message_text + load_animation[ind_load_animation]
                )
                ind_load_animation += 1
                if ind_load_animation >= len(load_animation): ind_load_animation = 0
            except Exception as e:
                print(f"Ошибка при обновлении сообщения: {e}")
    except asyncio.CancelledError:
        pass
        # print("❌ Отображение загрузки отменено")
