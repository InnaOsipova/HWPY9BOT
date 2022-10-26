import logging

from aiogram import Bot, Dispatcher, types
from aiogram.filters  import Command
from aiogram.types import Message

TOKEN = "5582013163:AAFinLXA1XGMmyn-TXYvcOQFIs5vhc8Ffxs"
bot = Bot(TOKEN)
dp = Dispatcher()

logger = logging.getLogger(__name__)


@dp.message(Command(commands=["start"]))
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, <b>{message.from_user.full_name}!</b>")


@dp.message()
async def echo_handler(message: types.Message) -> None:
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer("Nice try!")


def main() -> None:
    bot = Bot(TOKEN, parse_mode="HTML")
    dp.run_polling(bot)
    


if __name__ == '__main__':
    print('Сервер запущен')
    main()
    

