
# Exercise

# validate user input exercise

#  1. username is no more than 12 characters

#  2. username must not contain spaces

#  3. username must not contain digits

username = input("Enter you username : ")

if len(username) > 12:

    print("The username cannot be more than 12 characters")

elif not username.find(" ") == -1:

    print("The username cannot contain spaces ")

elif not  username.isalpha() :

    print("The username cannot contain numbers")
else:

    print(f"Welcome {username}")
