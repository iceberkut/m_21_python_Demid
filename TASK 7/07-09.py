text = input()
num = int(input())
if 0 < num <= len(text):
    print(text[num - 1])
else:
    print('ОШИБКА')
