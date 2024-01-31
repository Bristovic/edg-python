# importing modules

# import a whole module - import keyword and math module name
import math

# import multiple modules, comma or list sequentially
import math, sys

# using an entity from a whole-imported module
x = math.pi
print(x)
print(math.sin(math.pi/2))

# can have own entities with same name with no conflict
pi = 3.14


def sin(y):
    if 2 * y == pi:
        return 0.99999999999999
    else:
        return None


print(sin(pi/2))

# importing specific entities to namespace
from math import sin, pi  # usually at top of page, would be overwritten

# now uses the imported entities (overwriting those defined)
print(sin(pi/2))

# aliasing, imports module under other alias
import tkinter as tk

# extended example
import math as m
print(m.sin(m.pi/2))

# entity aliasing
from math import pi as PI, sin as sine

print(sine(PI/2))

