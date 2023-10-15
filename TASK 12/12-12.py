line = input().lower()
num = 0
for i in range(len(line)):
    if line.count(line[i]) > num:
        num = line.count(line[i])

print(num)
