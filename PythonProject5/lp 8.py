import re
import logging
import time
import unittest


def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        logging.info(f"Функція {func.__name__} виконалась за {execution_time:.6f} секунд")
        return result, execution_time

    return wrapper


def calculator_decorator(func):
    def wrapper(expression):
        logging.basicConfig(filename="calculator.log", level=logging.INFO, format="%(asctime)s - %(message)s")

        if not re.match(r'^[0-9+\-*/(). ]+$', expression):
            logging.error(f"Невірний ввід: {expression}")
            return "Помилка: введено недопустимі символи"

        try:
            result = func(expression)
            logging.info(f"Обчислення: {expression} = {result}")
            return result
        except Exception as e:
            logging.error(f"Помилка при обчисленні '{expression}': {e}")
            return "Помилка: некоректний вираз"

    return wrapper


@calculator_decorator
@timer_decorator
def calculate(expression):
    return eval(expression)


class TestTimerDecorator(unittest.TestCase):
    def test_calculate_valid(self):
        result, exec_time = calculate("2 + 2 * 2")
        self.assertEqual(result, 6)
        self.assertGreaterEqual(exec_time, 0)

    def test_calculate_division_by_zero(self):
        result, exec_time = calculate("10 / 0")
        self.assertEqual(result, "Помилка: некоректний вираз")
        self.assertGreaterEqual(exec_time, 0)

    def test_calculate_invalid_input(self):
        result, exec_time = calculate("hello")
        self.assertEqual(result, "Помилка: введено недопустимі символи")
        self.assertGreaterEqual(exec_time, 0)


if __name__ == "__main__":
    unittest.main()