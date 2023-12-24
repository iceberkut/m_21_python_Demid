import sys
import random

c = 1
names = list(map(str.strip, sys.stdin))
random.shuffle(names)
for i in range(0, len(names)):
    if i == len(names) - 1:
        print(names[i], ' - ', names[0])
    else:
        print(names[i], ' - ', names[c])
        c += 1
