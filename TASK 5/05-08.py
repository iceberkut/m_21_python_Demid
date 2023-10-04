cat_in_phrase = False
count = 0
phrase = ''
number = 0
first = -1
while phrase != 'СТОП':
    phrase = input()
    count += 1
    while not (cat_in_phrase):
        if ('Кот' in phrase) or ('кот' in phrase):
            cat_in_phrase = True
            first = count
            number += 1
        break
print(number, " ", first)
