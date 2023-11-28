def triangle(a,b,c):
    if a + b <= c or a + c <= b or b + c <= a or c + a <= b:
        print('Это не треугольник')
    else:
        print('Это треугольник')


a = float(input())
b = float(input())
c = float(input())
triangle(a,b,c)