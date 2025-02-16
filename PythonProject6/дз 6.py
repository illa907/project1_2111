pip install colorama


import colorama
import inspect

attributes = dir(colorama)
print("Усі атрибути та методи colorama:\n", attributes)

print("\nОсновні атрибути та їх значення:")
print(f"colorama.Fore.RED: {colorama.Fore.RED}")
print(f"colorama.Back.GREEN: {colorama.Back.GREEN}")
print(f"colorama.Style.BRIGHT: {colorama.Style.BRIGHT}")

print("\nФункція ініціалізації:")
print(inspect.getsource(colorama.init))

print("\nФункція reset:")
print(inspect.getsource(colorama.ansi.AnsiCodes.reset))
