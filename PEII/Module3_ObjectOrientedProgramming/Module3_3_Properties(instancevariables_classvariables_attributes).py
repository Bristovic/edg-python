# example to look at instance var functionality
class InstVarClass:
    def __init__(self, val=1):
        self.first = val

    def set_second(self, val):
        self.second = val


# examples
ex_obj_1 = InstVarClass()
ex_obj_2 = InstVarClass(2)

# use method to set second
ex_obj_2.set_second(3)

ex_obj_3 = InstVarClass(4)
ex_obj_3.third = 3

# prints inbuilt dictionary of names and values
print(ex_obj_1.__dict__)
print(ex_obj_2.__dict__)
print(ex_obj_3.__dict__)

#modified version with limited private variables
class InstVarClass2:
    def __init__(self, val=1):
        self.__first = val

    def set_second(self, val=2):
        self.__second = val


# examples
ex_obj_1 = InstVarClass2()
ex_obj_2 = InstVarClass2(2)

# use method to set second
ex_obj_2.set_second(3)

ex_obj_3 = InstVarClass2(4)
ex_obj_3.__third = 3

print(ex_obj_1.__dict__)
print(ex_obj_2.__dict__)
print(ex_obj_3.__dict__)


# class variables
class ClassVarEx:
    # instantiates a class variable shared between all instances
    counter = 0
    # initiates by creating property "first" with default val of 10
    # or whatever put in as first parameter
    def __init__(self, val = 10):
        self.__first = val
        # increments the class variable by one with class instance
        # instantiation
        ClassVarEx.counter += 1

# create three instances of the class
ex_4 = ClassVarEx()
ex_5 = ClassVarEx(20)
ex_6 = ClassVarEx(12)

# print dict of values and value of counter. counter same on all
print(ex_4.__dict__, ex_4.counter)
print(ex_5.__dict__, ex_5.counter)
print(ex_6.__dict__, ex_6.counter)

# difference between class and instance __dict__
class ExampleClass:
    varia = 1
    def __init__(self, val):
        ExampleClass.varia = val


print(ExampleClass.__dict__)
example_object = ExampleClass(2)

print(ExampleClass.__dict__)
print(example_object.__dict__)


# checking an attribute's existence
class ExampleClass:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1


example_object = ExampleClass(1)
#
# print(example_object.a)
# print(example_object.b)  # will raise error as trying to access
# nonexistent attribute

# using hasattr to check if a class has specified attribute
if hasattr(example_object, "b"):
    print(example_object.b)


# hasattr() on classes and instances
class ExampleClass:
    a = 1
    def __init__(self):
        self.b = 2


example_object = ExampleClass()

print(hasattr(example_object, 'b'))
print(hasattr(example_object, 'a'))
print(hasattr(ExampleClass, 'b'))
print(hasattr(ExampleClass, 'a'))


