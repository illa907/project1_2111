def checker(function):
    def checker(*args, **kwargs):
        try:
            result = function(*args, **kwargs)
        except Exception as exc:
            print(f"We have a problem - {exc}")
        else:
            print(f"No problem - {result}")

    return checker


def calculate(experession):
    return eval(experession)


calculate = checker(calculate)
calculate("2+2")