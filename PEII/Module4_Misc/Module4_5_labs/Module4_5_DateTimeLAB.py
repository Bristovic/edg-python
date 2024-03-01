import datetime as dt
# import time


def datetime_format_func(year=0, month=0, day=0, hour=0, minute=0, second=0):
    func_dt = dt.datetime(year, month, day, hour, minute, second)
    print(func_dt.strftime("%Y/%m/%d %H:%M:%S"))
    print(func_dt.strftime("%y/%B/%d %H:%M:%S %p"))
    print(func_dt.strftime("%a, %Y %b %d"))
    print("Weekday:", func_dt.isoweekday())
    # func_time = time.localtime(func_dt.timestamp())
    # print("Day of the year:", func_time.tm_yday)
    # print("Week of the year:", func_dt.isocalendar().week)
    print("Day of the year:", func_dt.strftime("%j"))
    print("Week of the year:", func_dt.strftime("%U"))


datetime_format_func(2020, 11, 4, 14, 53)
