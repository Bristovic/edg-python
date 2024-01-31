# to find the path variable (list of all dir searched for modules)
import sys

for p in sys.path:
    print(p)

# to add to path
from sys import path

path.append("ex_package/packages/extra")