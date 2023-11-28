import math


def discriminant(a, b, c):
    x = (b ** 2) - 4 * a * c
    return x


def larger_root(p, q):
    x1 = (-p + math.sqrt(discriminant(1, p, q))) / 2
    return x1


def smaller_root(p, q):
    x2 = (-p - math.sqrt(discriminant(1, p, q))) / 2
    return x2


def main():
    p, q = float(input()), float(input())
    print(discriminant(1, p, q))
    if discriminant(1, p, q) < 0:
        print('нет корней')
    else:
        print(smaller_root(p, q), larger_root(p, q))


main()



