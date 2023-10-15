a = []
for i in range(int(input()[1:])):
    b = input()
    if '#' in b.split():
        f = b.index('#')
        b = ''.join(b[:f])
    a.append(b)

for i in range(len(a)):
    print(a[i])