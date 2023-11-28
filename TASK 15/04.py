def average(values):
    if values:
        return int(sum(values) / len(values))
    else:
        return 0


print(average([1, 2, 3, 4, 5]))
