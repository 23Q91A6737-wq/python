

#print(__name__)


from script1 import *

def favorite_drink(drink):
    print(f"Your favorite drink is {drink}")

def main():
    print("This is script2")
    favorite_food("sushi")
    favorite_drink("coffee")
    print("goodbye")

if __name__ == "__main__":
    main()




# note:

# if __name__ == __main__ : (this script can be imported OR run standalone)
# Functions and classes in this module can be reused without the main block of code executing
# Good practice (code is moduler;
#                helps readability,
#                leaves no global variables,
#                avoid unintended execution)


# Ex.library = import library for functionality
#                When running library directly, display a help page