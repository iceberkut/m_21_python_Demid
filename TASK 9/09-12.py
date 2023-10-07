n = input()
s = []
s1 = []
b = 0
lot, itogo = int(n[:4]), int(n[4:])
for i in range(lot):
    a = input()
    price, kolvo, summ = int(a[0:7]), int(a[8:12]), int(a[13:18])
    if price * kolvo != summ:
        s.append(i + 1)
    summ1 = kolvo * price
    s1.append(summ1)
for i in s1:
    b += i
print(itogo - b)
for i in s:
    print(i, end=' ')
