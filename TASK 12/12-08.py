text = input().lower()
first = 0
second = 0
count = 0
for i in range(len(text)):
    first = text.count(text[i])
    if first > second:
        count = i
        second = first
print(text[count])
