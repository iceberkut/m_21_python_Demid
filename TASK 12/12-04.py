nums = [int(i) for i in input().split()]
range1 = [int(i) for i in input().split()]
squares = 0
for i in range(range1[0], range1[1] + 1):
    squares += nums[i] * nums[i]
print(squares)
