
# While loop                                                        (1:51:27)

# while loop = exercise some code WHILE some condition remains true



# Example :1

# in the below code we used if statement

# in the output you will find difference between if condition and while loop condition

# in the if condition the code is executed only one time

# in the if condition we will not see the repeating process

name = input("Enter your name: ")

if name == "":

    print("You did not enter your name!")

else:

    print(f"Hello {name}")


# Output :-1

#Enter your name: ""
#You did not enter your name!

# Output :-2

#Enter your name: aashu
#Hello aashu









# Example:-2

# using while loop

# in the below example we will solve the problem using while loop

# it will executes the process until the condition is true

# if the condition is not true it will repeat the process

while name == "":

    print("You did not enetred your name!")

    name = input("Enter your name: ")

print(f"Hello {name}")

# output 1:- if you did not entered your name it will repeat the process unless if condition

# unless the if condition which executes only one time

#You did not entered your name!
#Enter your name:
#You did not entered your name!
#Enter your name:
#You did not entered your name!
#Enter your name:
#You did not entered your name!
#Enter your name:



# Output :- 2

# if you entered your name

#Enter your name: Aakash
#Hello Aakash

# Example :3

# in the below given example we will see the

# infinity loop

#name = input("Enter your name")
#while name== "":

 #   print("Please Enter your name!")

#print(f"Hello {name}")


# Example :_3

age = int(input("Enter your age: "))

while age < 0:

    print("age can't be negative")

    age = int(input("Enter your age"))

print(f"you are {age} old")


# Example :-4

# in the below example

# the program is about the if you entered food name

# it will ask repeatedly and once you entered "q" it will exit

food = input("Enter your favorate food you like (q to quit) : ")

while not food == "q":

    print(f"you like {food} ? it is good")

    food = input("enter your another favorate food (q to quit)")

print("bye")

# Example :- 5

number = int(input("Enter a number # between 1-10"))

while number <1 or number > 10:

    print("your number is not valid")

    number = int(input("the number is valid # fbecause it is  in between 1-10"))

print(number)