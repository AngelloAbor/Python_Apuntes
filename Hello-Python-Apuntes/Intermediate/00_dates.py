### dates ###

from datetime import datetime
# datetime.date(year, month, day)

now = datetime.now()


def print_date(date):
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.year)
    print(date.month)
    print(date.timestamp())


print_date(now)

timestamp = now.timestamp()

year = datetime(2025, 1, 1)

print_date(year)


from datetime import time

current_time = time(9, 30, 45)

print(current_time.hour)
print(current_time.minute)
print(current_time.second)


from datetime import date

current_date = date.today()

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(current_date.year, current_date.month + 1, current_date.day)

print(current_date)

diff = year - now
print(diff)

diff = year.date() - current_date
print(diff)

from datetime import timedelta

start_timedelta = timedelta(weeks=5,days=7,seconds=60,microseconds=1000)

end_timedelta = timedelta(weeks=8,days=24,seconds=60,microseconds=1000)

print(end_timedelta - start_timedelta)
print(end_timedelta + start_timedelta)