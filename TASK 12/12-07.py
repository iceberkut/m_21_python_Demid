line = []
s = input().split()
for x in s:
    if x == '+':
        g = line.pop()
        z = line.pop()
        line.append(g + z)
    elif x == '-':
        g = line.pop()
        z = line.pop()
        line.append(z - g)
    elif x == '*':
        g = line.pop()
        z = line.pop()
        line.append(g * z)
    else:
        line.append(int(x))
print(line[0])
