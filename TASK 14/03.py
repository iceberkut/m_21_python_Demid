def quarter(xcoord, ycoord):
    if xcoord > 0 and ycoord > 0:
        print('I четверть')
    elif xcoord > 0 and ycoord < 0:
        print('IV четверть')
    elif xcoord < 0 and ycoord < 0:
        print('III четверть')
    else:
        print('II четверть')


x = float(input('Введите координату x: '))
y = float(input('Введите координату y: '))
quarter(x,y)