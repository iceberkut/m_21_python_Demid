dayBirth = {
    'янв': [],
    'фев': [],
    'мар': [],
    'апр': [],
    'май': [],
    'июн': [],
    'июл': [],
    'авг': [],
    'сен': [],
    'окт': [],
    'ноя': [],
    'дек': [],
}
for i in range(int(input())):
    about = input().split()
    name = about[0]
    month = about[2]
    dayBirth[month].append(name)
    dayBirth[month].sort()
for u in range(int(input())):
    qwerty = input()
    print(' '.join(dayBirth[qwerty]))
