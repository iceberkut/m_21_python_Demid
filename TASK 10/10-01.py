num = int(input())
arr = []
ban = 0
for o in range(num):
    arr.append(int(input()))
main = int(input())
ban = 0
for i in arr:
    for j in arr:
        if i * j == main:
            ban = 1
            break
if ban:
    print("ДА")
else:
    print("НЕТ")
