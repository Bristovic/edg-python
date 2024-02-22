# exception for incorrect day name
class WeekDayError(Exception):
    pass


# class to check day of week for given offset
class WeekDayChecker:
    __valid_day_names = ("Monday",
                         "Tuesday",
                         "Wednesday",
                         "Thursday",
                         "Friday",
                         "Saturday",
                         "Sunday")

    def __init__(self, day):
        if day not in WeekDayChecker.__valid_day_names:
            raise WeekDayError
        else:
            self.__day = day

    def __str__(self):
        return self.__day

    def add_days(self, n):
        self.__day = WeekDayChecker.__valid_day_names[
            ((WeekDayChecker.__valid_day_names.index(self.__day))
             + n) % 7
        ]

    def sub_days(self, n):
        self.__day = WeekDayChecker.__valid_day_names[
            ((WeekDayChecker.__valid_day_names.index(self.__day))
             - n) % 7
        ]


weekday = WeekDayChecker('Monday')
print(weekday)
weekday.add_days(15)
print(weekday)
weekday.sub_days(23)
print(weekday)
