# module = a file containing code you want to include in your program
#          use 'import' to include a module (built-in your own)
#          useful to break up a large up program reusable separate files

print(help("modules"))

print("----------------------------------------------------------------")
# for example with the math module
print(help("math"))

import math

print(math.pi)

print("----------------------------------------------------------------")

# method 2
# using an alias would reduce some of typing you have to  use.
# if you have very long moduler name
#2nd method to import

import math as m

print(m.pi)

print("----------------------------------------------------------------")

# method->3

# import to use from the name of the module

# import something specific , PI for instance, you would no longer needed the module name
# from math import pi , pi would be included within our name space

# however I tend not use from import as much
#just because it's possible there could be name conflicts

from math import e

print(e)

print("----------------------------------------------------------------")

# Example on name conflicts

# problem of using the method->3
# because of name conflicts

from math import e

print(e)

a, b, c, d = 1, 2, 3, 4

print(e**a)
print(e**b)
print(e**c)
print(e**d)

print("----------------------------------------------------------------------")

# example on name conflicts from using method->3

from math import e

print(e)

a, b, c, d, e = 1, 2, 3, 4, 5

print(e ** a)
print(e ** b)
print(e ** c)
print(e ** d)
print(e ** e)

# the above problem is wrong output