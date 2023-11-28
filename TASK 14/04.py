def who_are_you_and_hello():
    while True:
        text = input()
        if text.count(' ') == 0 and text.isalpha() and text.istitle():
            print(text)
            break


who_are_you_and_hello()