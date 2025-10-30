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