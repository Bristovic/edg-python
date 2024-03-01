# first calendar
import calendar
print(calendar.calendar(2024))
calendar.prcal(2024)

# month calendar
print(calendar.month(2024, 3))
calendar.prmonth(2024, 3, 4, 2)

# set first weekday
calendar.setfirstweekday(calendar.SUNDAY)
calendar.prmonth(2024, 1)

calendar.setfirstweekday(2)
calendar.prmonth(2024, 1)

calendar.setfirstweekday(0)

# weekday function
print()
print(calendar.weekday(2024, 3, 1))  # returns 4 (Fri)
print()

# weekheader function, short weekday names
print(calendar.weekheader(3))
print(calendar.weekheader(1))
print()

# leap years
print(calendar.isleap(2024))  # returns True if year is leap year
print(calendar.leapdays(2020, 2024))  # returns no. leap days

# creating Calendar objects
c = calendar.Calendar(0)

# returns the number of weekday in week range
for weekday in c.iterweekdays():
    print(weekday, end=" ")
print()

# Calendar iterators: itermonthdates
# iterates and returns all dates in month as datetime.date objects
# AND any necessary on ends to make complete weeks
for date in c.itermonthdates(2024, 2):
    print(date, date.isoweekday())

# returns day of month numbers (extra zeros to complete weeks out range)
for day in c.itermonthdays(2019, 11):
    print(day)

# returns tuples, month no and week no
for day in c.itermonthdays2(2019, 11):
    print(day)

# returns tuple of year, motnh and day of month no
for day in c.itermonthdays3(2019, 11):
    print(day)

# returns days in tupes of year, month, day of month, day of week
for day in c.itermonthdays4(2019, 11):
    print(day)

# returns list of tuples, list is weeks, tuples monthday, weekday
for data in c.monthdays2calendar(2020, 12):
    print(data)
