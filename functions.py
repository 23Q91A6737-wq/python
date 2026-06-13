# Function

# function = a block of reusable code
#            place () after the function name to invoke it



def happy_birthday():
    print("Happy Birthday 🥳🥳 ")
    print(" you have grown")
    print("many more happy return of the day")
    print()
happy_birthday()    #-> it will print the answer . the benefit from this method is you can type the same answer multiple times
happy_birthday()     # -> we have executing the answer 3 times . so we are printing the same answer 3 times
happy_birthday()

print("-----------------------------------------------")

# Note

# With functions , you are able tos end data directly to a function using what are known as arguments.
# you can send values or variables directly to a function.
# place any data in the parenthesis
# any data you send a function are known as arguments
# but you need a matching set of parameters that are in order


def first_name(name):
    print(f" Hello {name}")
    print(f"Good Morning ☀️☀️")
    print()  #-> prints an empty line


first_name("Ash")  #-> you can print the answer many times as you want . But here just for practice just printing only 3 times. Because time is less
first_name("Ashu")
first_name("Fire and Ash")

print("-----------------------------------------------") #-> printing just for decoration for identifying the next answer just bordering the line


def aadhar_details(name , id):
    print(f" Hello {name} ,your Aadhar number is {id}")
    print(f"you are proceded , Because your {id} is valid")
    print(f"Thank you {name}")
    print() #-> just to print new line

aadhar_details("Ash 🌞🌤️🌥️" , 2003)
aadhar_details("Fire and Ash 🙈🙉🙊🐶" , 3012)
aadhar_details("Water 🐺🐱🦁🐯" , 4789)

print("----------------------------------------------------------") #-> just to print new decorative line for to identify next answer

#->  Note

# -> when you invoke a function, you can pass in some data.Those are known as arguments.
# -> But you need a matching set of parameters
#-> the also matters

#-> for example just for example we exchange the values of above answer


def aadhar_details(id , name):
    print(f" Hello {name} ,your Aadhar number is {id}")
    print(f"you are proceded , Because your {id} is valid")
    print(f"Thank you {name}")
    print() #-> just to print new line

aadhar_details("Ash 🌞🌤️🌥️" , 2003)
aadhar_details("Fire and Ash 🙈🙉🙊🐶" , 3012)
aadhar_details("Water 🐺🐱🦁🐯" , 4789)

print("--------------------------------------------------------------------")


# just for example
#-> to know the importance of order we executed the above answer
#-> the answer depends on the order of the parameter or in function part also


print("------------------------------------------------------------------------------")

def person_details(x,y):
    print(f"User name is : {x}")
    print(f"User age is : {y}")
    print(f"Welcome {x}")
    print() #-> just to print empty line

person_details("Ash ☀️🌞",21)
person_details("Fire and Ash 🔥🔥", 28)
person_details("water 🌊🌊🌊",37)

print("--------------------------------------------------------------------------------------------------------------------------")
print()
print()
#------------------------------------------------------------------------------------------------------------------------------------

# -> For Example
# Creating a function for example on creating to display an invoice(function_name) . it is our wish



# there will be three parameters .
# there are username , amount , due_date

def display_invoice(name , amount , due_date):
    print(f"Hello {name} , Your Electricity bill Is {amount}")
    print(f"please pay the {amount} before {due_date}")
    print(f"Thank you {name}")
    print()

display_invoice("Ash 😎😎⭐" , 2700 , "28/09/2025")  #-> dussehra holidays from 28/09/2025 to 05/10/2025  in collage
display_invoice("Fire and Ash 🔥🔥🌞🌞☀️" , 7000 , "28/09/2026")
display_invoice("Water 🌊🌊🌊", 8888 , "28/09/2027")

print("----------------------------------------------------------------------------")
