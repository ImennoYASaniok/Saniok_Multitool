from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from consts import ADMINS


KB_MENU_1 = {
    "messages": "📝 Письма", "memes": "😂 Мемы",
    "music": "🎵 Музыка", "games": "🎮 Игры",
    "admin_panel": "⚙️ Админ панель [admin]", "next": "▶️ Далее"
}
def kb_menu_1(user_id: str):
    kb_list = [
        [KeyboardButton(text=KB_MENU_1["messages"]), KeyboardButton(text=KB_MENU_1["memes"])],
        [KeyboardButton(text=KB_MENU_1["music"]), KeyboardButton(text=KB_MENU_1["games"])],
        [KeyboardButton(text=KB_MENU_1["next"])]
    ]
    if user_id in ADMINS: kb_list[-1] = [KeyboardButton(text=KB_MENU_1["admin_panel"]), *kb_list[-1]]
    return ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True,
        one_time_keyboard=True
    )

KB_MENU_2 = {
    "predictions": "🔮 Предсказания", "casino": "🎰 Казик",
    "notes": "📒 Заметки", "todolist": "🗓️ Ту ду лист",
    "anonymous_chat": "🤫 Анонимный чат", "next": "▶️ Далее"
}
def kb_menu_2():
    kb_list = [
        [KeyboardButton(text=KB_MENU_2["predictions"]), KeyboardButton(text=KB_MENU_2["casino"])],
        [KeyboardButton(text=KB_MENU_2["notes"]), KeyboardButton(text=KB_MENU_2["todolist"])],
        [KeyboardButton(text=KB_MENU_2[""]), KeyboardButton(text=KB_MENU_2["next"])]
    ]
    return ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True,
        one_time_keyboard=True
    )

KB_MENU_3 = {
    "translate": "🔠 Переводчик", "llm": "🤖 Chat GPT", # + Распознать голос
    "editor_image": "🎨 Редактор картинок", "editor_video": "🎥 Редактор видео",
    "next": "▶️ Далее"
}
def kb_menu_3():
    kb_list = [
        [KeyboardButton(text=KB_MENU_3["translate"]), KeyboardButton(text=KB_MENU_3["llm"])],
        [KeyboardButton(text=KB_MENU_3["editor_image"]), KeyboardButton(text=KB_MENU_3["editor_video"])],
        [KeyboardButton(text=KB_MENU_3["next"])]
    ]
    return ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True,
        one_time_keyboard=True
    )

KB_MENU_4 = {
    "auto_publish": "✍️ Авто публикация", "auto_comments": "💬 Авто комментарии", # комменты в ютуб + twitch
    "auto_antispam": "🚫 Авто анти спам", "pixel_art": "🎨 Пиксель-арты",
    "next": "▶️ Далее"
}
def kb_menu_4():
    kb_list = [
        [KeyboardButton(text=KB_MENU_4["auto_publish"]), KeyboardButton(text=KB_MENU_4["auto_comments"])],
        [KeyboardButton(text=KB_MENU_4["auto_spam"])],
        [KeyboardButton(text=KB_MENU_4["next"])]
    ]
    return ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True,
        one_time_keyboard=True
    )

KB_MENU_5 = {
    "market": " 🛒 Магазин", "stock_translate": "💰 Рынок переводов",
    "crypto": "₿ Крипта", "presents": "🎁 Подарки",
    "auction": "⚖️ Аукционы", "next": "▶️ Далее"
}
def kb_menu_5():
    kb_list = [
        [KeyboardButton(text=KB_MENU_5["market"]), KeyboardButton(text=KB_MENU_5["stock_translate"])],
        [KeyboardButton(text=KB_MENU_5["crypto"]), KeyboardButton(text=KB_MENU_5["presents"])],
        [KeyboardButton(text=KB_MENU_5["auction"]), KeyboardButton(text=KB_MENU_5["next"])]
    ]
    return ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True,
        one_time_keyboard=True
    )

KB_MENU_6 = {
    "account": "👤 Аккаунт", "friends": "👥 Друзья",
    "subscribe": "🔔 Подписка", "rating": "🌟 Рейтинг",
    "search_accounts": "🔎 Поиск аккаунтов", "next": "▶️ Далее"
}
def kb_menu_6():
    kb_list = [
        [KeyboardButton(text=KB_MENU_5["account"]), KeyboardButton(text=KB_MENU_5["friends"])],
        [KeyboardButton(text=KB_MENU_5["search_accounts"])],
        [KeyboardButton(text=KB_MENU_5["next"])]
    ]
    return ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True,
        one_time_keyboard=True
    )

KB_MENU_7 = {
    "search_internet": "🔎 Поисковик", "statistics": "📊 Статистика",
    "ide": "👨🏻‍💻 Среды разработки", "extra_func": "✨ Доп функции / Расширения",
    "maker_test": "📋 Составить тест", "next": "▶️ Далее"
}
def kb_menu_7():
    kb_list = [
        [KeyboardButton(text=KB_MENU_6["search"]), KeyboardButton(text=KB_MENU_6["statistics"])],
        [KeyboardButton(text=KB_MENU_6["ide"]), KeyboardButton(text=KB_MENU_6["extra_func"])],
        [KeyboardButton(text=KB_MENU_6["next"])]
    ]
    return ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True,
        one_time_keyboard=True
    )

KB_MENU_8 = {
    "settings": "⚙️ Настройки", "questions": "❓ Частые вопросы",
    "about_projects": "ℹ️ О проекте", "about_autor": "👤 О авторе",
    "support": "🤝 Поддержать", "next": "▶️ Обратно"
}
def kb_menu_8():
    kb_list = [
        [KeyboardButton(text=KB_MENU_7["settings"]), KeyboardButton(text=KB_MENU_7["support"])],
        [KeyboardButton(text=KB_MENU_7["about_projects"]), KeyboardButton(text=KB_MENU_7["about_autor"])],
        [KeyboardButton(text=KB_MENU_4["maker_test"]), KeyboardButton(text=KB_MENU_7["next"])]
    ]
    return ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True,
        one_time_keyboard=True
    )