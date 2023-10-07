N = int(input())
s = []
for i in range(N):
    num = int(input())
    s.append(num)
p = int(input())
q = int(input())
result = sum(s[p - 1:q])
print(result)
