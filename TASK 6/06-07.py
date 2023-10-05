from collections import Counter
n = int(input())
sep = []
for i in range(n):
    for j in range(int(input())):
        a = input()
        sep.append(a)
dict1 = dict(Counter(sep))
for elem in dict1:
    if dict1.get(elem) == n:
        print(elem)
        