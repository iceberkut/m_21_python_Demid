from random import sample
import string
symbols = 'ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnpqrstuvwxyz23456789'

def generate_password(m):
    return ''.join(sample(symbols, m))

def main(n, m):
    a = set()
    while len(a) < n:
        a.add(generate_password(m))
    return a

print("Случайный пароль из 7 символов:", generate_password(7))
print("10 случайных паролей длиной 15 символов:")
print(*main(10, 15), sep="\n")
