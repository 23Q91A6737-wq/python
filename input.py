#input = A function that prompts the user to enter the data
#          Returns the entered data as a string

name = input("what is your name ? :")
age = input("How old are you ? :")

print(f"Hello {name}")
print("HAPPY BIRTHDAY !")
print(f"you are {age} old ")

# what is your name ? : Aakash
# How old are you ? : 21
# Hello  Aakash
# HAPPY BIRTHDAY !
# you are 21 old



#  2) it is usaually concentrate on strings so we can convert into

#              integers and float

name = input("what is your name ? :")
age = input("How old are you ? :")
height = input("you are grown upto {height} feet : ")


age = int(age)

age =  age+1       #---> THIS step will increase your age from last year to present year (for example)
height = float(height)


print(f"Hello {name}")
print("HAPPY BIRTHDAY !")
print(f"you are {age} old ")
print(f"you are grown upto {height} feet ")


