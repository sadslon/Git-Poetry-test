import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator

transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702"
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {
            "amount": "79114.93",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188"
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {
            "amount": "43318.34",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160"
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {
            "amount": "56883.54",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229"
    },
]


def test_filter_by_currency():
    usd_transactions = list(filter_by_currency(transactions, "USD"))

    assert len(usd_transactions) == 3
    assert usd_transactions[0]['description'] == "Перевод организации"
    assert usd_transactions[1]['description'] == "Перевод со счета на счет"
    assert usd_transactions[2]['description'] == "Перевод с карты на карту"

    empty_transactions = list(filter_by_currency([], "USD"))
    assert len(empty_transactions) == 0


def test_transaction_descriptions():
    descriptions = list(transaction_descriptions(transactions))

    assert len(descriptions) == 4
    assert descriptions[0] == "Перевод организации"
    assert descriptions[1] == "Перевод со счета на счет"
    assert descriptions[2] == "Перевод со счета на счет"
    assert descriptions[3] == "Перевод с карты на карту"

    empty_descriptions = list(transaction_descriptions([]))
    assert len(empty_descriptions) == 0


def test_card_number_generator():
    generated_numbers = list(card_number_generator(1, 5))
    expected_numbers = [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
        "0000 0000 0000 0005"
    ]

    assert generated_numbers == expected_numbers
