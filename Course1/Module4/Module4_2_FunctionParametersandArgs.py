# simple one-parameter function (takes an arg: name)
def hello(name):  # defining func and arg
    print("Hello,", name)  # body of function


name = input("Enter your name: ")  # defining name
hello(name)  # invoking with name


# legal to have parameter and variable of same name
def message(number):
    print("Number:", number)


number = 1234  # invokes shadowing
message(1)
print(number)


# multiple parameter function
# positional parameter passing
def message(what, number):
    print("Enter", what, "number", number)


message("telephone", 11)  # positional arguments

# keyword argument passing
message(number=12, what="page")


# mixing positional and keyword. all positional come first.
def new_message(what, number, times):
    print("Enter", what, "number", number, times, "times.")


new_message("entry", times=3, number=22)


# default args for parameters
def introductions(first_name="John", second_name="Smith"):
    print("Hello, my name is", first_name, second_name)


# these are valid
introductions("Alfred")  # uses this and default for 2nd name
introductions()  # uses default for both
introductions(second_name="Willis")  # uses default for 1st
introductions(second_name="Jones", first_name="Tom")  # replaces defaults
