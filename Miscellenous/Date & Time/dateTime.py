import calendar
import time
from datetime import date, time as t, datetime

print(time.time())
print(time.localtime())
print(time.localtime(time.time()))
print(time.asctime(),"\n")

print(calendar.month(2025,8))

print("Date", date(2025, 8, 1))
print("Time", t(12, 30, 45))
print(datetime(2025, 8, 1, 12, 30, 45))