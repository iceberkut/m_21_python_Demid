klass = int(input())

for i in range(klass):
    x = int(input())
    klass_oh = list()
    for j in range(x):
        klass_oh.append(input().split()[1])
    print(any(lambda w: '5' in klass_oh))
