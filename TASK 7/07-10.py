letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
shag = int(input())
sms = input().upper()
cipher = ''
for i in sms:
    place = letters.find(i)
    new_place = place + shag
    if i in letters:
        cipher += letters[new_place]
    else:
        cipher += i
print(cipher)
