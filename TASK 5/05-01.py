a = int(input())
b = int(input())  # b more than a
for i in range(a, b + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("buzzfizz")
    elif i % 5 == 0:
        print("buzz")
    elif i % 3 == 0:
        print("fizz")
    else:
        print(i)
