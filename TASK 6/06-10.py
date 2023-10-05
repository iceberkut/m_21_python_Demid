s = set()
g = set()
n = int(input())
for i in range(n):
    s.add(input())
n = 0
n = int(input())
for i in range(n):
    d = int(input())
    for a in range(d):
        g.add(input())
q = list(s - g)
v = sorted(q)
print(*v, sep='\n')
