import functools
import logging
import sys


def log(filename: str = None):
    """
        Декоратор для логирования выполнения функции.
       :param filename:
       :return:
       """
    logger = logging.getLogger('function_logger')
    logger.setLevel(logging.DEBUG)

    if filename:
        file_handler = logging.FileHandler(filename)
        logger.addHandler(file_handler)

    console_handler = logging.StreamHandler(sys.stdout)
    logger.addHandler(console_handler)

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                logger.info(f"Starting {func.__name__} with inputs: {args}, {kwargs}")
                result = func(*args, **kwargs)
                logger.info(f"{func.__name__} ok")
                return result
            except Exception as e:
                logger.error(f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}")
                raise
            finally:
                if filename:
                    logger.removeHandler(file_handler)
                logger.removeHandler(console_handler)

        return wrapper

    return decorator