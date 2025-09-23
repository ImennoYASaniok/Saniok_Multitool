import asyncio

from aiogram import Router, F
from aiogram.filters import Command, or_f
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from keyboards.keyboards import kb_other_menu, kb_snake_menu, kb_snake_play
from bot_session import bot
from bot_session import KB_OTHER_MENU, KB_SEND_MESSAGE, KB_SNAKE_MENU, KB_SNAKE_PLAY, logger
from bot_session import message_process_util
from bot_session import Form_Session
from handlers.handlers_other_menu import fun_menu_other

from db.db_session import create_session
from db.models import Messages as Model_Messages, Users

from random import choice

class Snake:
    def __init__(self):
        self.SYMBOLS = {
            "zone": "##",
            "snake_head": "🟠",
            "snake_body": "🟧",
            "apple": "🍎"
        }

        self.w_zone, self.h_zone = 10, 10
        self.zone = self._zone_clear()

        self.snake_dir = "up"
        self.snake_coords = [[self.w_zone // 2, self.h_zone // 2], [self.w_zone // 2, self.h_zone // 2 + 1]]
        self.snake_length = 1

        self.apple_coords = self._apple_spawn()

    def _zone_clear(self) -> list:
        return [[self.SYMBOLS["zone"]] * self.w_zone for _ in range(self.h_zone)]

    def _apple_spawn(self) -> [int, int]:
        return [choice(list(filter(lambda x: x not in list(map(lambda c: c[0], self.snake_coords)), range(0, self.w_zone)))),
                choice(list(filter(lambda y: y not in list(map(lambda c: c[1], self.snake_coords)), range(0, self.h_zone))))]

    def get_screen(self) -> str:
        return f"Текущий результат {self.snake_length}\n\n" + "\n".join(["".join(row) for row in self.zone])

    def _is_alive(self) -> bool:
        head_coords = self.snake_coords[0]
        if 0 <= head_coords[0] <= self.w_zone - 1 and 0 <= head_coords[1] <= self.h_zone - 1:
            return True
        else:
            return False

    def _move_snake(self):
        new_head_coords = self.snake_coords[0].copy()
        if self.snake_dir == "up":
            new_head_coords[1] -= 1
        elif self.snake_dir == "down":
            new_head_coords[1] += 1
        elif self.snake_dir == "left":
            new_head_coords[0] -= 1
        elif self.snake_dir == "right":
            new_head_coords[0] += 1
        new_coords = [new_head_coords]
        for i in range(len(self.snake_coords) - 1):
            new_coords.append(self.snake_coords[i])
        self.snake_coords = new_coords.copy()

    async def run_screen(self, message, state, message_game_id, chat_id):
        try:
            while self._is_alive():
                await asyncio.sleep(0.5)
                try:
                    self._move_snake()
                    # print("snake:", self.snake_coords)
                    # print("apple:", self.apple_coords)
                    # print("zone:", self.w_zone, self.h_zone)
                    # print()
                    self.update_screen()
                    await bot.edit_message_text(
                        chat_id=chat_id,
                        message_id=message_game_id,
                        text=self.get_screen(),
                        reply_markup=kb_snake_play()
                    )
                    # await message.edit_text(self.get_screen(), reply_markup=kb_snake_play())
                except Exception as e:
                    logger.error(f"Ошибка при обновление поля: {e}")
            print(f"Итоговый результат {self.snake_length}")
            await func_snake_menu(message, state)
        except asyncio.CancelledError:
            logger.info("Игра завершена")

    def update_screen(self):
        self.zone = self._zone_clear()
        print(self.w_zone, self.h_zone, self.apple_coords[1], self.apple_coords[0])
        self.zone[self.apple_coords[1]][self.apple_coords[0]] = self.SYMBOLS["apple"]
        print(self.w_zone, self.h_zone, self.snake_coords[0][1], self.snake_coords[0][0])
        self.zone[self.snake_coords[0][1]][self.snake_coords[0][0]] = self.SYMBOLS["snake_head"]
        print("INTO")
        for coords in self.snake_coords[1:]:
            self.zone[coords[1]][coords[0]] = self.SYMBOLS["snake_body"]

snake_task = None
snake = Snake()

snake_router = Router()

async def func_snake_menu(message: Message, state: FSMContext):
    global snake_task
    if snake_task:
        snake_task.cancel()
    await state.set_state(Form_Session.SNAKE_MENU)
    await message.answer(message_process_util.get_message("snake_menu"), reply_markup=kb_snake_menu())

@snake_router.message(or_f(Command("snake"), F.text == str(KB_OTHER_MENU["snake"])))
async def handle_snake_menu(message: Message, state: FSMContext):
    await func_snake_menu(message, state)

@snake_router.message(Form_Session.SNAKE_MENU, F.text == str(KB_SNAKE_MENU["back"]))
async def handle_snake_back(message: Message, state: FSMContext):
    await fun_menu_other(message, state)

@snake_router.message(Form_Session.SNAKE_MENU, F.text == str(KB_SNAKE_MENU["play"]))
async def handle_snake_play(message: Message, state: FSMContext):
    global snake_task, snake
    await state.set_state(Form_Session.SNAKE_PLAY)
    snake = Snake()
    message_game = await message.answer(snake.get_screen(), reply_markup=kb_snake_play())
    snake_task = asyncio.create_task(snake.run_screen(message=message, state=state, message_game_id=message_game.message_id, chat_id=message_game.chat.id))

@snake_router.callback_query(Form_Session.SNAKE_PLAY, lambda x: x.data == KB_SNAKE_PLAY["back"]["command"])
async def handle_snake_play_back(callback: CallbackQuery, state: FSMContext):
    print("Фиксация результата")
    await func_snake_menu(callback.message, state)
    await callback.answer()

@snake_router.callback_query(Form_Session.SNAKE_PLAY, lambda x: x.data in KB_SNAKE_PLAY["up"]["command"])
async def handle_snake_play_up(callback: CallbackQuery, state: FSMContext):
    snake.snake_dir = "up"
    await callback.answer()

@snake_router.callback_query(Form_Session.SNAKE_PLAY, lambda x: x.data in KB_SNAKE_PLAY["down"]["command"])
async def handle_snake_play_down(callback: CallbackQuery, state: FSMContext):
    snake.snake_dir = "down"
    await callback.answer()

@snake_router.callback_query(Form_Session.SNAKE_PLAY, lambda x: x.data in KB_SNAKE_PLAY["left"]["command"])
async def handle_snake_play_left(callback: CallbackQuery, state: FSMContext):
    snake.snake_dir = "left"
    await callback.answer()

@snake_router.callback_query(Form_Session.SNAKE_PLAY, lambda x: x.data in KB_SNAKE_PLAY["right"]["command"])
async def handle_snake_play_right(callback: CallbackQuery, state: FSMContext):
    snake.snake_dir = "right"
    await callback.answer()