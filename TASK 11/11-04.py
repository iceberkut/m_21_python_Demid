nums = input().split()
print(' '.join([str(int(i) ** 2) for i in nums if int(i) % 2 != 0 and int(i) ** 2 % 10 != 9]))
