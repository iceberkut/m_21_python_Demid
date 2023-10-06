a = input()
tr = 0
k = 0
mx = 0
for i in a:
    if i == 'о' and k == 0:
        tr += 1
    elif i == 'о' and k != 0:
        tr = 1
        k = 0
    else:
        k = 1
    if tr > mx:
        mx = tr
print(mx)
