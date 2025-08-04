# Программа  для сортировки списков словарей по дате и по ключу у которой есть определённый параметр
# Модуль генераторов для работы с транзакциями

## Установка
## Декоратор логирования

## log
Декоратор `log` используется для логирования выполнения функций. 
Принимает необязательный аргумент `filename` для указания файла, 
в который будут записываться логи. Если `filename` не указан, вывод идет в консоль.
## Функции
```commandline
filter_by_currency(transactions, currency)
```
Фильтрует транзакции по заданной валюте. Возвращает итератор транзакций с заданной валютой.
```commandline
transaction_descriptions(transactions)
```
Возвращает описание каждой транзакции по очереди.
```commandline
card_number_generator(start, end)
```
Генерирует номера банковских карт в заданном диапазоне.

1. Клонируйте репозиторий

```commandline
git@github.com:sadslon/git-poetry-test.git
```

2. Установите зависимости:

```commandline
from datetime import datetime
import functools
import logging
import sys
from src.decorators import log
import pytest
from src.processing import filter_by_state, sort_by_date
from src.widget import mask_account_card
from src.masks import get_mask_card_number, get_mask_account
from typing import List, Dict, Iterator, Any
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator
```

3. Установите инструменты:

```commandline
pip install flake8 mypy black pytest
```
### Запуск тестов
Для запуска тестов используется команда:
```commandline
pytest test_generators.py
```

## Использование:

1. Перейдите на страницу https://github.com/ в вашем веб-браузере.
2. Создайте новую учетную запись или войдите c существующей.