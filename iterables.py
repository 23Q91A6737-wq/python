# iterables = An object/collection that can return its elements one at a time,
#             allowing it to be iterated over in a loop

#EXAMPLES ->

# Lists -> []
numbers = [1,2,3,4,5]  #-> lists are iterables ()

for element in numbers:
    print(element)
print("-------------")

for blablabla in reversed(numbers):
    print(blablabla)

print("------------")

# Tuples -> ()

    # Tuples are also iterable

numbers = (7,8,9,4,5,6)

for element in numbers:
    print(element)

print("-----------------------")


# SETS -> {}


# now lets cover sets

fruits = {"apple" , "banana" , "orange" , "pineapple"}

for fruit in fruits:
    print(fruit)

print("-------------------------------")

# Character

name = "Aakash"

for character in name:
    print(character)

print("---------------------------------")

login = "Aakash"

for letter in login:
    print(letter,end=" ")

print("--------------------------------------")

#Dictionaries

my_dictionary = {"Ash":789, "Fire":456 , "Water":123}

for key in my_dictionary:
    print(key)
    print()
for value in my_dictionary.values():
    print(value)

# to print the key and values together

for key , value in my_dictionary.items():
    print(key,value)
print("---------------")
# ypu can add some design also to identify the key and values

for key , value in my_dictionary.items():
    print(f"{key:10}:{value}")