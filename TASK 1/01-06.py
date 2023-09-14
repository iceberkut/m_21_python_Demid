first_q = input("Вы достаточно спите?")
second_q = input("Вы умеете учиться?")
if first_q == "да" and second_q == "да":
    print("Вас ждет хорошее будущее")
elif first_q == "да" and second_q == "нет":
    print("Вам следует научиться учиться")
elif first_q == "нет" and second_q == "да":
    print("Трудоголизм до хорошего не доведет")
elif first_q == "нет" and second_q == "нет":
    print("Жизнь впустую?")
else:
    print("Ответы должны быть да или нет")
