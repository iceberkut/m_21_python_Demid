login = input("Enter LOGIN ")
email = input("Enter EMAIL ")
if "@" in login:
    print("Incorrect LOGIN")
elif "@" not in email:
    print("Incorrect EMAIL")
else:
    print("OK")
