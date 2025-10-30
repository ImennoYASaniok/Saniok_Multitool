from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from consts import ADMINS

# сделать так чтобы через "#" подставлялся нужный тип сообщения (тег)
KB_MESSAGES_MENU = {
    "send_message": "📝 Отправить письмо", "edit_messages": "✎ Редактирование писем",
    "check_messages": "🆗 Пометка писем [admin]", "back": "🔙 Назад"
}
KB_SEND_MESSAGE = {
    "type": {"text": "☰ Тип письма", "type": "", "type_value": {"обычное": "basic", "поддержки": "support"}, "command": "type_message"},
    "cancel": {"text": "❌ Отмена", "command": "cancel_message"}
}

def kb_messages_menu(user_id: str):
    kb_list = [
        [KeyboardButton(text=KB_MESSAGES_MENU["send_message"]), KeyboardButton(text=KB_MESSAGES_MENU["edit_messages"])],
        [KeyboardButton(text=KB_MESSAGES_MENU["back"])]
    ]
    if user_id in ADMINS: kb_list[-1].append(KeyboardButton(text=KB_MESSAGES_MENU["check_messages"]))
    return ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Воспользуйтесь дополнительным меню:"
    )

def kb_message():
    kb_list = [
        [InlineKeyboardButton(text=KB_SEND_MESSAGE["cancel"]["text"], callback_data=KB_SEND_MESSAGE["cancel"]["command"])]
    ]
    return InlineKeyboardMarkup(inline_keyboard=kb_list)