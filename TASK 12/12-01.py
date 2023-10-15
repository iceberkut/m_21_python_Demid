num = int(input())
num_lines = []
for i in range(num):
    line = input()
    temp = line.find('кот')
    if temp != -1:
        print(i + 1, temp + 1)

