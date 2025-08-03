import functools
import logging
import sys


def log(filename: str = None):
    """
    Декоратор для логирования выполнения функции.

    :param filename: Имя файла, в который будут записываться логи. Если None, логи выводятся в консоль.
    """
    # Настройка логирования
    logger = logging.getLogger('function_logger')
    logger.setLevel(logging.DEBUG)

    if filename:
        file_handler = logging.FileHandler(filename)
        logger.addHandler(file_handler)
    else:
        console_handler = logging.StreamHandler(sys.stdout)
        logger.addHandler(console_handler)

    # Декоратор
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                # Логирование начала выполнения функции
                logger.info(f"Starting {func.__name__} with inputs: {args}, {kwargs}")
                result = func(*args, **kwargs)

                # Логирование успешного завершения функции
                logger.info(f"{func.__name__} ok")
                return result
            except Exception as e:
                # Логирование возникшей ошибки
                logger.error(f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}")
                raise  # Перебрасываем ошибку дальше

        return wrapper

    return decorator
