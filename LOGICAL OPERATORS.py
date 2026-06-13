# Logical Operators                                    (1:16:10) BroCode

# Logical Operators = evaluate multiple conditions (or, and, not)

#                     or = at least one condition must be True

#                     and = both conditions must be True

#                     not = inverts the condition (not False, not True)

temp =33

is_raining = True

if temp > 35 or temp < 0 or is_raining:

    print("The outdoor event is cancelled")

else:

    print("The outdoor event is still sheduled ")

# in the above example the temperature(temp) in first line you an
# assign a value after assigning the value
# the condition temp>35 or temp < 0 or is_raining
# if temp in first line is greater than 35 it will rain
# if the temperature is less than 0 it will rain

# Logical Operator

# and = both conditions must be True

temp = -27

is_sunny = False

if temp >= 28 and is_sunny:

    print("It is HOT outside 🥵🥵🥵")
    print("It is SUNNY ☀️🌄🌻🌅🌦️🌥️🌤️⛅🌞")

elif temp <= 0 and is_sunny:
    print("It is COLD outside 🥶❄️")
    print("It is SUNNY ☀️")

elif temp > 28 and temp < 0 and is_raining:

    print("It is WARM outside 😀")
    print("It is SUNNY🌞")
if temp >= 28 and not is_sunny:

    print("It is HOT outside 🥵🥵🥵")
    print("It is CLOUDY ⛅☁️")

elif temp <= 0 and not is_sunny:
    print("It is COLD outside 🥶❄️")
    print("It is CLOUDY ☁️⛅")

elif temp > 28 and temp < 0 and not is_raining:

    print("It is WARM outside 😀")
    print("It is CLOUDY ⛅☁️")



else:
    print("it is not valid ! ")
