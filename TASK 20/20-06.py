import sys


def num_code(char):
    char = char.upper()
    return ord(char) - ord("A") + 1


print(*sorted([elem.strip() for elem in sys.stdin], key=lambda k: (sum([num_code(i) for i in k]), k)), sep="\n")
