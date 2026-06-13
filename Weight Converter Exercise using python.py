# Python weight converter

weight = float(input("Enter your weight : "))

unit = input("Enter Kilograms or Pounds ? (K or L) : ")

if unit == "K":

    weight = weight * 2.205

    unit = "Lbs."
    
    print(f"Your weight is {weight}{unit}")

elif unit == "L":

    weight = weight / 2.205

    unit = "Kgs."

    print(f"Your weight is {weight}{unit}")
else:

    print(f"your weight is {weight}{unit}  not valid !")


# Python Calculator Optional

# if you don't want answers like 3.1423456

# just add round figure for 2 float points like 3.14

weight = float(input("Enter your weight : "))

unit = input("Enter Kilogram or Pounds ? (K or L) :")

if unit == "K":

    weight =weight * 2.205

    unit = "Lbs."

    print(f"Your weight is : {round(weight,2)}{unit}")

elif unit == "L":

    weight = weight / 2.205

    unit = "Kgs."

    print(f"Your weight is : {round(weight,2)}{unit}")

else:

    print(f"Your weight is {round(weight,2)} {unit} ")















