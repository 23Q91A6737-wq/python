# dictionary = a collection of {key:value} pairs
#              ordered and changeable . No duplicates

capitals = {"USA" : "Washington D.C",
            "India" : "New Delhi",
            "Japan" : "Tokyo",
            "Germany" :  "Berlin"}

print(dir(capitals)) # -> all attributes and method of a dictionary

help(help(capitals)) # -> descriptive of all attributes and methods of a dictionary

print() #-> this will print new line

print(capitals.get("Japan"))
print(capitals.get("India"))
print(capitals.get("Canada")) # -> this will print None . Because the capital is not there in our tuple

# we can use in if statement also

if capitals.get("Mongolia"):
    print("The Mongolia Country Exits")
else:
    print("The Mongolia Country does not exits in our capital ")



print("\n") #-> this will print new line

print(capitals) #-> Normally printed the actual capitals .   Because in below we are updating the capitals . to check just we are printing the actual capitals .it is optional or not neccesary to print
print()
capitals.update({"Germany" : "BMW "})  #-> THIS UPDATE THE CAPITALS .By updating the country's capital
capitals.update({"ISREAL" : "Jerusalem"})  # -> This will uptage the capital . By adding another country name and itd capital
print(capitals)

capitals.pop("Germany")  # -> the pop method will remove the entire key and value
print(capitals)

capitals.popitem() #-> this will remove the latest key : value that is entered
print(capitals)

#capitals.clear() # -> this will clear all the key and values in the Tuple
#print(capitals)

print("\n\n")


# To print all the Keys in the list

keys = capitals.keys()
print(keys)

# -> To get all values .in the list

values = capitals.values()
print(values)

print("\n")

# -> You can go with the for loop method

for key in capitals.keys():
    print(key)

print() #-> to leave one line

for value in capitals.values():
    print(value)

# -> items method

# -> items returns a dictionary object which resembles a 2D list of tuples
items = capitals.items()
print(items)

print() #-> just to print new line
# using for loop to print
# to print every key ,  value in capitals.items() method


for key,value in capitals.items():
    print(key,value)


    #-> or you can print by design
    # (f"{key} : {value}")