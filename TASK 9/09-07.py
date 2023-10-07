flag = False
num = int(input())
foundsystem = []
inputsystem = []
for i in range(num):
    foundsystem.append(input())
num1 = int(input())
for i in range(num1):
    inputsystem.append(input())
for i in foundsystem:
    for j in inputsystem:
        if j in i:
            flag = True
        else:
            flag = False
            break
    if flag:
        print(i)
