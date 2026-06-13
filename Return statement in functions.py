# Return Statements                                playtime -> (04:00:00) Bro code

# return = statement used to end a function
#           and send a result back to the caller


# the below code is just the basic to know the return statement

def add(x,y):
    z = x+y
    print(z)

def substraction(x,y):
    z = x-y
    print(z)

def multiplication(x,y):
    z = x*y
    print(z)


def division(x, y):
    z = x/y
    print(z)

add(25,27)
substraction(87,65)
multiplication(81,87)
division(86,24)

print("-------------------------------------------------------------------------------")
print() #-> just to print new line

#------------------------------------------------------------------------------------------

# For Example,
# Creating a first name and last name


def create_name(first_name , last_name):
    first_name=first_name.capitalize()
    last_name=last_name.capitalize()
    return first_name + " " + last_name

full_name = create_name("Spongebob","squarepants")
second_full_name = create_name("spongebob","squarepants in cartoon network show")
print(full_name)
print(second_full_name)

