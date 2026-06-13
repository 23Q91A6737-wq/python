# compound interest calculator

principle = 0

rate = 0

time = 0

while principle <= 0:

    principle = float(input("Enter your principle amount : "))

    if principle <= 0:

        print("The principle amount cannnot be less than or equal to zero ! ")



while rate <= 0:

    rate = float(input("Enter your interset rate : "))

    if rate <= 0:

        print("The interest rate cannot be less than or equal to zero")



while time <= 0:

    time = float(input("Enter the time : "))

    if time <= 0:

        print("The time cannot be less than ")



print(principle)

print(rate)

print(time)



total = principle * pow((1+rate / 100),time)

print(f"Balance after {time} year/s: {total:.2f}")

