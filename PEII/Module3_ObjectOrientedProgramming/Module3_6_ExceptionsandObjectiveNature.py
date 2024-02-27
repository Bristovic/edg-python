# inclusion of else and finally after try-accept
def reciprocal_function(n):
    try:
        n = 1 / n
    except ZeroDivisionError:
        print("Division failed. Attempted to divide by zero.")
        n = None
    else:
        print("Everything went fine.")
    finally:
        print("Time to say goodbye. Goodbye!")
        return n


# test data
print(reciprocal_function(2))
print(reciprocal_function(0))

# exceptions as objects
try:
    val = int("Hello!")
except Exception as e:
    print(e)
    print(e.__str__())


# extending exception hierarchy
def print_exception_tree(this_class, nest=0):
    if nest > 1:
        print("   |" * (nest - 1), end="")
    if nest > 0:
        print("   +---", end="")

    print(this_class.__name__)

    for subclass in this_class.__subclasses__():
        print_exception_tree(subclass, nest + 1)


# prints entire exception tree
print_exception_tree(BaseException)


# closer look at exception anatomy
# this code prints args passed to the class constructor
def print_args(args):
    lng = len(args)
    if lng == 0:
        print("")
    elif lng == 1:
        print(args[0])
    else:
        print(str(args))


try:
    raise Exception
except Exception as e:
    print(e, e.__str__(), sep=' : ', end=' : ')
    print_args(e.args)

try:
    raise Exception("my exception")
except Exception as e:
    print(e, e.__str__(), sep=' : ', end=' : ')
    print_args(e.args)

try:
    raise Exception("my", "exception")
except Exception as e:
    print(e, e.__str__(), sep=' : ', end=' : ')
    print_args(e.args)


# Creating own exceptions
class MyZeroDivisionError(ZeroDivisionError):
    pass


def do_the_division(mine):
    if mine:
        raise MyZeroDivisionError("some worse news")
    else:
        raise ZeroDivisionError("some bad news")


for mode in [False, True]:
    try:
        do_the_division(mode)
    except ZeroDivisionError:
        print('Division by zero')

for mode in [False, True]:
    try:
        do_the_division(mode)
    except MyZeroDivisionError:
        print('My division by zero')
    except ZeroDivisionError:
        print('Original division by zero')


# defining a new base class for a new hierarchy of exception
# new base superclass for exceptions
class BeanError(Exception):
    # init takes specific bean and message (problem desc.)
    def __init__(self, bean="unknown", message=""):
        # init inits Exception with problem message
        Exception.__init__(self, message)
        # makes bean arg an attribute
        self.bean = bean


# new subclass of BeanError
class OldBeanError(BeanError):
    # init takes specific bean, age of bean, and problem desc.
    def __init__(self, bean="unknown", bn_age=">15", message=""):
        # inits BeanError (and Exception in turn)
        BeanError.__init__(self, bean, message)
        # makes age arg an attribute
        self.age = bn_age


# new function to test these errors
def make_bean_stew(bean, bn_age):
    if bean not in ["butter bean", "green bean", "runner bean"]:
        raise BeanError(bean, "No such type of bean")
    if bn_age > 15:
        raise OldBeanError(bean, bn_age, "Beans are too old")
    print("Stew is ready!")


# test data
for (bn, age) in [("butter bean", 4),
                  ("green bean", 29),
                  ("mouse bean", 10)]:
    try:
        make_bean_stew(bn, age)
    except OldBeanError as o_bn_error:
        print(o_bn_error, ":", o_bn_error.age, "days.")
    except BeanError as bn_error:
        print(bn_error, ":", bn_error.bean + ".")
