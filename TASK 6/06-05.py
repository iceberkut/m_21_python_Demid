people = set()
pause = set()
n = int(input())
m = int(input())
k = int(input())
count = 0
for i in range(n + m + k):
    name = input()
    if name in people:
        count += 1
        pause.add(name)
    people.add(name)
if (n == k == m) and len(people) == n:
    print('NO')
else:
    if len(pause) + count > 0:
        if ((len(pause) + count) % 2 != 0):
            print((len(pause) + count) % 2)
        else:
            print((len(pause) + count) // 2)
    else:
        print('NO')
