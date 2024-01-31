from sys import path

path.append("ex_package\\packages\\")

import extra.iota
print(extra.iota.FunI())

from extra.iota import FunI
print(FunI())