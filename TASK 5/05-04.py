num = int(input())
i = 0
while i < num:
    string1 = input()
    if "кот" or "Кот " in string1:
        print("мяу")
        break
    else:
        i += 1
        if i == num:
            print("нет")
