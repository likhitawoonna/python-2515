# Using Modules
# get all modules
# print(help('modules'))

# 1st Approach -> Import entire module
import math
print(math.sqrt(25))

# 2nd Approach -> Import specific functionalities from module
from math import sqrt
print(sqrt(25))

# 3rd Approach -> Using Alias names
import math as m
print(m.sqrt(25))

# User Defined Modules