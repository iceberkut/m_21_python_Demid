ok = ['']
i = 1


def print_without_duplicates(message):
    ok.append(message)
    global i
    if ok[i] != ok[i - 1]:
        print(message)
    i += 1
    return i


print_without_duplicates("Привет")
print_without_duplicates("Не могу до тебя дозвониться")
print_without_duplicates("Не могу до тебя дозвониться")
print_without_duplicates("Не могу до тебя дозвониться")
print_without_duplicates("Когда доедешь до дома")
print_without_duplicates("Ага, жду")
print_without_duplicates("Ага, жду")
