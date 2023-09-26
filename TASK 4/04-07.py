count = 0
number = int(input())
for i in range(1, number + 1):
    if number % i == 0:
        if i != number:
            print(str(i), end=" ")
        if i == number:
            print(str(i))
        count += 1
if number == 1:
    print("НЕТ")
elif count == 2:
    print("ПРОСТОЕ")
else:
    print("НЕТ")
