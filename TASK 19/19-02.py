def simple_map(transformation, values):
    for i in values:
        yield transformation(i)


values = [1, 3, 1, 5, 7]
print(*simple_map(lambda x: x + 5, values))
