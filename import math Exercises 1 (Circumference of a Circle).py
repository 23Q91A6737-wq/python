
# Exercise 1 :- The circumference of a circle (c = 2.pi.r)
# pi=>22/7 => 3.41...

import math

radius = float(input("The Radius of the Circle : "))

circumference = 2 * math.pi * radius

print(f"The circumference of the circus is : {circumference}")

# if you want you can add various round , ceil function
# to convert the answer according to your wish

# Here in this example we have converting
# the float point into round figure
# by the above round method
# if the answer is 3.24234356789
#we will get 3.24 (here two float point will show or as you insert)

import math

radius = float(input("Enter the Radius of the circle : "))

circumference = 2 * math.pi * radius

print(f"The Circumference of the Circle : {round(circumference,2)}")


