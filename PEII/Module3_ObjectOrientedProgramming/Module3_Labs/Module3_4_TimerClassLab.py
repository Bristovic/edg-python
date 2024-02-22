# Timer Class Lab
class Timer:
    def __init__(self, hrs=0, mins=0, secs=0):
        self.__time = [hrs, mins, secs]

    def __str_time(self):
        self.__time_list = []
        for digit in self.__time:
            digit = str(digit)
            if len(digit) == 1:
                digit = "0" + digit
            self.__time_list.append(digit)
        return ":".join(self.__time_list)

    def __str__(self):
        return self.__str_time()

    def next_sec(self):
        self.__time[2] += 1
        if self.__time[2] == 60:
            self.__time[2] = 0
            self.__time[1] += 1
        if self.__time[1] == 60:
            self.__time[1] = 0
            self.__time[0] += 1
        if self.__time[0] == 24:
            self.__time[0] = 0

    def prev_sec(self):
        self.__time[2] -= 1
        if self.__time[2] == -1:
            self.__time[2] = 59
            self.__time[1] -= 1
        if self.__time[1] == -1:
            self.__time[1] = 59
            self.__time[0] -= 1
        if self.__time[0] == -1:
            self.__time[0] = 23


timer = Timer(23, 59, 59)
print(timer)
timer.next_sec()
print(timer)
timer.prev_sec()
print(timer)

timer = Timer(0, 59, 59)
print(timer)
timer.next_sec()
print(timer)
timer.prev_sec()
print(timer)
