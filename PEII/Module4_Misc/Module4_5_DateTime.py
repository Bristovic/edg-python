# datetime module
import datetime as dt
import time
#
# date
today = dt.date.today()

print("Today:", today)
print("Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)

# timestamps
timestamp = time.time()
print("Timestamp:", timestamp)

d = dt.date.fromtimestamp(timestamp)
print("Date:", d)

# creating date from string according to format
d = dt.date.fromisoformat("2022-10-04")
print(d)

# replace method
d = d.replace(year=1992, month=1)
print(d)

# weekday method (Mon=0, Sun=6)
print(d.weekday())

# isoweekday method (Mon=1, Sun=7)
print(d.isoweekday())

# datetime time class to create time
t = dt.time(14, 53, 20, 1)
print("Time:", t)
print("Hour:", t.hour)
print("Minute:", t.minute)
print("Second:", t.second)
print("Microsecond:", t.microsecond)


# the time module
# sleep function
class Student:
    def take_nap(self, seconds):
        print("I'm very tired. I have to take a nap. See you later.")
        time.sleep(seconds)
        print("I slept fantastically!")


student = Student()
student.take_nap(0.1)

# ctime function
timestamp = time.time()
print(time.ctime(timestamp))
print(time.ctime())

# struct_time class
print(time.timezone)


# converting timestamp to struct_time objects
timestamp = 1572879180
print(time.gmtime(timestamp))
print(time.localtime(timestamp))

t = time.localtime(timestamp)
print(t.tm_zone)
print(t.tm_gmtoff)

# asctime and mktime
st = time.gmtime(timestamp)

print(time.asctime(st))
print(time.mktime((2018, 11, 4, 14, 53, 0, 0, 308, 0)))

# datetime object
dati = dt.datetime(2019, 11, 4, 14, 53)

print("Datetime:", dati)
print("Date:", dati.date())
print("Time:", dati.time())

# datetime and returning current time
print("today:", dt.datetime.today())
print("now:", dt.datetime.now())

# datetime and timestamp
dooti = dt.datetime(2020, 10, 4, 14, 55)
print("Timestamp:", dooti.timestamp())

# date and time formatting
d = dt.date(2020, 1, 4)
print(d.strftime('%Y/%m/%d'))

t = dt.time(14, 53)
print(t.strftime("%H:%M:%S"))

deet = dt.datetime(2020, 11, 4, 14, 53)
print(deet.strftime("%y/%B/%d %H:%M:%S"))

# the strftime() function in time module
timestamp = 1572879180
st = time.gmtime(timestamp)

# provide struct_time object
print(time.strftime("%Y/%m/%d %H:%M:%S", st))
# no struct_time means local time
print(time.strftime("%Y/%m/%d %H:%M:%S"))

# the strptime() method in datetime to get date from string
print(dt.datetime.strptime("2019/11/04 14:53:00", "%Y/%m/%d %H:%M:%S"))

# analogous strptime method in time to create struct_time object
print(time.strptime("2019/11/04 14:53:00", "%Y/%m/%d %H:%M:%S"))

# date and time operations: timedelta
d1 = dt.date(2020, 11, 4)
d2 = dt.date(2019, 11, 4)

print(d1 - d2)
print(type(d1 - d2))

dt1 = dt.datetime(2020, 11, 4, 0, 0, 0)
dt2 = dt.datetime(2019, 11, 4, 14, 53, 0)

print(dt1 - dt2)
print(type(dt1 - dt2))

# creating timedelta objects manually
delta = dt.timedelta(weeks=2, days=2, hours=3)
# stored as days and seconds
print(delta)
print("Days:", delta.days,
      "Seconds:", delta.seconds,
      "Microseconds:", delta.microseconds)

# using timedelta
print(delta)

delta2 = delta * 2
print(delta2)

fin_date = dt.date(2019, 10, 4) + delta2
fin_datetime = dt.datetime(2019, 10, 4, 14, 53) + delta2
print(fin_date)
print(fin_datetime)
