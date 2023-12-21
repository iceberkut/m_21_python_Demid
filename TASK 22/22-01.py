import random


def make_bingo():
    numbers = random.sample(range(1, 76), 24)
    numbers.insert(12, 0)
    rows = [numbers[i:i + 5] for i in range(0, 25, 5)]
    return tuple(rows)


result = make_bingo()
print(result)
