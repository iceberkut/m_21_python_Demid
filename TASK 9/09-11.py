white_list = []
for i in range(int(input())):
    white_list.append(input())
search = []
for j in range(int(input())):
    search.append(input())
for k in search:
    if k in white_list:
        print(k)
