# Useful modules

# using the dir() function to see entity names
import math  # necessary for use of dir
print(dir(math))

for name in dir(math):
    print(name, end="\t")

# some basic examples from math module
from math import pi, radians, degrees, sin, cos, tan, asin

ad = 90
ar = radians(ad)
ad = degrees(ar)

print(ad == 90.)
print(ar == pi / 2.)
print(sin(ar) / cos(ar) == tan(ar))
print(asin(sin(ar)) == ar)

# exponentiation
from math import e, exp, log

print(pow(e, 1) == exp(log(e)))
print(pow(2, 2) == exp(2 * log(2)))
print(log(e, e) == exp(0))

# general purpose
from math import ceil, floor, trunc

x = 1.4
y = 2.6

print(floor(x), floor(y))
print(floor(-x), floor(-y))
print(ceil(x), ceil(y))
print(ceil(-x), ceil(-y))
print(trunc(x), trunc(y))
print(trunc(-x), trunc(-y))

# random module
from random import random

for i in range(5):
    print(random())

# modifying seed so that "random" sequence will always show same order
from random import seed

seed(0)

for i in range(5):
    print(random())

# randrange and randint
from random import randrange, randint

print(randrange(1), end=' ')
print(randrange(0, 1), end=' ')
print(randrange(0, 1, 1), end=' ')
print(randint(0, 1))

# choice and sample
from random import choice, sample

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(choice(my_list))
print(sample(my_list, 5))
print(sample(my_list, 10))

# platform and platform()
from platform import platform

print(platform())  # returns system (hardware, OS, interpreter, etc)
print(platform(1))
print(platform(0, 1))

# machine()
from platform import machine

print(machine())  # returns processor

# processor()
from platform import processor

print(processor())  # returns full processor name

# system()
from platform import system

print(system())  # returns generic OS name

# version()
from platform import version

print(version())  # returns version number

# python_implementation() and python_version_tuple()
from platform import python_implementation, python_version_tuple

print(python_implementation(), python_version_tuple())
