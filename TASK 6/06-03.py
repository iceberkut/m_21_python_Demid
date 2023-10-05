english_students = int(input())
german_students = int(input())
eng = set()
ger = set()
for v in range(english_students):
    str1 = input()
    eng.add(str1)
for n in range(german_students):
    str2 = input()
    ger.add(str2)
count = len(eng ^ ger)

if count > 0:
    print(count)
else:
    print("No")
