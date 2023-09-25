def coins(number):
    while number > 7:
        number /= 8
    print(number.__floor__())


coins(129)
