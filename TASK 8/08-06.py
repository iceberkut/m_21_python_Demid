a = int(input())
n = int(input())
for i in range(n):
    text = input()
    if len(text) <= a:
        print(text)
    else:
        print(text[:a - 3] + '...')
