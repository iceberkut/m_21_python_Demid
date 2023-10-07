numbers = []
n = int(input())
for i in range(n):
    numbers.append(int(input()))
for i in range(n - 1):
    print(numbers[i] + numbers[i + 1])
