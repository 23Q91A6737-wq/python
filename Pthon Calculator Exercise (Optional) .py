# Python Calculator Optional

# Because in this program you can change the the answer if the

# Division like 22/7 = 3.1434567890

# you will get the answer like = 3.143

# in below example we taken 3 means the answer in points prints only
# three decimals after answer

# But you can take according to your wish !


operator = input("Enter an operator ( + - * / ):  ")

num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))

if operator == "+":

   result = num1+num2

   print(result,3)

elif operator == "-":

    result = num1-num2

    print(result,3)

elif operator == "*":

    result = num1*num2

    print(result,3)

elif operator == "/":

    result = num1/num2

    print(result,3)

else:

    print(f"{operator} is not valid operator ")

# Here else statement is used because if user types the words like

# car, bike , aeroplane , ship

