import datetime
from math import sin, pi

def bio_rhythm(P, T):
    return round(sin(2.0 * pi * T / P) * 100, 2)

birthday = input()
y0, m0, d0 = map(int, birthday.split('.'))
date0 = datetime.date(d0, m0, y0)
biorhythm = input()
y, m, d = map(int, biorhythm.split('.'))
date = datetime.date(d, m, y)
T = (date - date0).days
print(bio_rhythm(23, T))
print(bio_rhythm(28, T))
print(bio_rhythm(33, T))
