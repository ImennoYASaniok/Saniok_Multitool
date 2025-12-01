from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from consts import ADMINS
from keyboards.keyboards import Buttons, Button, Button_Bool, Button_Choose

KB_MENU_1 = {
    "account": "👤 Профиль", "messages": "🤫 Анонимный чат",
    "music": "🎵 Музыка", "fun": "🤪 Развлечения",
    "admin_panel": "⚙️ Админ панель [admin]", "next": "▶️ Далее"
}
def kb_menu_1(user_id: str):
    kb_list = [
        [KeyboardButton(text=KB_MENU_1["account"]), KeyboardButton(text=KB_MENU_1["messages"])],
        [KeyboardButton(text=KB_MENU_1["music"]), KeyboardButton(text=KB_MENU_1["fun"])],
        [KeyboardButton(text=KB_MENU_1["next"])]
    ]
    if user_id in ADMINS: kb_list[-1] = [KeyboardButton(text=KB_MENU_1["admin_panel"]), *kb_list[-1]]
    return ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True,
        one_time_keyboard=True
    )

KB_MENU_2 = {
    "presents": "🎁 Подарки",  "tools": "🛠️ Инструменты",
    "ai_tools": "ИИ инструменты", "auto_tools": "Авто инструменты",
    "next": "▶️ Далее"
}
def kb_menu_2():
    kb_list = [
        [KeyboardButton(text=KB_MENU_2["presents"]), KeyboardButton(text=KB_MENU_2["tools"])],
        [KeyboardButton(text=KB_MENU_2["ai_tools"]), KeyboardButton(text=KB_MENU_2["auto_tools"])],
        [KeyboardButton(text=KB_MENU_2["next"])]
    ]
    return ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True,
        one_time_keyboard=True
    )

KB_MENU_3 = {
    "market_places": "🛒 Маркетплейсы", "subscribe": "🔔 Премиум PRO",
    "search_accounts": "🔎 Поиск пользователей", "clear": "🚫 Очистить диалог",
    "next": "▶️ Далее"
}
def kb_menu_3():
    kb_list = [
        [KeyboardButton(text=KB_MENU_3["market_places"]), KeyboardButton(text=KB_MENU_3["subscribe"])],
        [KeyboardButton(text=KB_MENU_3["search_accounts"]), KeyboardButton(text=KB_MENU_3["clear"])],
        [KeyboardButton(text=KB_MENU_3["next"])]
    ]
    return ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True,
        one_time_keyboard=True
    )

KB_MENU_4 = {
    "settings": "⚙️ Настройки", "extensions":"✨ Расширения",
    "docs": "ℹ️ Документация", "feedback": "⭐ Обратная связь",
    "support": "🤝 Поддержать", "next": "▶️ В начало"
}
def kb_menu_8():
    kb_list = [
        [KeyboardButton(text=KB_MENU_4["settings"]), KeyboardButton(text=KB_MENU_4["extensions"])],
        [KeyboardButton(text=KB_MENU_4["documentation"]), KeyboardButton(text=KB_MENU_4["support"])],
        [KeyboardButton(text=KB_MENU_4["maker_test"]), KeyboardButton(text=KB_MENU_4["next"])]
    ]
    return ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True,
        one_time_keyboard=True
    )