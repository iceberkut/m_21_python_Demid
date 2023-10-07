n = int(input())
soups = ['щи', 'борщ', 'щавелевый суп', 'овсяный суп?', 'суп по-чабански']
for i in range(n):
    print(soups[i % 5])