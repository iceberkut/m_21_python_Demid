words = input()
minx = words
maxx = words
y = 'ДА'
n = 'НЕТ'
while True:
    words = input()
    if words == 'стоп':
        if len(set(minx) - set(maxx)) == 0:
            print(y)
            break
        else:
            print(n)
            break
    if len(words) > len(maxx):
        maxx = words
    if len(words) < len(minx):
        minx = words
