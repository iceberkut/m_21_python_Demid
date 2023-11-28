phones = {}
for _ in range(int(input())):
    val, key = input().split()
    if key in phones:
        phones[key].append(val)
    else:
        phones[key] = [val]

for _ in range(int(input())):
    key = input()
    print(*phones.get(key, ['Нет в телефонной книге']))
