import pytest
import os
from src.decorators import log
import logging


@pytest.fixture
def caplog(capsys):
    capsys.readouterr()  # очищаем перед тестом
    return capsys


def test_log_file():
    log_filename = 'test_log.text'

    @log(filename=log_filename)
    def add_numbers(a, b):
        return a + b

    add_numbers(5, 3)

    # Проверяем содержимое лог-файла
    with open(log_filename, 'r') as file:
        logs = file.read()

    assert "Starting add_numbers with inputs: (5, 3), {}" in logs
    assert "add_numbers ok" in logs

    # Удаляем файл после теста с помощью try..except
    try:
        os.remove(log_filename)
    except PermissionError:
        print(f"Не удалось удалить файл {log_filename}, возможно, файл все еще занят.")


def test_successful_function(capsys):
    result = successful_function(1, 2)
    assert result == 3


@log()
def successful_function(a, b):
    logging.info(f"Starting successful_function with inputs: ({a}, {b}), {{}}")
    return a + b

    # Проверяем, что лог соответствует ожиданиям


# assert "Starting successful_function with inputs: (1, 2), {}" in caplog
# assert "successful_function ok" in caplog


def test_failing_function(capsys):
    with pytest.raises(ZeroDivisionError):
        failing_function(1, 0)


@log()
def failing_function(x, y):
    return x / y  # Деление на ноль вызовет ошибку

    # Проверяем, что лог соответствует ожиданиям


# assert "Starting failing_function with inputs: (1, 0), {}" in caplog
# assert "failing_function error: ZeroDivisionError. Inputs: (1, 0), {}" in caplog
