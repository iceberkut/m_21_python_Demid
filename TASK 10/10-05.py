n = int(input())
names = []
for i in range(n):
    names.append(input())

num = int(input("Step"))
repeats = int(input("Rounds"))

for j in range(repeats):
    del names[num - 1::num]
print("".join(names))
