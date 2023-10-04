num = int(input())
euro = "Евразия"
osta = "Остазия"
for i in range(num):
    question = input()
    if question == "С кем война?":
        print(euro)
    elif question == "С кем мир?":
        print(osta)
    if question == "Меняем":
        new = euro
        euro = osta
        osta = new
