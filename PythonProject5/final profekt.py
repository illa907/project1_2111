import random
import time
import os

# Файл для збереження рекорду
LEADERBOARD_FILE = "leaderboard.txt"

# Налаштування гри
WIDTH = 3  # Кількість смуг
CAR = "🚗"
OBSTACLE = "X"
BONUS = "⭐"
EMPTY = " "
LIVES = 3  # Кількість життів
START_SPEED = 0.5  # Початкова швидкість оновлення (сек)
SPEED_INCREASE = 0.05  # Зменшення затримки кожні 10 очок

# Завантаження найкращого рекорду
def load_high_score():
    if os.path.exists(LEADERBOARD_FILE):
        with open(LEADERBOARD_FILE, "r") as file:
            return int(file.read().strip())
    return 0

# Збереження нового рекорду
def save_high_score(score):
    with open(LEADERBOARD_FILE, "w") as file:
        file.write(str(score))

# Генеруємо смугу дороги
def generate_road():
    road = [EMPTY] * WIDTH
    rand_num = random.random()

    if rand_num < 0.4:  # 40% шанс появи перешкоди
        obstacle_pos = random.randint(0, WIDTH - 1)
        road[obstacle_pos] = OBSTACLE
    elif rand_num < 0.6:  # 20% шанс появи бонусу
        bonus_pos = random.randint(0, WIDTH - 1)
        road[bonus_pos] = BONUS

    return road

# Відображення гри
def display_game(road, car_position, score, high_score, lives):
    os.system("cls" if os.name == "nt" else "clear")  # Очищення екрану
    print(f"🏆 Рекорд: {high_score} | Очки: {score} | ❤️ Життя: {lives}")

    for row in road:
        print("| " + " | ".join(row) + " |")

    car_row = [" "] * WIDTH
    car_row[car_position] = CAR
    print("| " + " | ".join(car_row) + " |")

# Оцінка результату після гри
def get_rank(score):
    if score >= 50:
        return "🏎️ Легендарний гонщик!"
    elif score >= 30:
        return "🚗 Професійний водій!"
    elif score >= 10:
        return "🚙 Початківець-гонщик!"
    else:
        return "🛑 Новачок! Спробуй ще раз!"

# Головна функція гри
def main():
    car_position = 1  # Початкова позиція
    score = 0
    lives = LIVES
    speed = START_SPEED
    game_over = False
    high_score = load_high_score()

    # Генеруємо стартові ряди
    road = [generate_road() for _ in range(5)]

    while not game_over:
        display_game(road, car_position, score, high_score, lives)

        # Ввід користувача
        move = input("Керуй машиною (A - вліво, D - вправо, W - вперед): ").strip().upper()
        if move == "A" and car_position > 0:
            car_position -= 1
        elif move == "D" and car_position < WIDTH - 1:
            car_position += 1
        elif move != "W":
            continue  # Ігнорувати введення, якщо це не "W"

        # Перевірка на зіткнення
        if road[-1][car_position] == OBSTACLE:
            lives -= 1
            print("\n💥 Ти врізався! -1 життя!")
            if lives == 0:
                game_over = True
                break

        # Перевірка на бонуси
        if road[-1][car_position] == BONUS:
            score += 5
            print("\n⭐ Ти зібрав бонус! +5 очок!")

        # Оновлення дороги
        road.pop()  # Видаляємо останній ряд
        road.insert(0, generate_road())  # Додаємо новий ряд
        score += 1

        # Прискорення гри кожні 10 очок
        if score % 10 == 0:
            speed = max(speed - SPEED_INCREASE, 0.1)

        time.sleep(speed)  # Затримка для реалістичності

    # Оновлення рекорду
    print("\n🚨 Гра закінчена! 🚨")
    print(f"Твій рахунок: {score}")
    print(f"Рейтинг: {get_rank(score)}")

    if score > high_score:
        print("🎉 Новий рекорд! 🎉")
        save_high_score(score)

# Запуск гри
if __name__ == "__main__":
    main()
