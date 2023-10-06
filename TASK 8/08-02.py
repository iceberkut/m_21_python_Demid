n = input()
m = input()
bulls = 0
cows = 0
for i in set(n) & set(m):
    if n.index(i) == m.index(i):
        bulls += 1
    else:
        cows += 1
print(bulls, cows)
