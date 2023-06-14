import datetime
from datetime import date
datetime = datetime.datetime.utcnow()
print("Current time: ",datetime)

#to get current date
current_date = date.today()
print("Current date: ",current_date)

print(dir(datetime))

today = date.today()
print("Current date : ",today)
print("Current year: ",today.year)
print("Current month: ",today.month)
print("Current day: ",today.day)