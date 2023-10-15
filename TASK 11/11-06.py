num_of_lines = int(input())
text = [input() for i in range(num_of_lines)]
print(str(", ".join([text[i] for i in range(len(text)) if "лук" not in text[i]])))
