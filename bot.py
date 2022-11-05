import logging
from tracemalloc import Filter
from typing import Text
import calc as c

from aiogram import Bot, Dispatcher, types
from aiogram.filters  import Command
from aiogram.types import Message
from aiogram.types.message import *
from aiogram.filters.state import State, StatesGroup
import asyncio
import logging
import sys
from os import getenv
from typing import Any, Dict

from aiogram import Bot, Dispatcher, F, Router, html
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import KeyboardButton, Message, ReplyKeyboardMarkup, ReplyKeyboardRemove

from magic_filter import F

form_router = Router()


TOKEN = "5582013163:AAFinLXA1XGMmyn-TXYvcOQFIs5vhc8Ffxs"
bot = Bot(TOKEN)
dp = Dispatcher()

logger = logging.getLogger(__name__)

class Form(StatesGroup):
    ans1 = State()
    ans2 = State()
    like_bots = State()



@dp.message(Command(commands=["start"]))
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, <b>{message.from_user.full_name}!</b>")

@dp.message(Command(commands=["calc"]))
async def cmd_dialog(message: types.Message, state: FSMContext) -> None:
    await state.set_state(Form.like_bots)
    await message.answer(
        f"Давайте посчитаем, {message.from_user.full_name}!\nКакой калькулятор вы выбираете?",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="Рациональные числа"),
                    KeyboardButton(text="Комплексные числа"),
                ]
            ],
            resize_keyboard=True,
        ),
    )
@dp.message(Form.like_bots, F.text.contains("Рациональные числа"))
async def cmd_dialog2(message: Message, state: FSMContext) -> None:
    await state.set_state(Form.ans1)
    await message.answer('Введите выражение для вычисления в формате: "A/B действие C/D, где:"'
                            '\n A и B - числители первой и второй дроби'
                            '\n C и D - знаменатели первой и второй дроби'
                            '\nдействие - математическая операция которую нужно произвести с двумя числами'
                            '\nМежду дробями и действием ставьте пробелы:'
                            '\n', reply_markup=ReplyKeyboardRemove())
    

@dp.message(Form.ans1)
async def process_message(message: Message, state : FSMContext) -> None:
    await state.update_data(ans1=message.text)
    await message.answer(c.calc_ration(message.text))    
  

@dp.message(Form.like_bots, F.text.contains("Комплексные числа"))
async def cmd_dialog1(message: Message, state: FSMContext) -> None:
    await state.set_state(Form.ans2)
    await message.answer('Введите выражение для вычисления в формате: "A знак(+-) B действие C знак(+-) D, где:'
                            '\n A и C - действительные части чисел"'
                            '\n B и D - мнимые части чисел'
                            '\n действие - математическая операция которую нужно произвести с двумя числами'
                            '\nМежду числами и знаком ставьте пробелы:'
                            '\n', reply_markup=ReplyKeyboardRemove())
@dp.message(Form.ans2)
async def process_message(message: Message, state : FSMContext) -> None:
    await state.update_data(ans2=message.text)
    await message.answer(c.calc_complex(message.text))  



def main() -> None:
    bot = Bot(TOKEN, parse_mode="HTML")
    dp.run_polling(bot)
    


if __name__ == '__main__':
    print('Сервер запущен')
    main()
    

