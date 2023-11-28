def ask_password():
    flag = False
    for i in range(3):
        password = input()
        if password == 'password':
            flag = True
            print('Пароль принят')
    if not flag:
        print('В доступе отказано')


ask_password()