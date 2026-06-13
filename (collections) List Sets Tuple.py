# collections = single "variable" used to store multiple values
# List = [] ordered and changeable.Duplicate OK
# Set = {} unordered and immutable, but Add/Remove OK. NO duplicate
# Tuple = () ordered and unchangable.Duplicate OK. FASTER


# dir = to list the different methods that are available to a collection
# you can use the dir function

#Note -> A Tuple is faster than the list .
# A Tuple is ordered and unchangeable

fruits = [ "orange", "orange" , "banana" , "coconut"]

print(fruits)
#--------------------------------------------------------------------------------
# Example ->1


fruits = [ "orange", "orange" , "banana" , "coconut"]
print(fruits)  # -> prints total value including []

print(fruits[0]) #-> to access a specific number

print(fruits[::2])  #-> to access every second element

print(fruits[-1])   # -> to print from last to first

print(fruits[::-1])  # -> to print from last to first (accessing all numbers)

#-----------------------------------------------------------------------------------------------
# Example -> 2

fruits = [ "orange", "orange" , "banana" , "coconut"]

for x in fruits:

    print(f"{x}\n")  # -> print(x)

# or method 2


fruits = [ "orange", "orange" , "banana" , "coconut"]

for fruit in fruits:
    print(fruit)
#--------------------------------------------------------------------------------------------------
# to list the different methods that are available to a collection
 # you can use the dir function

fruits = ["orange", "orange", "banana", "coconut"]

for fruit in fruits:

   print(dir(fruits))
#----------------------------------------------------------------------------------------
# to know the descrotion of the dir

# use help method

fruits = ["apple", "orange", "banana", "coconut"]

print(len(fruits)) # -> to find the length

# using the in operator , we can find if a value within a collection

# for example -> is our value apple in fruits?

print("apple" in fruits) # -> like boolean function
print("pineapple" in fruits)



# Note
# with lists they are ordered and changeable.
# dupicates are okay.
# we can change one of these values after we create our list

#---------------------------------------------------------------------------------
cars = ["apple", "orange", "banana", "coconut"]

cars[0] = "BMW"

for car in cars:

    print(f"{car}\n")

#-----------------------------------------------------------------------

# lets cover some methods that found withnin a list

# we can append an element

aeroplane = [ "TATA" , "VISTARA" , "INDIGO" , "KINGFISHER"]

aeroplane.append("TATA") #-> it will again appear in last

print(aeroplane)

aeroplane.remove("VISTARA") # -> it will remove the item

print(aeroplane)

aeroplane.insert( 0 , "FEDEX")  # -> to insert the item we will use this function
# it is inserted in first position
print(aeroplane)

aeroplane.insert( 2 , "QUANTUS") # TO INSERT the new element in 3rd position

print(aeroplane)

aeroplane.sort()#-> to print in alphabetical order

print(aeroplane)

#aeroplane.reverse() # -> to reverse a list we use this function.

print(aeroplane)

#aeroplane.clear() # -> for clearing the list we use this element

print(aeroplane)

print(aeroplane.index("FEDEX")) # -> to know the index of the ite

print(aeroplane.count("TATA")) # -> HOW MANY TIMES IS IT REPEATED

for car in cars:
    print(car)