text = input()
count = 0
for char in text:
    count += 1
    if count % 5 == 0:
        print(char)
if count < 5:
    print("НЕТ")
