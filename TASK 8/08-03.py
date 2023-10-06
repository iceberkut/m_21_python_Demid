str1 = list(input())
for i in str1:
    if i not in '1234567890_qwertyuiopasdfghjklzxcvbnm':
        print(f"Неверный символ {i}")
        break
