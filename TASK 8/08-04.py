n = int(input())
vert = 'ABCDEFGHI'
k = 0
if n < 10:
    for i in range(n, 0, -1):
        for j in vert[0:n]:
            print(j, i, sep='', end=' ')
            if j == vert[n - 1]:
                print()
else:
    print("Много")
