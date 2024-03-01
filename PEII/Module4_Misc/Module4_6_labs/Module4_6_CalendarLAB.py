import calendar


class MyCalendar(calendar.Calendar):
    def __init__(self):
        super().__init__()

    def days_of_week_in_year(self, year=0, weekday=0):
        day_count = 0
        count = 0
        for month in range(1, 13):
            month_days = list(self.itermonthdays2(year, month))
            for day in month_days:
                if day[0] == 0:
                    count += 1
                    continue
                elif day[1] == weekday:
                    day_count += 1
                else:
                    continue
        return day_count


calendario = MyCalendar()
print(calendario.days_of_week_in_year(2000, 6))
