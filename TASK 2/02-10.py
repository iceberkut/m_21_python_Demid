firstn = float(input())
secondn = float(input())
mark = input()
if mark == "-":
    print(firstn - secondn)
elif mark == "+":
    print(firstn + secondn)
elif mark == "*":
    print(firstn * secondn)
elif mark == "/":
    if secondn != 0:
        print(firstn / secondn)
    elif secondn == 0:
        print('888888')
else:
    print('888888')
