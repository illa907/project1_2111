ch1 = float(input("Ведіть перше чісл"))
ch2 = float(input("Ведіть друге чісл"))

try:
    result = ch1/ch2
    print(result)
except:
    print(f"Ви намагалися поділити {ch1} на {ch2} і отримали помилку!")
    if ch2 == 0:
        print("На 0 ділити незя")
else:
    print("Розрахунки завершено")

