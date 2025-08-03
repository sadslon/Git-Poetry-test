import pytest
import os
from decorators import log


@log()
def successful_function(x, y):
    return x + y


@log()
def failing_function(x, y):
    return x / y  # Деление на ноль вызовет ошибку


def test_successful_function(capsys):
    result = successful_function(1, 2)
    assert result == 3

    # Проверяем, что вывод в консоль соответствует ожиданиям
    captured = capsys.readouterr()
    assert "Starting successful_function with inputs: (1, 2), {}" in captured.out
    assert "successful_function ok" in captured.out


def test_failing_function(capsys):
    with pytest.raises(ZeroDivisionError):
        failing_function(1, 0)

    # Проверяем, что вывод в консоль соответствует ожиданиям
    captured = capsys.readouterr()
    assert "Starting failing_function with inputs: (1, 0), {}" in captured.out
    assert "failing_function error: ZeroDivisionError. Inputs: (1, 0), {}" in captured.err


def test_log_file():
    log_filename = 'test_log.txt'

    @log(filename=log_filename)
    def add_numbers(a, b):
        return a + b

    add_numbers(5, 3)

    # Проверяем содержимое лог-файла
    with open(log_filename, 'r') as file:
        logs = file.read()

    assert "Starting add_numbers with inputs: (5, 3), {}" in logs
    assert "add_numbers ok" in logs

    # Удаляем файл после теста
    os.remove(log_filename)