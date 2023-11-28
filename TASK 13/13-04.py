num = int(input())
point = []
for i in range(num):
    num, m = input().split()
    point.append((int(num), int(m)))
result = []
while len(point) > 0:
    same_route = []
    a = point[0][0] // 10 * 10
    b = point[0][1] // 10 * 10
    for i in range(0, len(point)):
        x = point[i][0] // 10 * 10
        y = point[i][1] // 10 * 10
        if x == a and y == b:
            same_route.append(point[i])
    result.append(same_route)
    point = list(filter(lambda p: p not in same_route, point))
quant = [len(result[i]) for i in range(len(result))]
qmax = max(quant)
print(qmax)