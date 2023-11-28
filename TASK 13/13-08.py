while True:
    N = int(input())
    if 1 <= N <= 1000:
        break
    print('1≤N≤1000 !')

slovar = {k[0]: ' '.join(k[1:]) for k in [input().split() for i in range(N)]}

while True:
    M = int(input())
    if 1 <= M <= 100:
        break
    print('1≤M≤100 !')

slova = [input() for i in range(M)]

[print(slovar.setdefault(i, 'Нет в словаре')) for i in slova]