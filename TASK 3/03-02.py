password = input()
pass_2 = input()
if len(password) <= 8:
    print("Короткий пароль!!!")
else:
    if password != pass_2:
        print("Различны пароли!!!")
    else:
        print("ОК")

