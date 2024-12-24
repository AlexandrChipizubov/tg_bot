import asyncio
import logging

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from config import TOKEN, ID
import exceptions
import expenses

bot = Bot(token=TOKEN)
dp = Dispatcher()

def auth(func):
    async def wrapper(message):
        if message.from_user.id != ID:
            return await message.reply('Access Denies', reply=False)
        return await func(message)
    return wrapper

@dp.message(CommandStart())
@auth
async def cmd_start(message: Message):
    await message.answer(f'Привет.\nТвой ID: {message.from_user.id}\nИмя: {message.from_user.full_name}')

@dp.message(Command('help'))
@auth
async def cmd_help(message: Message):
    await message.answer('Это команда /help')

@dp.message(F.text == 'Как дела?')
@auth
async def how_are_you(message: Message):
    await message.answer('OK!')


@dp.message_handler()
@auth
async def add_expense(message: types.Message):
    """Добавляет новый расход"""
    try:
        expense = expenses.add_expense(message.text)
    except exceptions.NotCorrectMessage as e:
        await message.answer(str(e))
        return
    answer_message = (
        f"Добавлены траты {expense.amount} руб на {expense.category_name}.\n\n"
        # f"{expenses.get_today_statistics()}"
        )
    await message.answer(answer_message)



async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')