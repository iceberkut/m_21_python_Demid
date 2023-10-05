n = int(input())
towns = set()
for i in range(n):
    new_town = input()
    towns.add(new_town)
newest_town = input()

if newest_town in towns:
    print("TRY ANOTHER")
else:
    print("OK")
