# methods
# example class for showing method defining with self
# and invoking without
class Classy:
    def methodical(self):
        print("method")


obj = Classy()
obj.methodical()


# example class for showing method with parameters beyond self
class Classy2:
    def method(self, par):
        print("method:", par)


obj = Classy2()
obj.method(1)
obj.method(2)
obj.method(3)

# using self to invoke other object/class methods inside the class
class Classy3:
    def other(self):
        print("other")

    def method(self):
        print("method")
        self.other()


obj = Classy3()
obj.method()

# class __init__
class Classy4:
    def __init__(self, value):
        self.var = value


obj_1 = Classy4("object")

print(obj_1.var)


# class and property name mangling
class Classy5:
    def visible(self):
        print("visible")

    def __hidden(self):
        print("hidden")


obj = Classy5()
obj.visible()

try:
    obj.__hidden()
except:
    print("failed")

obj._Classy5__hidden()


# a class to show inbuilt attributes
class Classy6:
    varia = 1
    def __init__(self):
        self.var = 2

    def method(self):
        pass

    def __hidden(self):
        pass


obj = Classy6()

print(obj.__dict__)
print(Classy6.__dict__)

# __name__, type(),
class TestClass:
    pass

print(TestClass.__name__)
test_object = TestClass()
print(type(test_object).__name__)

# these return name of module
# in this instance will return __main__ (current file)
print(TestClass.__module__)
print(test_object.__module__)

# __bases__ and superclasses
class SuperOne:
    pass


class SuperTwo:
    pass


class Sub(SuperOne, SuperTwo):
    pass


def printBases(cls):
    print('( ', end='')

    for x in cls.__bases__:
        print(x.__name__, end=' ')
    print(')')


printBases(SuperOne)
printBases(SuperTwo)
printBases(Sub)

