import sys

data = list(map(str.strip, sys.stdin))
data = [a.strip() for a in data]
coment = list(filter(lambda word: word[0] == '#', data))
for i in coment:
    print(f'Line {data.index(i) + 1}: {i[1:].strip()}')
