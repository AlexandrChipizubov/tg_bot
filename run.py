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
@dp.message(Command('help'))
async def send_welcome(message: Message):
    """Отправляет приветственное сообщение и помощь по боту"""
    await message.answer(
        "Бот для учёта финансов\n\n"
        "Добавить расход: 250 такси\n"
        # "Сегодняшняя статистика: /today\n"
        # "За текущий месяц: /month\n"
        "Последние внесённые расходы: /expenses\n\n"
        # "Категории трат: /categories"
        "Узнать свой ID: /id"
        )

@dp.message(Command('id'))
async def get_user_data(message: Message):
    await message.answer(f'Привет.\nТвой ID: {message.from_user.id}\nИмя: {message.from_user.full_name}')

@dp.message(lambda message: message.text.startswith('/del'))
@auth
async def del_expense(message: Message):
    """Удаляет одну запись о расходе по её идентификатору"""
    row_id = int(message.text[4:])
    expenses.delete_expense(row_id)
    answer_message = "Удалил"
    await message.answer(answer_message)

@dp.message(Command('month'))
@auth
async def month_statistics(message: Message):
    """Отправляет статистику трат текущего месяца"""
    answer_message = expenses.get_month_statistics()
    await message.answer(answer_message)

@dp.message(Command('expenses'))
async def list_expenses(message: Message):
    """Отправляет последние несколько записей о расходах"""
    last_expenses = expenses.last()
    if not last_expenses:
        await message.answer("Расходы ещё не заведены")
        return
    last_expenses_rows = [
        f"{expense.amount} руб. на {expense.category_name} — нажми "
        f"/del{expense.id} для удаления"
        for expense in last_expenses]
    answer_message = "Последние сохранённые траты:\n\n* " + "\n\n* "\
            .join(last_expenses_rows)
    await message.answer(answer_message)

@dp.message()
@auth
async def add_expense(message: Message):
    """Добавляет новый расход"""
    try:
        expense = expenses.add_expense(message.text)
    except exceptions.NotCorrectMessage as e:
        await message.answer(str(e))
        return
    answer_message = (
        f"Добавлены траты {expense.amount} руб на {expense.category_name}.\n"
        f"Нажми /del{expense.id} для удаления\n\n"
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

#.venv\Scripts\activate