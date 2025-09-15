from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from bot_session import ADMINS, KB_MENU, KB_SEND_MESSAGE, KB_OTHER_MENU


def kb_menu(user_id: int):
    kb_list = [
        [KeyboardButton(text=KB_MENU["send_message"]), KeyboardButton(text=KB_MENU["clear"])],
        [KeyboardButton(text=KB_MENU["info"]), KeyboardButton(text=KB_MENU["contacts"])],
        [KeyboardButton(text=KB_MENU["other"])]
    ]
    if user_id in ADMINS: kb_list[-1].append(KeyboardButton(text=KB_MENU["admin"]))
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Воспользуйтесь меню:"
    )
    return keyboard

def kb_send_message():
    kb_list = [
        [KeyboardButton(text=KB_SEND_MESSAGE["cancel"])],
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Письмо:"
    )
    return keyboard

def kb_other_menu():
    kb_list = [
        [KeyboardButton(text=KB_OTHER_MENU["music"]), KeyboardButton(text=KB_OTHER_MENU["snake"])],
        [KeyboardButton(text=KB_OTHER_MENU["back"])]
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Воспользуйтесь дополнительным меню:"
    )
    return keyboard