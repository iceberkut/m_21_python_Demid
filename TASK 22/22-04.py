from datetime import datetime, timedelta

start = str('01.09.2019')
end = int(input())

date = datetime.strptime(start, "%d.%m.%Y")
modified_date = date + timedelta(days = end)
print(datetime.strftime(modified_date, "%d.%m"))
