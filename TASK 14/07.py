def print_statistic(arr):
    arr.sort()
    print(len(arr))
    print(sum(arr) / len(arr))
    print(min(arr))
    print(max(arr))
    index = len(arr) // 2
    print(arr[index])


arr = [float(input()) for i in range(int(input()))]
print_statistic(arr)