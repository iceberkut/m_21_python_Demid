space = int(input())
star = 1
while space > 0:
    print(' ' * space + 'I' * star)
    star += 2
    space -= 1
