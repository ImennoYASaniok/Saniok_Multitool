from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from bot_session import ADMINS, KB_MENU, KB_SEND_MESSAGE, KB_OTHER_MENU, KB_SNAKE_PLAY, KB_SNAKE_MENU
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


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

def kb_message():
    kb_list = [
        [InlineKeyboardButton(text=KB_SEND_MESSAGE["cancel"]["text"], callback_data=KB_SEND_MESSAGE["cancel"]["command"])]
    ]
    return InlineKeyboardMarkup(inline_keyboard=kb_list)

def kb_snake_menu():
    kb_list = [
        [KeyboardButton(text=KB_SNAKE_MENU["play"]), KeyboardButton(text=KB_SNAKE_MENU["back"])]
    ]
    return ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Игра змейка"
    )

def kb_snake_play():
    kb_list = [
        [InlineKeyboardButton(text=KB_SNAKE_PLAY["back"]["text"], callback_data=KB_SNAKE_PLAY["back"]["command"]), InlineKeyboardButton(text=KB_SNAKE_PLAY["up"]["text"], callback_data=KB_SNAKE_PLAY["up"]["command"]), InlineKeyboardButton(text="ㅤ", callback_data="empty")],
        [InlineKeyboardButton(text=KB_SNAKE_PLAY["left"]["text"], callback_data=KB_SNAKE_PLAY["left"]["command"]), InlineKeyboardButton(text=KB_SNAKE_PLAY["right"]["text"], callback_data=KB_SNAKE_PLAY["right"]["command"])],
        [InlineKeyboardButton(text="ㅤ", callback_data="empty"), InlineKeyboardButton(text=KB_SNAKE_PLAY["down"]["text"], callback_data=KB_SNAKE_PLAY["down"]["command"]), InlineKeyboardButton(text="ㅤ", callback_data="empty")],
    ]
    return InlineKeyboardMarkup(inline_keyboard=kb_list)