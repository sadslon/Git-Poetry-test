from typing import List, Dict, Iterator, Any


def filter_by_currency(transactions: List[Dict[str, Any]], currency: str) -> Iterator[Dict[str, Any]]:
    """
    Фильтрует транзакции по заданной валюте.

    :param transactions: Список транзакций в виде словарей.
    :param currency: Валюта, по которой необходимо отфильтровать транзакции.
    Итератор транзакций с заданной валютой.
    """
    for transaction in transactions:
        if transaction.get('operationAmount', {}).get('currency', {}).get('code') == currency:
            yield transaction


def transaction_descriptions(transactions: List[Dict[str, Any]]) -> Iterator[str]:
    """
    Возвращает описание каждой транзакции по очереди.
    """
    for transaction in transactions:
        yield transaction.get('description', '')


def card_number_generator(start: int, end: int) -> Iterator[str]:
    """
    Генерирует номера банковских карт в заданном диапазоне.

    :param start: Начальное значение для генерации номеров карт.
    :param end: Конечное значение для генерации номеров карт.
    :return: Итератор номеров карт в формате XXXX-XXXX-XXXX-XXXX.
    """
    for number in range(start, end + 1):
        yield f"{number:016d}"[:4] + " " + f"{number:016d}"[4:8] + " " + f"{number:016d}"[8:12] + " " + f"{number:016d}"[12:16]