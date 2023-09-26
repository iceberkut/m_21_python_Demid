start = 1
for _ in range(6):
    numbers = int(input())
    if numbers != 0:
        start *= numbers
print(start)
