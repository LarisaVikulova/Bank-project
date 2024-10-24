import pytest

from src.generators import filter_by_currency, card_number_generator, transaction_descriptions


@pytest.mark.parametrize("index, expected", [(0, "Перевод организации"), (1, "Перевод со счета на счет")])
def test_transaction_descriptions(index: int, expected: str) -> None:
    """Функция тестирования вывода описания каждой операции"""
    transactions_list = [{"description": "Перевод организации"}, {"description": "Перевод со счета на счет"}]
    descriptions = list(transaction_descriptions(transactions_list))
    assert descriptions[index] == expected


@pytest.fixture
def transactions() -> list[dict]:
    """Функция вывода транзакций для тестирования"""
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
    ]


def test_filter_by_currency_exceptions(transactions: list[dict]) -> None:
    """Функция тестирования вывода транзакций по заданной валюте"""
    result = filter_by_currency(transactions, "EUR")
    assert list(result) == []
    result = filter_by_currency([], "EUR")
    assert result == "Список пустой!"


@pytest.mark.parametrize("start, stop, expected", [(1, 2, ("0000 0000 0000 0001"))])
def test_card_number_generator(start: int, stop: int, expected: str) -> None:
    """Функция тестирует генератор для номеров карт"""
    assert next(card_number_generator(start, stop)) == expected
