# keyword arguments = an argument by an identifier
#                     helps with readability
#                     order of arguments doesn't matter
#                     1.positional 2. default 3. KEYWORD 4. arbitrary


def hello(greeting, title, first_name, last_name):

    print(f"{greeting} {title}{first_name} {last_name}")

#hello("HEllo" , "Mr.","spongebob", "squarepants")

# order of the arguments doesn't matter
hello( "HEllo", first_name= "spongebob", title="Mr.",last_name="squarepants")  # prefix any arguments with the name is the parameter followed by equals.Title equals



#hello( first_name= "spongebob", title="Mr.",last_name="squarepants","HEllo",)  # the follows errors

# the above step has an error

# because Positional arguments follow keyword arguments

# so make sure any positional arhuments(like in example "HEllo" in program) are first before using any keyword arguments



# Exeample -1


for x in range(1,11):
    print(x,end=" ")

# use the separate keyword arguments then separate each of the strings with any of the given character or characters
print("\n1","2","3","4","5","6","7","8","9","10", sep="-")
print("\n1","2","3","4","5","6","7","8","9","10", sep="*")
print("------------------------------------------------------")

# Exercise -1

def get_phone(country,area,first_digit,last_digit):
    return f"{country}+{area}-{first_digit}-{last_digit}"

phone_num = get_phone(area=738,first_digit=670,last_digit=9941,country=91)
#phone_num = get_phone(91,738,670,9941)
print(phone_num)