num = int(input())
while str(num)[0] != '1' and num <= 1000000000:
    num = num * int(str(num)[0])
print(num)
