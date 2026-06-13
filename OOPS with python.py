# OOPS

# object  = A "bundle" of related attributes (Variables) and methods (functions)
#           Ex. phone, cup , book
#           You need a "class" to create many objects

# class = (blueprint) used to design the structure and layout of an object

from caroops import Car

car1 = Car("TATA",2017,"Natural Silver",True)
car2 = Car("BMW",1997,"Black",False)


print(car1.model)
print(car1.year)
print(car1.color)
print(car1.for_sale)

print()

print(car2.model)
print(car2.year)
print(car2.color)
print(car2.for_sale)

