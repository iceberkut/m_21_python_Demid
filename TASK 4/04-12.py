num_of_nums = int(input())
count = 0
for index in range(num_of_nums):
    num = int(input())
    if index % 2 == 0:
        count += num
    else:
        count -= num
print(count)
