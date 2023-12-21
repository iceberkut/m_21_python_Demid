print(sum(map(lambda x: x ** 2, filter(lambda x: not x % 9, range(10, 100)))))
