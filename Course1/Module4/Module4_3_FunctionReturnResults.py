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
def true_function(x):
    if x % 2 == 0:
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
    pointless_list = []  # init empty list

    for i in range(0, n):  # for val in range 0 to n
        pointless_list.insert(0, i)  # insert val in first index

    return pointless_list  # returns a list with countdown from n to 0

print(pointless_list(3))


# Lab 1: Leap year function
def is_year_leap(yr):
    if yr < 1582:
        return False
    elif yr % 4 != 0:
        return False
    elif yr % 100 != 0:
        return True
    elif yr % 400 != 0:
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
