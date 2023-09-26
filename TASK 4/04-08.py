number = int(input())
while number >= 0:
    print(f"Осталось секунд: {number}")
    number -= 1
    if number < 0:
        print("ПУСК!")
