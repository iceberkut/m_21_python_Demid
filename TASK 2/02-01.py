town_1 = input("Town Jul")
town_2 = input("Town Aug")
if (town_1 == "Тула" and town_2 == "Тула") or (town_1 == "Пенза" and town_2 == "Пенза") \
        or (town_1 == "Тула" and town_2 == "Пенза") or (town_1 == "Пенза" and town_2 == "Тула"):
    print("НЕТ")
elif town_1 == "Тула" or town_2 == "Тула" or town_1 == "Пенза" or town_2 == "Пенза":
    print("ДА")
else:
    print("НЕТ")
