from random import randint
symbols = 'ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnpqrstuvwxyz23456789'

def generate_password(m):
    a = set()
    while len(a) < m:
        a.add(randint(0, len(symbols) - 1))
    str = ''
    for x in a:
        str += symbols[x]
    return str

def main(n, m):
    return [generate_password(m) for _ in range(n)]

print("Случайный пароль из 7 символов:", generate_password(7))
print("10 случайных паролей длиной 15 символов:")
print(*main(10, 15), sep="\n")
