n = int(input())
a = []
for i in range(n):
    a.append(input())

k = int(input())
for i in a:
    if k <= len(i):
        print(i[k - 1], end='')
