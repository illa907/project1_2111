import inspect


class Human:
    def __init__(self, age, heinght, name='John'):
        self.age = age
        self.name = name
        self.secondname = 'Wick'


sig = inspect.signature(Human)
for parameter in sig.parameters.values():
    print(parameter.name, parameter.default)
