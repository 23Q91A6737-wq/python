# Match-case statement (Switch) = An alternative to using many 'elif' statement
#                                 Execute some code if a value matches a 'case'
#                                 Benefits : cleaner and syntax is more readable


# by using elif statements


def num_of_week(day):

    if day == 1:
        return "It is Sunday"

    elif day == 2:

        return "It is Monday"

    elif day == 3:

        return "It is Tuesday"

    elif day == 4:

        return "It is Wednesday"

    elif day == 5:

        return "It is Thursday"

    elif day == 6:

        return "It is Friday"

    elif day == 7:

        return "It is Saturday"
    else:

        return "It is not valid !!!"

print(num_of_week(1))


# Using match-case statement (Switch)

# new feature added in python 3.10

# it does not work in below python versions like 3.09 , 3.08 etc.,

# below is a multiline comment code


'''def num_of_weeks(day):

    match day:
        case 1:
            return"Monday"
        case 2:
            return"Tuesday"
        case 3:
            return"Wednesday"
        case 4:
            return"Thursday"
        case 5:
            return"Friday"
        case 6:
            return"Saturday"
        case 7:
            return"Sunday"

        case _:
            return"Not a valid number"

print(num_of_weeks(1))'''

# above is a multiline comment code in python

# used for temporarily

#Use Triple Quotes

''' or """ (For Docstrings or Temporary Blocks)
Python treats triple-quoted strings as multi-line string literals, which can be used as:
- Docstrings (attached to functions/classes)
- Temporary comments (ignored if not assigned or used)
⚠️ Note: Triple-quoted strings are not true comments — they’re still parsed and stored in memory. 
Use them sparingly outside of docstrings.'''


# you can use an alternative method

# it is also only works in  new feature  python 3.10 or latest versions

'''def is_weekend():
    match day:
        case "Saturday" | "Sunday":
            return True
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return False
        case _:
            print("Invalid type !!!")
print(is_weekend("Saturday"))'''