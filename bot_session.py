from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand, BotCommandScopeDefault
from aiogram.fsm.state import State, StatesGroup

from message_process import MessageProcess
import logging
from decouple import config

TYPE_TOKEN = 'EXTRA_TOKEN' # TOKEN
ADMINS = list(map(int, config('ADMINS').split(',')))

bot = Bot(token=config(TYPE_TOKEN), default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Текст в reply клавиатурах
KB_MENU = {
    "send_message": "📝 Отправить анонимное письмо", "clear": "🚫 Очистить диалог",
    "info": "📖 О проекте", "contacts": "👤 Контакты",
    "other": "Дополнительно", "admin": "⚙️ Админ панель"
}
KB_SEND_MESSAGE = {
    "cancel": {"text": "❌ Отмена", "command": "cancel_message"}
}
KB_OTHER_MENU = {
    "music": "🎵 Музыка", "snake": "🐍 Игра змейка", "back": "<= Назад"
}
KB_SNAKE_MENU = {
    "play": "Играть", "back": "<= Назад"
}
KB_SNAKE_PLAY = {
    "back": {"text": "<=", "command": "back"},
    "up": {"text": "⬆️", "command": "up"},
    "down": {"text": "⬇️", "command": "down"},
    "left": {"text": "⬅️", "command": "left"},
    "right": {"text": "➡️", "command": "right"},
}

message_process_util = MessageProcess()



class Form_Session(StatesGroup):
    SENDING = State()
    OTHER_MENU = State()
    MAIN_MENU = State()
    SNAKE_MENU = State()
    SNAKE_PLAY = State()

def get_readme_text():
    with open("README.md", "r", encoding="utf-8") as readme:
        info_text = readme.read().strip()

    info_text = info_text.replace("---\n", "")

    info_text = info_text.split("\n")
    info_text = list(map(lambda s: "<i>"+" ".join(s.split()[1:]).strip()+"</i>" if len(s.split()) > 0 and s.split()[0] == "#"*len(s.split()[0]) else s, info_text))
    info_text = list(map(lambda s: " ".join(list(map(lambda w: w.split("[")[0] + f'<a href="{w[w.index("(")+1:w.index(")")].strip()}">'+w[w.index("[")+1:w.index("]")].strip()+"</a>" + w.split(")")[1] if len(s.split()) > 0 and "".join(list(filter(lambda x: x in "[]()", w))) == "[]()" else w, s.split()))), info_text))
    info_text = "\n".join(info_text)

    type_tag = 0
    while info_text.find("**") != -1:
        info_text = info_text.replace("**", "<b>" if type_tag == 0 else "</b>", 1)
        type_tag = not type_tag

    contacts_text = "сбой в программе, контакты не определись :(.\nАдмин уже всё чинит"
    info_text_readlines = info_text.split("\n")
    for i in range(len(info_text_readlines)):
        if "Ссылки и контакты" in info_text_readlines[i]:
            contacts_text = "\n".join(info_text_readlines[i:])
            break

    return info_text, contacts_text
MESSAGE_INFO, MESSAGE_CONTACTS = get_readme_text()


async def set_commands():
    commands = [BotCommand(command='/start', description='Показать главное меню'),
                BotCommand(command='/send_message', description='Отправить анонимное письмо'),
                BotCommand(command='/music', description='Показать список музыки автора'),
                BotCommand(command='/info', description='Узнать информацию о проекте'),
                BotCommand(command='/contacts', description='Узнать контакты автора и ссылки на проект'),
                BotCommand(command='/clear', description='Очистить диалог с ботом'),
                BotCommand(command='/other_menu', description='Показать дополнительное меню'),
                BotCommand(command='/snake', description='Сыграть в змейку')]
    await bot.set_my_commands(commands, BotCommandScopeDefault())