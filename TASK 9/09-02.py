num_of_str = int(input())
text = []
for i in range(num_of_str):
    text.append(input())

found = input()
for i in text:
    if found in i:
        print(i)
