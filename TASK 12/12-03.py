num = int(input())
nums = list()
for i in range(num):
    s = int(input())
    nums.append(s)
first = int(input())
second = int(input())
print(sum(nums[first - 1:second]))
