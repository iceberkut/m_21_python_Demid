cat_in_phrase = False
count = 0
phrase = ''
while phrase != 'СТОП':
    phrase = input()
    count += 1
    while not (cat_in_phrase):
        if ('Кот' in phrase) or ('кот' in phrase):
            cat_in_phrase = True
            number = count
        break
    if cat_in_phrase:
        print(number)
        break
else:
    print(-1)
   