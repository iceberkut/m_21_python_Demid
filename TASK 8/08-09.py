num = int(input())
while num > 0:
    num -= 1
    word = input()
    if word[0:2] == '%%':
        print(word[2:])
    elif word[0:4] == '####':
        continue
    else:
        print(word)
