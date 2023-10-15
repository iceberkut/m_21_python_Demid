text = input()
septext = text.split(" ")
secret_message = []
for i in range(len(septext)):
    if (i+1) % 3 == 0:
        secret_message.append(septext[i])
print(" ".join(char for char in secret_message))
