# string methods                                   play back time = (1:34:36)  from Bro code channel


# Example to find the string length

name = input("Enter your full name : ")

result = len(name)

print(result)




# Example 2:- to find the letter which occurs at first from the string

# It will count  until the letter occurs

# It will count only first occurrence ( First appearance)

# if the character is not found in the string it will return -1

name = input("Enter your name : ")

result = name.find("a")

print(result)



# Example :- 3 to find the last  occurrence from the string

name = input("Enter your name : ")

result = name.rfind("a")

print(result)



# Example :- 4

# if the character is not found in the string it will return -1

name = input("Enter your name : ")

result = name.find("q")

print(result)




# Example 5:- If you did  not mention the char to find

# It will count upto first space occurs

# which means the no.of characters from the string it will cound upto

# first space

name = input("Enter your name :")

result = name.find(" ")

print(result)






# Example 6:-

# We can capitalize the first letter in a string by using capitalize function

name = input("Enter your name : ")

name = name.capitalize()

print(name)

# Output ;- Enter your name :- nannabatuni aakash
# Answer -: Nannanbatuni aakash







# Example :- 7

# The upper method

# The upper method will take all of the characters in a string

# Then make them all uppercase

name = input("Enter your name : ")

name = name.upper()

print(name)

# Output :- Enter your name :- nannbattuni aakash

# Answer = NANNABATTUNI AAKASH








# Example :- 8

# The Lower method

# The Lower method will take all of the  characters in a string

# Then make them all Lowercases

name = input("Enter your name : ")

name = name.lower()

print(name)

# Output :- Enter your name :- NANNABATTUNI AAKASH

# Answer = nannabattuni aakash





# Example 9:- Digit method

# Now the Digit method will return true or False

# If a string contains only digits , the result is a Boolean

# True or False

name = input("Enter your name : ")

name = name.isdigit()

print(name)

# Output : Enter  your name :- 12345678

# Answer = True






# Example :- 10 Digit Method

# It will return False if any character is identified

# or a combination of characters and digits

name = input("Enter your name :")

name = name.isdigit()

print(name)

# Output :- Enter your name = Aakash77

#Answer = False







# Example 11 :- Alpha method


# this Alpha method will return a boolean True or False

# Depending if a string contains only alphabetical characters

name = input("Enter your name : ")

name = name.isalpha()

print(name)

# Output :- Enter your name :- Aashu

# Answer = True








# Example 12 :- Alpha method

# if the name contains any spaces it will return false

# which is not an alphabetical order

name = input("Enter your name : ")

result = name.isalpha()

print(result)

# Output :- Enter your name = Nannabattuni Aakash

#Answer = False (Because of containing spaces which is not alphabetical order)








# Example 13:- Alpha method

# It will also return False if your string(name)

# contains any digits

# or any combination of string and digits (numbers)

name = input("Enter your name : ")

result = name.isalpha()

print(result)

# Output = Enter your name = Aakash77

# Answer = False









# Example 13:- Count method

# we can use this method in string

# using example as Phone Number

# In this we can learn how the count method works

# in phone number we have some dashes (-)

# like for example 91+738-670-9941

# in above phone number we have 2 (-) dashes

# it will count them

phone_number = input("Enter your Phone Number #: ")

result = phone_number.count("-")

print(result)

# Output :- Enter your name = 738-670-9941

#Answer = 2









# Example 14:- Replace method

# Replace method is one of the most used method in the string

# We can replace any occurrence with one character with another

# we can use this method in names as well as in numbers also

# in below example we replace "N" in place "A"

name = input("Enter your name : ")

name = name.replace("n","a")

print(name)

# output :- nannabatttuni aakash

# Answer = aaaaabattuai aakash











# Example 15 :- Replace method

# Replace method is one of the most used method in the string

# We can replace any occurrence with one character with another

# we can use this method in names as well as in numbers also



phone_number = input("Enter your Phone number #:- ")

phone_number = phone_number.replace("-"," ") # in this new strign we have leave some space in another example we did not leave the space in between the empty string(new)

print(phone_number)

# Output = Enter your Phone Number =  738-673-341

# Answer = 738 670 9941











# Example :- 16

# If you did not enter any char or did not leave any spaces

#


name = input("Enter your name : ")

name = name.replace("-","")

print(result)

# Output = Enter your name = Nannabattuni-Aakash
#

# Answer = NannbattuniAakash
