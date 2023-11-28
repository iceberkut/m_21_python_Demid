daily_food = [0, 150, 150]


def count_food(lst: list):
    return sum([daily_food[i - 1] for i in lst])



print(count_food([1]))
print(count_food([2, 3]))
