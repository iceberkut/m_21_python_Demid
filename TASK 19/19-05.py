gl_eng = ['a', 'e', 'i', 'o', 'u', 'y']
sog_eng = ['b', 'c', 'd', 'f', 'g', 'h',
           'j', 'k', 'l', 'm', 'n', 'p',
           'q', 'r', 's', 't', 'v', 'w',
           'x', 'z']


def ask_password(login, password, success, failure):
    gl_password = list(map(lambda x: x.lower(), filter(lambda x: x.lower() in gl_eng, password)))
    sog_password = list(map(lambda x: x.lower(), filter(lambda x: x.lower() in sog_eng, password)))
    sog_login = list(map(lambda x: x.lower(), filter(lambda x: x.lower() in sog_eng, login)))

    if len(gl_password) == 3 and (sog_password == sog_login):
        success(login)
        return (True, '')
    if len(gl_password) != 3 and (sog_password == sog_login):
        failure(login, "Wrong number of vowels")
        return (False, 'Wrong number of vowels')
    if len(gl_password) == 3 and (sog_password != sog_login):
        failure(login, "Wrong consonants")
        return (False, "Wrong consonants")
    if len(gl_password) != 3 and (sog_password != sog_login):
        failure(login, "Everything is wrong")
        return (False, "Everything is wrong")


def success(login):
    return


def failure(login, mes):
    return


def main(login, password):
    e, mes = ask_password(login, password, success, failure)
    if e:
        print('Привет, ' + login.lower() + '!')
    else:
        print('Кто-то пытался притвориться пользователем ' + login.lower() + ', но в пароле '
                                                                             'допустил ошибку: ' + mes.upper() + '.')


main("anastasia", "nsyatos")
