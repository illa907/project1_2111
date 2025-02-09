def divide_and_sort(a, b, c):
    numbers = [a, b, c]
    if all(num % 5 == 0 for num in numbers):
        return sorted(numbers)
    else:
        raise  ValueError("Якесь число не ділится на 5!")

try:
    a = int(input("Ведіть перше число"))
    b = int(input("Ведіть друге число"))
    c = int(input("Ведіть третє число"))

    result = divide_and_sort(a, b, c)
    print("Відсортовані чиса", result)

except ValueError as e:
    print("Помилка", e)

