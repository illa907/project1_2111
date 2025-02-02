import random


class Human:
    def __init__(self, name="Human", job=None, car=None, home=None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.home = home
        self.car = car

    def get_home(self):
        self.home = Home()

    def get_car(self):
        self.car = Auto(brends_of_car)

    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(list_of_jod)

    def eat(self):
        if self.home.food <= 0:
            self.shopping("food")
        else:
            if self.satiety >= 100:
                self.satiety = 100
            self.satiety += 5
            self.home.food -= 5


    def work(self):
        if self.car.drive():
            pass

        else:
            if self.car.fuel < 20:
                self.shopping("fuel")
                return
            else:
                self. to_repair()
                return
            self.money += self.job.salary
            self.gladness -= self.job.gladness_less
            self.satiety -= 4


    def shopping(self):
        if self.car.drive():
            pass

        else:
            if self.car.fuel < 20:
                manage = "fuel"
            else:
                self.to_repair()
                return
        if manage == "fuel":
            print('I buy fuel')
            self.money -= 100
            self.car.fuel += 100
        elif manage == "food":
            print("I buy food")
            self.money -= 50
            self.home.food += 50
        elif manage == "delicacies":
            print("Hooray! Delicacies!")
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
        self.car.strenght += 100
        self.money -= 50


    def days_indexes(self,day):
        print(f"Today is {day} of{self.name} life")
        print(f"Mone - {self.money}\nGladnes - {self.gladness}\nStiety - {self.satiety}")
        print(f"Home\nFood - {self.home.food}\nMess - {self.home.mess}")
        print(f"Car\nFuel - {self.car.fuel}\nStrenght - {self.strenght}")

    def is_alive(self):
        if self.gladness < 0:
            print("Depression")
            return False
        if self.satiety > 0:
            if self.money < -500:
                print("Bankrupt")
                return False


    def live(self, day):
        if self.is_alive() == False:
            return False
        if self.home is None:
            print("Settled in a house")
            self.get_home()
        if self.car is None:
            self.get_home()
        if self.car is None:
            self.get_car()
            print(f"I buy car {self.car.brend}")
        if self.job is None:
            self.get_job()
            print(f"I get a job - {self.job.job}")
        self.days_indexes(day)
        dice = random.randint(1,4)
        if self.satiety < 20:
            self.eat()
        elif self.gladness < 20:
            self.chill()
        elif self.money < 0:
            self.work()
        elif self.car.strenght < 15:
            self.to_repair()
        if dice == 1:
            print("Lets chill")
            self.chill()
        elif dice == 2:
            print("Go to work")
            self.work()
        elif dice == 3:
            print("Cleaning time")
            self.clean_house()
        elif dice == 4:
            print("Time to reats")
            self.shopping("delicacies")




class Auto:
    def __init__(self, brend_list):
        self.brend = random.choice(list(brend_list))
        self.fuel = brend_list[self.brend]["fuel"]
        self.strenght = brend_list[self.brend]["strenght"]
        self.consumption = brend_list[self.brend]["consumption"]

    def drive(self):
        if self.strenght > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strenght -= 1
            return True
        else:
            print("The car cannot move!")
            return False


brends_of_car = {
    "BMW": {"fuel": 100, "strenght": 100, "consumption": 6},
    "Lada": {"fuel": 50, "strenght": 40, "consumption": 10},
    "Volvo": {"fuel": 70, "strenght": 150, "consumption": 8},
    "Ferrari": {"fuel": 80 , "strenght": 120, "consumption": 14},
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


list_of_jod = {
    "Java developer": {"salary": 50, "gladness_less": 3},
    "Python develope": {"salary": 40, "gladness_less": 3},
    "C++ develope": {"salary": 45, "gladness_less": 25},
    "Rust developer": {"salary": 70, "gladness_less": 1},
}

my_human = Human(name="Skubidy")
for day in range(1, 8):
    if my_human.live(day) == False:
        break







