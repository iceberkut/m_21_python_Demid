home_biblion = set()
home_biblion_N = int(input())
home_task = set()
home_task_M = int(input())
for i in range(home_biblion_N):
    book = input()
    home_biblion.add(book)
for i in range(home_task_M):
    book = input()
    home_task.add(book)
    if book in home_biblion:
        print('YES')
    else:
        print('NO')
