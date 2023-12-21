def find_farthest_orbit(list_of_orbits):
    sp = []
    for i in list_of_orbits:
        sp.append(i[0] * i[1])
    ind = sp.index(max(sp))
    return list_of_orbits[ind]


orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits))
