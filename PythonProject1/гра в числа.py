import random

secret_number = random.randint(1, 100)
attempts = 3

print("Я загадав число від 1 до 100. Спробуй вгадати!")

for _ in range(attempts):
    guess = int(input("Введіть число: "))

    if guess > secret_number:
        print("Менше")
    elif guess < secret_number:
        print("Більше")
    else:
        print("Вітаю, ви вгадали!")
        break
else:
    print(f"Ви не вгадали! Загадане число було {secret_number}.")