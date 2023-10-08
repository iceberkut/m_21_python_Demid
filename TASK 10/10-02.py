list1 = []
list2 = []
num = int(input())
for i in range(num):
    line = input()
    if "4" in line or "5" in line:
        list1.append(line)
        list2.append(line)
    else:
        list2.append(line)
    continue

for j in range(len(list2)):
    print(list2[j])

print(" ")

for k in range(len(list1)):
    print(list1[k])
