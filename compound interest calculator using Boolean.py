# compound interest calculator

# in this method the user can enter zero

# it is not available in previous method


principle = 0

rate = 0

time = 0

while True :

    principle = float(input("Enter your principle amount : "))

    if principle < 0:

        print("The principle amount cannot be less than zero!")

    else:
        break

while  True:

    rate = float(input("Enter your interest rate : "))

    if rate < 0:

        print("The interest rate cannot be less than zero!")

    else:

        break

while  True:

    time = int(input("Enter the time in years : "))

    if time < 0:

        print("The time in years cannot be less than zero !")

    else:

        break

print(principle)
print(rate)
print(time)




total = principle * pow((1+rate / 100),time)

print(f"Balance after {time} year/s: {total:.2f}")

