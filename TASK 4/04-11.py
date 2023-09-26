iq = 0
sum_iq = 0
for ix in range(1, int(input()) + 1):
    iq = int(input())
    average = (iq + sum_iq) / ix
    sum_iq += iq
    if iq == average:
        print('0')
    elif iq > average:
        print('>')
    elif iq < average:
        print('<')
