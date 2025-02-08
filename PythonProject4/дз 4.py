import random

class Student:
    def __init__(self, name):
        self.name = name
        self.money = 100
        self.knowledge = 0
        self.energy = 50
        self.happiness = 50

    def study(self):
        if self.energy >= 10:
            self.knowledge += 10
            self.energy -= 10
            print(f"{self.name} вчився. Знання: {self.knowledge}, Енергія: {self.energy}")
        else:
            print(f"{self.name} занадто втомлений для навчання.")

    def work(self):
        if self.energy >= 15:
            self.money += 50
            self.energy -= 15
            print(f"{self.name} працював. Гроші: {self.money}, Енергія: {self.energy}")
        else:
            print(f"{self.name} занадто втомлений для роботи.")

    def relax(self):
        self.happiness += 10
        self.energy += 15
        print(f"{self.name} відпочиває. Щастя: {self.happiness}, Енергія: {self.energy}")

    def go_to_university(self):
        if self.energy >= 10:
            self.knowledge += random.randint(5, 15)
            self.energy -= 10
            print(f"{self.name} відвідав університет. Знання: {self.knowledge}, Енергія: {self.energy}")
        else:
            print(f"{self.name} занадто втомлений, щоб йти на пари.")

    def live_day(self, day):
        print(f"\nДень {day}: {self.name}")
        print(f"Гроші: {self.money} | Знання: {self.knowledge} | Енергія: {self.energy} | Щастя: {self.happiness}")

        if self.energy < 20:
            self.relax()
        elif self.money < 50:
            self.work()
        elif self.knowledge < 30:
            self.study()
        else:
            random.choice([self.study, self.work, self.relax, self.go_to_university])()

        if self.happiness <= 0 or self.energy <= 0 or self.money < -100:
            print("Гра закінчена.")
            return False
        return True


student = Student("Іван")
for day in range(1, 6):
    if not student.live_day(day):
        break