from typing import Generator


def filter_by_currency(transactions: list[dict], currency: str) -> Generator[str, None, None]:
    """Функция, фильтрующая операции по заданной валюте"""
    if len(transactions) > 0:
        filtered_transactions = filter(
            lambda transactions: transactions.get("operationAmount").get("currency").get("code") == currency,
            transactions
        )
        return filtered_transactions
    else:
        return "Список пустой!"


def transaction_descriptions(transactions: list[dict]) -> Generator[str, None, None]:
    """Генератор, выводящий описание каждой операции по очереди"""
    try:
        for description_operation in transactions:
            yield description_operation.get("description")
    except StopIteration:
        if transactions == []:
            return "Нет транзакций"


def card_number_generator(start: int, stop: int) -> Generator[str, None, None]:
    """Функция для генерации номера карты"""
    for number in range(start, stop):
        card_number = str(number)
        while len(card_number) < 16:
            card_number = "0" + card_number
        formatted_card_number = f"{card_number[0:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:16]}"
        yield formatted_card_number
