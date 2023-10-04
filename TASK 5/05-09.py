last = ''
num_of_strings = int(input())
condition = False
for i in range(num_of_strings):
    string = input().upper()
    if 'КОТ' in string:
        condition = True
    if 'ПЁС' in string:
        condition = False
if condition:
    print('МЯУ')
else:
    print('НЕТ')
