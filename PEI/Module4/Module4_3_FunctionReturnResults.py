# Getting results with return

# return without an expression terminates execution
def happy_new_year(wishes=True):
    print("Three...")
    print("Two...")
    print("One...")
    if not wishes:
        return

    print("Happy New Year!")


# invoking without args, return does not have an effect
happy_new_year()

# invoking with arg to specify wishes=False, returns before final print
happy_new_year(False)


# return with an expression makes it return a value as func result
def pointless_function():
    return 123


x = pointless_function()
print("The pointless function has return the result", x)

# evoking the func without assigning
pointless_function()  # the result will be ignored and lost

# on `None`
value = None
if value is None:
    print("Sorry, you don't carry any value")


# using none
# this function will return True if arg is even
def true_function(arg):
    if arg % 2 == 0:
        return True


y = true_function(2)  # returns True
z = true_function(3)  # returns None (as haven't defined else)


# function handling lists.
def list_sum(lst):
    s = 0

    for elem in lst:
        s += elem

    return s


print(list_sum([1, 2, 3, 4]))  # sums to 10
print(list_sum(5))  # will cause TypeError as int


# function returning list
def pointless_list(n):  # def func that takes int
    listed = []  # init empty list

    for item in range(0, n):  # for val in range 0 to n
        listed.insert(0, item)  # insert val in first index

    return listed  # returns a list with countdown from n to 0


print(pointless_list(3))


# Lab 1: Leap year function
def is_year_leap(yr_val):
    if yr_val < 1582:
        return False
    elif yr_val % 4 != 0:
        return False
    elif yr_val % 100 != 0:
        return True
    elif yr_val % 400 != 0:
        return False
    else:
        return True


# test data
test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr, "->", end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")


# Lab 2: Days in month
def days_in_month(year, month):
    # list of lengths of month
    month_length = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # check if inputs are valid, else return None
    if not isinstance(year, int) or not isinstance(month, int):
        return None
    # check if year == leap year. if True, change Feb to 29 days
    if is_year_leap(year):
        month_length[1] = 29
    # return number of days in input month by list index
    return month_length[month - 1]


# test data
test_years = [1900, 2000, 2016, 1987, 2004]
test_months = [2, 2, 1, 11, 2]
test_results = [28, 29, 31, 30, 29]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")

# Checking that incorrect inputs return None
print(days_in_month(1992, "b"))
print(days_in_month(1992, 2))


# Lab 3: Day of year
def day_of_year(year, month, day):
    # Check inputs are right type (int) or return None
    if (not isinstance(year, int)
            or not isinstance(month, int)
            or not isinstance(day, int)):
        return None
    # Check day value not larger than actual days in month or return None
    elif day > days_in_month(year, month):
        return None
    else:
        # make day of year equal day in final month
        year_day = day
        # sum days of previous months and add to day of year
        for months in range(month-1):
            # need months+1 or first month return [-1]
            year_day += days_in_month(year, months+1)
        return year_day


# Test to return None if wrong type inputs
print(day_of_year("bob", 1, 2))

# Test to return None if day number > actual days in month
print(day_of_year(2012, 2, 31))

# Test data
print(day_of_year(2000, 12, 31))
print(day_of_year(2024, 2, 5))
print(day_of_year(1999, 3, 1))
print(day_of_year(1692, 10, 12))


# Lab 4: Primes
# function to check if number is prime
def is_prime(val):
    # for each divisor in range from 2 to num-1 (to avoid 1 and # itself)
    for div in range(2, val-1):
        # if number is divisible (remainder zero) return False
        if val % div == 0:
            return False
    # Otherwise, return True
    return True


# test data, should return 2 3 5 7 11 13 17 19
for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()


# Lab 5: Converting fuel Consumption
def l_pr_100km_to_mpg(l_pr_100km):
    mile = 1.609344
    gallon = 3.785411784
    km_pr_l = 100 / l_pr_100km
    mpg = (km_pr_l * gallon) / mile
    return mpg


def mpg_to_l_pr_km(mpg):
    mile = 1.609344
    gallon = 3.785411784
    gpm = 1 / mpg
    lpm = gpm * gallon
    lpkm = lpm / mile
    lpckm = lpkm * 100
    return lpckm


# test data
print(l_pr_100km_to_mpg(3.9))
print(l_pr_100km_to_mpg(7.5))
print(l_pr_100km_to_mpg(10.))
print(mpg_to_l_pr_km(60.3))
print(mpg_to_l_pr_km(31.4))
print(mpg_to_l_pr_km(23.5))


# simplified
def simple_l_pr_100km_to_mpg(l_pr_100km):
    mile = 1.609344
    gallon = 3.785411784
    return (100 * gallon) / (l_pr_100km * mile)


def simple_mpg_to_l_pr_km(mpg):
    mile = 1.609344
    gallon = 3.785411784
    return (gallon * 100) / (mpg * mile)


print(simple_l_pr_100km_to_mpg(3.9))
print(simple_l_pr_100km_to_mpg(7.5))
print(simple_l_pr_100km_to_mpg(10.))
print(simple_mpg_to_l_pr_km(60.3))
print(simple_mpg_to_l_pr_km(31.4))
print(simple_mpg_to_l_pr_km(23.5))
