first = set()
second = set()
c = input()
while c != '':
    first.add(c)
    c = input()
first.add(c)
c1 = input()
while c1 != '':
    second.add(c1)
    c1 = input()
intersection = first & second
if not intersection:
    print('EMPTY')
else:
    for i in intersection:
        print(i)
