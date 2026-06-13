# conditional expression = A one-line shortcut for the if-else statement (ternary operator)

#                          print or assign one of two values based on a condition

#                          X if condition else Y

# Example :- 1

num = 7

#     Example Formula :- print("X if condition else Y")

print("Positive" if num > 0 else "Negative")

# Example :-2

num = -21

print("Positive" if num>0 else "Negative")

# Example 3:-

num = -11

print("Negative" if num<0 else "Positive")


# Example for Even

num = 8

print("EVEN" if num %2 == 0 else "ODD")

# Example for ODD

num = 7

print("ODD" if num %2 != 0 else "EVEN")

# In other form of writing EVEN and ODD functions

# Example for EVEN(1)

num = 10

result = "EVEN" if num %2 == 0 else "ODD"

print(result)

#Example for ODD(1)

num = 27

result = "ODD" if num %2 != 0 else "EVEN"

print(result)

# Example for Finding the Maximum Number(MAX)

a = 21

b = 7

max_num =a if a > b  else b

print(max_num)

# Example for Finding the Minimum Number(MIN)

a = 88

b = 116

min_num = a if a<b else b

print(min_num)

# To find the status in conditional expression

age = 21

status = "ADULT" if age >= 18  else "Child"

#print(status)

# or print(f"{status}")

print(f"{status}")

# Example for status for confirmation
age = 17

status = "ADULT" if age >=18  else "CHILD"

print(status)

# Example on Finding Temperature if HOT or COLD or WARM

temperature = 37

temp = "HOT" if temperature >= 40  else "WARM"

print(temp)

# Example on temperature 2:-

temperature = 40

temp = "VERY HOT 🌞🌞🌞" if temperature >= 40 else "WARM ☀️"

print(temp)

# Example on temperature 3:-

weather = 35

temp = "CLOUDY ☁️⛅🌥️ " if weather <= 37 else "COLD 🥶❄️"

print(temp)

# Example on condition expression

# example using admin

user_role = "admin"

access_level = "Full Access" if user_role == "admin" else "Limited Access"

print(access_level)

# Example 2:- on using user_role

user_role = "guest"

access_level = "Full Access" if user_role == "admin" else "Limited Access"

print(access_level)









