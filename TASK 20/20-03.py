import sys

x = sys.stdin.readlines()
sum = 0
b = 0
if len(x) == 0:
    print("-1")
else:
    for n in range(0, len(x)):
        sum += int(x[j])
        b += 1
    answer = sum / b
    print(answer)
