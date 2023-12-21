data = """
import sys   
for line in sys.stdin:   
    # rstrip(’\n’) "отрезает" от строки line, идущий справа символ перевода строки,  
    # ведь print сам переводит строку   
    print(line.rstrip(’\n’))
"""

count = list(map(lambda x: x.lstrip().startswith("#"), data.split("\n"))).count(True)
print(count)
