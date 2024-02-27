# the anatomy of an iterator
# example fibonacci iterator
class Fib:
    def __init__(self, nn):
        print("__init__")
        self.__n = nn
        self.__i = 0
        self.__p1 = self.__p2 = 1

    def __iter__(self):
        print("__iter__")
        return self

    def __next__(self):
        print("__next__")
        self.__i += 1
        if self.__i > self.__n:
            raise StopIteration
        if self.__i in [1, 2]:
            return 1
        ret = self.__p1 + self.__p2
        self.__p1, self.__p2 = self.__p2, ret
        return ret


for i in Fib(10):
    print(i)


# iterator as part of a complex object
class Fib:
    def __init__(self, nn):
        self.__n = nn
        self.__i = 0
        self.__p1 = self.__p2 = 1

    def __iter__(self):
        print("Fib iter")
        return self

    def __next__(self):
        self.__i += 1
        if self.__i > self.__n:
            raise StopIteration
        if self.__i in [1, 2]:
            return 1
        ret = self.__p1 + self.__p2
        self.__p1, self.__p2 = self.__p2, ret
        return ret


class Class:
    def __init__(self, n):
        self.__iter = Fib(n)

    def __iter__(self):
        print("Class iter")
        return self.__iter


object = Class(8)

for i in object:
    print(i)


# building own generator with the yield keyword
def fun(n):
    for i in range(n):
        # yield works like return but keeps state and doesn't stop exec
        # must be invoked implicitly (as below)
        yield i


for v in fun(5):
    print(v)


# own generator example
# generator to give the first n powers of 2
def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2


# test data
for v in powers_of_2(8):
    print(v)


# list comprehension generators
list_comp = [x for x in powers_of_2(5)]
print(list_comp)

# list() function to transform a series of generator invocs to a list
list_func = list(powers_of_2(3))
print(list_func)

# the in operator
for i in range(20):
    if i in powers_of_2(4):
        print(i)


# simpler fibonacci generator
def fibonacci(n):
    # sets two first numbers to be summed (both always 1)
    p = pp = 1
    # makes the first two values return (0th and 1st) to 1
    for i in range(n):
        if i in [0, 1]:
            yield 1
        else:
            # gives n: the sum of the two previous values
            n = p + pp
            # reassigns the two previous values to current and previous
            pp, p = p, n
            # yields the sum at start of else block
            yield n


# test data
fibs = list(fibonacci(10))
print(fibs)


# list comprehensions reminder
list_1 = []

for ex in range(6):
    list_1.append(10 ** ex)

list_2 = [10 ** ex for ex in range(6)]

print(list_1)
print(list_2)


# the conditional expression
the_list = []

for x in range(10):
    the_list.append(1 if x % 2 == 0 else 0)

print(the_list)


# list comprehensions vs generators
the_list = [1 if x % 2 == 0 else 0 for x in range(10)]
the_generator = (1 if x % 2 == 0 else 0 for x in range(10))

for v in the_list:
    print(v, end=" ")
print()

for v in the_generator:
    print(v, end=" ")
print()


# example of the lamda function used for anonymous functions
two = lambda: 2
sqr = lambda x: x * x
pwr = lambda x, y: x ** y

for a in range(-2, 3):
    print(sqr(a), end=" ")
    print(pwr(a, two()))


# using lamdas to streamline code
# long version
def print_function(args, fun):
    for x in args:
        print('f(', x, ')=', fun(x), sep='')


def poly(x):
    return 2 * x**2 - 4 * x + 2


print_function([x for x in range(-2, 3)], poly)


# lamdaed version
def print_function(args, fun):
    for x in args:
        print('f(', x, ')=', fun(x), sep='')


print_function([x for x in range(-2, 3)], lambda x: 2 * x**2 - 4 * x + 2)


# the map() function
list_1 = [x for x in range(5)]
list_2 = list(map(lambda x: 2 ** x, list_1))
print(list_2)

for x in map(lambda x: x * x, list_2):
    print(x, end=' ')
print()


# filter function and lamdas
from random import seed, randint

seed()
data = [randint(-10,10) for x in range(5)]
filtered = list(filter(lambda x: x > 0 and x % 2 == 0, data))

print(data)
print(filtered)


# using closures to access variables
def outer(par):
    loc = par

    def inner():
        return loc
    return inner


var = 1
fun = outer(var)
print(fun())


# invoking closures in the same way they are declared
def make_closure(par):
    loc = par

    def power(p):
        return p ** loc
    return power


fsqr = make_closure(2)
fcub = make_closure(3)

for i in range(5):
    print(i, fsqr(i), fcub(i))
