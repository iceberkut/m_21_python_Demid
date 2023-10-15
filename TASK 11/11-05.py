line = input().split()
print(str('[' + ', '.join('"' + line[i] + '"' for i in range(len(line))) + ']'))
