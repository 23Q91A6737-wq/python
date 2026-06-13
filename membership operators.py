# Membership operators

# Membership operators = used to test whether a value or variable is found in a sequence
#                        (string, list, tuple, set, or dictionary)
#                         1. in
#                         2. not in


#  string

# Example -> method-1

secret_word = "Aeroplane"

letter = input("Enter a letter in the secret word: ")

if letter in secret_word:
    print(f"there is a  {letter}")
else:
    print(f"the {letter} was not found")

print("------------------------------------------------------")


# method-2

word = "Aeroplane"

letter = input("Guess a letter in the secret word: ")

if letter not in word:
    print(f"The {letter} was not found")
else:
    print(f"There is a {letter}")

print("-----------------------------------------------------------")


# set  (similarly like  list, tuples )

students = {"Spongebob", "patrik","Square pants"}

student = input("Enter the name of the student: ")

if student in students:
    print(f"{student} was present in class")
else:
    print(f"{student} was absent in class")

print("-------------------------------------------------------------------")


# dictionary

# Example -> names and grades (A, B, C, D)

grades = {"Ben10":"A",
            "Tom and Jerry": "B",
            "Bey Blade":"C",
            "Power Rangers":"D"}

student = input("Enter the name of the students for grades: ")

if student in grades:
    print(f"{student}'s grade is {grades[student]}")
else:
    print(f"{student} was not found")

print("-----------------------------------")


# Example -> grades and names (A, B, C, D)

grades = {"Ben10":"A",
            "Tom and Jerry": "B",
            "Bey Blade":"C",
            "Power Rangers":"D"}

grade = input("Enter the grade to find students: ")

found = False
for name in grades:
    if grades[name] == grade:
        print(f"{name} got grade {grade}")
        found = True

if not found:
    print(f"No students found with grade {grade}")



# ANOTHER example on string

email = "aakash772005@gmail.com"

# check if at is an email and check if a period is an email

if "@" in email and "." in email:
    print("valid email")
else:
    print("invalid email !!!")

print("-------------------------------------------")

email = "aakash772005@gamilcom"

if "@" in email and "." in email:
    print("Valid email")
else:
    print("Invlaid Email !!!")