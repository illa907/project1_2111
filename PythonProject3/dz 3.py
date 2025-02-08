import random


class Human:
    def __init__(self, name="Human", job=None, car=None, home=None, pet=None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.home = home
        self.car = car
        self.pet = pet

    def get_home(self):
        self.home = Home()

    def get_car(self):
        self.car = Auto(brands_of_car)

    def get_job(self):
        if self.car and not self.car.drive():
            self.to_repair()
            return
        self.job = Job(list_of_jobs)

    def get_pet(self, pet_name):
        self.pet = Pet(pet_name)

    def feed_pet(self):
        if self.pet:
            self.pet.eat()
            self.gladness += 5  # Людина стає щасливішою
        else:
            print("У мене немає домашньої тварини.")

    def play_with_pet(self):
        if self.pet:
            self.pet.play()
            self.gladness += 10
        else:
            print("У мене немає домашньої тварини.")

    def eat(self):
        if self.home.food <= 0:
            self.shopping("food")
        else:
            self.satiety = min(self.satiety + 5, 100)
            self.home.food -= 5

    def work(self):
        if self.car and not self.car.drive():
            if self.car.fuel < 20:
                self.shopping("fuel")
                return
            else:
                self.to_repair()
                return
        self.money += self.job.salary
        self.gladness -= self.job.gladness_less
        self.satiety -= 4

    def shopping(self, manage):
        if self.car and not self.car.drive():
            if self.car.fuel < 20:
                manage = "fuel"
            else:
                self.to_repair()
                return
        if manage == "fuel":
            print('Я купив паливо')
            self.money -= 100
            self.car.fuel += 100
        elif manage == "food":
            print("Я купив їжу")
            self.money -= 50
            self.home.food += 50
        elif manage == "delicacies":
            print("Ура! Смаколики!")
            self.gladness += 10
            self.satiety += 2
            self.money -= 15

    def chill(self):
        self.gladness += 10
        self.home.mess += 5

    def clean_house(self):
        self.gladness -= 5
        self.home.mess = 0

    def to_repair(self):
        print("Машину відремонтовано!")
        self.car.strenght += 100
        self.money -= 50

    def days_indexes(self, day):
        print(f"Сьогодні {day}-й день життя {self.name}")
        print(f"Гроші: {self.money}\nЩастя: {self.gladness}\nСитість: {self.satiety}")
        if self.home:
            print(f"Дім\nЇжа: {self.home.food}\nБезлад: {self.home.mess}")
        if self.car:
            print(f"Авто\nПаливо: {self.car.fuel}\nСтан: {self.car.strenght}")
        if self.pet:
            print(f"Домашня тварина: {self.pet.name}\nСитість: {self.pet.satiety}\nЩастя: {self.pet.gladness}")

    def is_alive(self):
        if self.gladness < 0:
            print("Депресія...")
            return False
        if self.satiety <= 0:
            print("Помер від голоду...")
            return False
        if self.money < -500:
            print("Банкрут!")
            return False
        return True

    def live(self, day):
        if not self.is_alive():
            return False
        if self.home is None:
            print("Поселився у будинку")
            self.get_home()
        if self.car is None:
            self.get_car()
            print(f"Купив авто: {self.car.brand}")
        if self.job is None:
            self.get_job()
            print(f"Отримав роботу: {self.job.job}")
        if self.pet is None:
            self.get_pet("Барсик")  # Людина заводить домашню тварину
            print(f"Завів домашню тварину: {self.pet.name}")

        self.days_indexes(day)
        dice = random.randint(1, 5)
        if self.satiety < 20:
            self.eat()
        elif self.gladness < 20:
            self.chill()
        elif self.money < 0:
            self.work()
        elif self.car.strenght < 15:
            self.to_repair()
        elif dice == 1:
            print("Час розслабитися!")
            self.chill()
        elif dice == 2:
            print("Йду на роботу")
            self.work()
        elif dice == 3:
            print("Прибираю дім")
            self.clean_house()
        elif dice == 4:
            print("Граюся з домашньою твариною")
            self.play_with_pet()
        elif dice == 5:
            print("Годую домашню тварину")
            self.feed_pet()


class Pet:
    def __init__(self, name):
        self.name = name
        self.satiety = 50
        self.gladness = 50

    def eat(self):
        self.satiety = min(self.satiety + 10, 100)
        print(f"{self.name} поїв! Ситість: {self.satiety}")

    def play(self):
        self.gladness = min(self.gladness + 10, 100)
        self.satiety -= 5
        print(f"{self.name} грається! Щастя: {self.gladness}, ситість: {self.satiety}")


class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.strenght = brand_list[self.brand]["strenght"]
        self.consumption = brand_list[self.brand]["consumption"]

    def drive(self):
        if self.strenght > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strenght -= 1
            return True
        else:
            print("Машина не може рухатися!")
            return False


brands_of_car = {
    "BMW": {"fuel": 100, "strenght": 100, "consumption": 6},
    "Lada": {"fuel": 50, "strenght": 40, "consumption": 10},
    "Volvo": {"fuel": 70, "strenght": 150, "consumption": 8},
    "Ferrari": {"fuel": 80, "strenght": 120, "consumption": 14},
}


class Home:
    def __init__(self):
        self.food = 0
        self.mess = 0


class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]["salary"]
        self.gladness_less = job_list[self.job]["gladness_less"]


list_of_jobs = {
    "Python developer": {"salary": 40, "gladness_less": 3},
    "Rust developer": {"salary": 70, "gladness_less": 1},
}

my_human = Human(name="Макс")
for day in range(1, 8):
    if not my_human.live(day):
        break