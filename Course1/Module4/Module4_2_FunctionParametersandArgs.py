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
def message(what, number):
    print("Enter", what, "number", number)


message("telephone", 11)
