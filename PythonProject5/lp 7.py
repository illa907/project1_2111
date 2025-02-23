import re
import logging

logging.basicConfig(filename="calculator.log", level=logging.INFO, format="%(asctime)s - %(message)s")


def calculator_decorator(func):
    def wrapper(expression):
        if not re.match(r'^[0-9+\-*/(). ]+$', expression):
            logging.error(f"Невірний ввід: {expression}")
            return "Помилка: введено недопустимі символи"

        try:
            result = func(expression)
            logging.info(f"Обчислення: {expression} = {result}")
            return result
        except ZeroDivisionError:
            logging.error(f"Помилка: ділення на нуль у виразі '{expression}'")
            return "Помилка: ділення на нуль"
        except SyntaxError:
            logging.error(f"Помилка: некоректний вираз '{expression}'")
            return "Помилка: некоректний вираз"
        except Exception as e:
            logging.error(f"Невідома помилка у виразі '{expression}': {e}")
            return f"Помилка: {e}"

    return wrapper


@calculator_decorator
def calculate(expression):
    return eval(expression)


print(calculate("2 + 2 * 2"))
print(calculate("10 / 0"))
print(calculate("hello"))
print(calculate("5 + (3 * 2"))