# Measurement Converter

unit = input("Is this temparature is Celcius or Fahrenheit (C/F) : ")

temp = float(input("Enter the temparature : "))

if unit == "C":

    temp = round((9*temp)/5+32,1)

    print(f"The temparature in Fahrenheit is : {temp}°F")

elif unit == "F":

    temp = round((temp-32)*5/9, 1)

    print(f"the temparature in Celcius is: {temp}°C")

else:
    print(f"{unit} is an invalid unit of measurement")
