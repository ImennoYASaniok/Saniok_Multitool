from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from bot_session import ADMINS, KB_MENU, KB_SEND_MESSAGE, KB_OTHER_MENU, KB_SNAKE_PLAY, KB_SNAKE_MENU, KB_SNAKE_SETTINGS, KB_DINO_MENU, KB_DINO_PLAY, KB_DINO_SETTINGS
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class Button:
    def __init__(self, text, command):
        self.text = text
        self.command = command
        self.button = self.init_button()

    def init_button(self) -> InlineKeyboardButton:
        return InlineKeyboardButton(text=self.get_text(), callback_data=self.command)

    def get_text(self) -> str:
        return self.text

class Button_Bool(Button):
    def __init__(self, text: str, value: bool, command: str):
        self.value = value
        self.output_value = {0: "❌", 1: "✅"}
        super().__init__(text, command)

    def change_value(self):
        self.value = not self.value
        self.button = self.init_button()

    def get_text(self) -> str:
        return f"{self.text} [{self.output_value[self.value]}]"

    def get_value(self) -> bool:
        return self.value

class Button_Choose(Button):
    def __init__(self, text: str, type: str, type_value: dict, command: str):
        self.type = type
        self.type_value = type_value
        self.init_type()
        super().__init__(text, command)

    def init_type(self):
        list_types = list(self.type_value.keys())
        if self.type not in list_types:
            self.type = list_types[0]

    def change_type(self):
        list_types = list(self.type_value.keys())
        new_type_ind = list_types.index(self.type) + 1
        new_type_ind = 0 if new_type_ind >= len(list_types) else new_type_ind
        self.type = list_types[new_type_ind]
        self.button = self.init_button()

    def get_text(self) -> str:
        return f"{self.text} [{self.type}]"

    def get_value(self):
        return self.type_value[self.type]

class Buttons:
    def __init__(self, buttons: dict):
        self.buttons = buttons

    def get_keyboard(self) -> InlineKeyboardMarkup:
        return InlineKeyboardMarkup(inline_keyboard=list(map(lambda button: [button.button], self.buttons.values())))


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
        [KeyboardButton(text=KB_SNAKE_MENU["back"]), KeyboardButton(text=KB_SNAKE_MENU["play"]), KeyboardButton(text=KB_SNAKE_MENU["settings"])]
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

kb_snake_settings = Buttons({
    "dead_border": Button_Bool(**KB_SNAKE_SETTINGS["dead_border"]),
    "color_snake": Button_Choose(**KB_SNAKE_SETTINGS["color_snake"]),
    "size_zone": Button_Choose(**KB_SNAKE_SETTINGS["size_zone"]),
    "symbol_zone": Button_Choose(**KB_SNAKE_SETTINGS["symbol_zone"]),
    "back": Button(**KB_SNAKE_SETTINGS["back"])
})