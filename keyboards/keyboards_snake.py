from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

KB_SNAKE_MENU = {
    "play": "🎮 Играть", "settings": "⚙️ Настройки", "back": "<- Назад"
}
KB_SNAKE_PLAY = {
    "back": {"text": "<-", "command": "back"},
    "up": {"text": "⬆️", "command": "up"},
    "down": {"text": "⬇️", "command": "down"},
    "left": {"text": "⬅️", "command": "left"},
    "right": {"text": "➡️", "command": "right"},
}
KB_SNAKE_SETTINGS = {
    "dead_border": {"text": "Смерть от границ", "value": False, "command": "dead_border"},
    "color_snake": {"text": "Цвет змейки", "type": "", "type_value": {"синий": "🔵🟦", "фиолетовый": "🟣🟪", "жёлтый": "🟡🟨", "зелёный": "🟢🟩"}, "command": "color_snake"},
    "size_zone": {"text": "Размер поля", "type": "", "type_value": {"маленький": [6, 6], "средний": [11, 11], "большой": [16, 16]}, "command": "size_zone"},
    "symbol_zone": {"text": "Символ поля", "type": "", "type_value": {"⬛️": "⬛️", "..": "..", "░░": "░░"}, "command": "symbol_zone"},
    "back": {"text": "<= Назад", "command": "back"},
}

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