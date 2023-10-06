town1 = input()
town2 = input()
while town1[-1] == town2[0]:
    town1 = input()
    town2 = input()
    if town1[-1] != town2[0]:
        print(town2)
        break
