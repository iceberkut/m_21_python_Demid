start = 1
stop = 1000
while True:
    bin_division = (start + stop) // 2
    result = input(f"Твое число >,< или = числу {bin_division} ?")
    if result == "=":
        print(f'это число {bin_division}')
        break
    elif result == ">":
        start = bin_division
    else:
        stop = bin_division