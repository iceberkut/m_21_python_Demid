while True:
    password = input("password")
    passTwo = input("password again:")
    approve = True
    if len(password) < 8:
        approve = False
        print("Короткий")
    if password != passTwo:
        approve = False
        print("Различаются")
    if "123" in password:
        approve = False
        print("Простой")
    if approve:
        break
print("OK")
