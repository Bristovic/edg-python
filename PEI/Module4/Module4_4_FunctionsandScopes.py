# Scope

# This will fail as x in func is out of scope.
def scope_test():
    x = 123


scope_test()
print(x)


# a variable defined outside func is accessible within.
def my_function():
    print("Do I know that variable?", var)


var = 1
my_function()
print(var)


# unless redefined within scope of function
def my_function():
    var = 2
    print("Do I know that variable?", var)


var = 1
my_function()
print(var)


# the global keyword circumvents this
def my_function():
    global var
    var = 2
    print("Do I know that variable?", var)


var = 1
my_function()
print(var)


# functions take value of scalar arg, not arg itself
def my_function(val):
    val += 1
    print("Val = ", val)


# test. value is not changed outside function. with scalar
value = 2
my_function(value)
print(value)


# the case with lists if you totally reassign
def list_function(list_data):
    print(list_data)
    print(list_data_2)
    list_data = [0, 1]
    print(list_data)
    print(list_data_2)


list_data_2 = [3, 4]
list_function(list_data_2)
print(list_data_2)


# but not if modify
def list_function_2(list_data):
    print(list_data)
    print(list_data_2)
    list_data[0] = 99
    print(list_data)
    print(list_data_2)


list_data_2 = [3, 4]
list_function_2(list_data_2)
print(list_data_2)
