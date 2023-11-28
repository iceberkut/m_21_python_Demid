def fyb(i):
    fib1 = 1
    fib2 = 1
    j = 2
    if i == 1 or i == 2:
        fib_sum = 1
    while j < i:
        fib_sum = fib2 + fib1
        fib1 = fib2
        fib2 = fib_sum
        j = j + 1
    return fib_sum


def golden_ratio(i):
    g = fyb(i + 1) / fyb(i)
    print(g)


golden_ratio(int(input()))