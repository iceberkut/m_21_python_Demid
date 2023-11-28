def transpose(matrix):
    matrix[:] = [list(x) for x in zip(*matrix)]


def main():
    matrix = [[1, 2], [3, 4]]
    transpose(matrix)
    for line in matrix:
        print(*line)


if __name__ == "__main__":
    main()