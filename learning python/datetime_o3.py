
from datetime import datetime
from datetime import date
from datetime import time

today = date.today()
print("today's date is", today)

print("component of today", today.day, today.month, today.year)
print("today's week # is" , today.weekday())

days = ["mon", "tue", "wed", "thur", "fri", "sat", "sun"]
print("which day of the week is today: ", days[today.weekday()])

today = datetime.now()
print("the current time is: ", today)

t = datetime.time(datetime.now())
print("the time is:", t)

