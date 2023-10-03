sum = 0
cnt = 1
num = 1
while num != 0:
    num = int(input())
    sum += num
    cnt += 1
    if sum >= 10:
        print(cnt - 1)
        break
