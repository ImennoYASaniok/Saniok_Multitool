from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand, BotCommandScopeDefault
from aiogram.fsm.state import State, StatesGroup

from message_process import MessageProcess
import logging
from consts import TOKEN

bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

message_process_util = MessageProcess()

class Form_Session(StatesGroup):
    SENDING = State()
    OTHER_MENU = State()
    MAIN_MENU = State()
    SNAKE_MENU = State()
    SNAKE_PLAY = State()
    SNAKE_SETTINGS = State()
    MESSAGES_MENU = State()

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