
import re
from typing import List, NamedTuple, Optional

import exceptions


class Message(NamedTuple):
    """Структура распаршенного сообщения о новом расходе"""
    amount: int
    category_text: str


class Expense(NamedTuple):
    """Структура добавленного в БД нового расхода"""
    id: Optional[int]
    amount: int
    category_name: str


def add_expense(raw_message: str) -> Expense:
    """Добавляет новое сообщение.
    Принимает на вход текст сообщения, пришедшего в бот."""
    parsed_message = _parse_message(raw_message)
    # category = Categories().get_category(
    #     parsed_message.category_text)
    # inserted_row_id = db.insert("expense", {
    #     "amount": parsed_message.amount,
    #     "created": _get_now_formatted(),
    #     "category_codename": category.codename,
    #     "raw_text": raw_message
    # })
    return Expense(id=None,
                   amount=parsed_message.amount,
                #    category_name=category.name)
                category_name=parsed_message.category_text) #tmp_kostil


def _parse_message(raw_message: str) -> Message:
    """Парсит текст пришедшего сообщения о новом расходе."""
    regexp_result = re.match(r"([\d ]+) (.*)", raw_message)
    if not regexp_result or not regexp_result.group(0) \
            or not regexp_result.group(1) or not regexp_result.group(2):
        raise exceptions.NotCorrectMessage(
            "Не могу понять сообщение. Напишите сообщение в формате, "
            "например:\n1500 метро")

    amount = regexp_result.group(1).replace(" ", "")
    category_text = regexp_result.group(2).strip().lower()
    return Message(amount=amount, category_text=category_text)