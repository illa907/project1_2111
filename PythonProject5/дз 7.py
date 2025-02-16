result = []

def divider(a, b):
    try:
        if a < b:
            raise ValueError("Число 'a' менше за 'b'")
        if b > 100:
            raise IndexError("Число 'b' більше 100")
        return a / b
    except ZeroDivisionError:
        print(f"Помилка: Ділення на нуль ({a} / {b})")
    except ValueError as e:
        print(f"Помилка ValueError: {e}")
    except IndexError as e:
        print(f"Помилка IndexError: {e}")

data = {10: 2, 2: 5, "123": 4, 18: 0, 8: 4}

for key, value in data.items():
    try:
        res = divider(int(key), int(value))
        if res is not None:
            result.append(res)
    except TypeError:
        print(f"Помилка TypeError: Неприпустимий тип ключа або значення ({key}: {value})")
    except Exception as e:
        print(f"Невідома помилка: {e}")

print("Результат:", result)