letter = input().upper()
line = input().split()
for i in range(len(line)):
    if letter in line[i] or letter.lower() in line[i]:
        print(line[i])
