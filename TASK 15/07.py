def find_mountain(heightsMap):
    row = -1
    maxValue = 0
    for i in heightsMap:
        if max(i) > maxValue:
            maxValue = max(i)
    for i in heightsMap:
        row += 1
        column = -1
        for j in i:
            column += 1
            if j == maxValue:
                return row, column


a = [[1, 3, 1], [3, 2, 5], [2, 2, 2]]
print(find_mountain(a))

a = [[2, 4, 2, 3, 2], [3, 2, 3, 4, 3]]
row, col = find_mountain(a)
print(a[row][col])


